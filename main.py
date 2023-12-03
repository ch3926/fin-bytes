import get_user_data
import news_api
import openai_api
import firebase
from openai import OpenAI
from dotenv import load_dotenv
import json
import json
from datetime import datetime, timedelta
from newsapi import NewsApiClient
import csv
import ssl
import smtplib


# Init
newsapi = NewsApiClient(api_key='01246e43061d4f3f981373160e2b4ec5')

# Calculate the date range for the last week
end_date = datetime.now()
start_date = end_date - timedelta(days=7)

# Format dates in the required News API format (YYYY-MM-DD)
from_date_str = start_date.strftime('%Y-%m-%d')
to_date_str = end_date.strftime('%Y-%m-%d')

# List of relevant financial news domains
financial_news_domains = [
    'wsj.com',        # The Wall Street Journal
    'forbes.com',     # Forbes
    'bloomberg.com',  # Bloomberg
    'ft.com',         # Financial Times
    'cnbc.com',       # CNBC
    'reuters.com',    # Reuters
    'investopedia.com',  # Investopedia
    'marketwatch.com',  # MarketWatch
    'fool.com',       # The Motley Fool
    'seekingalpha.com'   # Seeking Alpha
]

# Make the News API request for the last week with domain filtering and top 50 articles
all_articles = newsapi.get_everything(
    q='stocks | stock market',
    from_param=from_date_str,
    to=to_date_str,
    language='en',
    sort_by='popularity', 
    domains=','.join(financial_news_domains),  # Convert the list to a comma-separated string
    page_size=30  # Limit the number of articles to 30
)

# Remove unwanted fields from each article
cleaned_articles = []
for article in all_articles['articles']:
    cleaned_article = {
        'source': article['source'],
        'title': article['title'],
        'description': article['description'],
        'url': article['url']
    }
    cleaned_articles.append(cleaned_article)

# Create a dictionary with cleaned data
cleaned_data = {
    'status': all_articles['status'],
    'totalResults': all_articles['totalResults'],
    'articles': cleaned_articles
}

# Convert the cleaned data to a JSON file
output_file_path = 'financial_news_articles.json'
with open(output_file_path, 'w') as json_file:
    json.dump(cleaned_data, json_file, indent=2)

print(f'Cleaned financial news articles saved to {output_file_path}')


def openai_summary(level, interests):
    load_dotenv()

    client = OpenAI()

    # Variables for user experience level and interests
    #user_experience = "intermediate"
    #user_interests = "Stocks"

    # Load the news articles from the JSON file
    input_file_path = 'financial_news_articles.json'
    with open(input_file_path, 'r') as json_file:
        news_articles = json.load(json_file)['articles']

    # Prepare the input for GPT-3.5
    input_text = f'Create a list of 5 articles for a user who is a {level}, and interested iinvesting in {interests}. Here are the news articles:'

    for article in news_articles:
        input_text += f"Title: {article['title']}\nSource: {article['source']['name']}\nDescription: {article['description']}\nLink: {article['url']}\n\n"

    # Generate a summary using GPT-3.5
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant, who goes through a JSON file with extracted news articles, and based on the context provided, selects 5 helpful news articles that should be selected to display to the user. The information to be selected is the title, the news source (website), a brief description, and the link to the article. Make sure to also select articles from varied sources, to ensure diversity of topics being covered. Just give me the articles without any text before or after the list. "},
            {"role": "user", "content": input_text}
        ]
    )

    # Extract the generated summary
    generated_summary = completion.choices[0].message.content

    # Print the generated summary
    #print(generated_summary)

    week_number = 2

    # Format the user prompt using f-string
    user_prompt = f"Create a weekly snippet for a user who is a {level} at investing, and is interested in investing in {interests}. This is for Week {week_number}"

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant who creates useful and educational snippets of information that would go out to a user on a week by week basis. These snippets will cater to information regarding investing, and should range between 500 - 700 words. You must not repeat information mentioned in a previous email, and strive to provide all information that a user may need to get into investing. The tone should be friendly, yet formal. The level of the weekly snippets should also increase week by week. Towards the end of this message, you must create a small quiz with 3-4 questions to engage the user and help them check how much of the snippet they have understood. Label the first part as 'Snippet', and label the second part as 'Quiz' "},

            {"role": "user", "content": user_prompt}
        ]
    )

    # Extract the ChatCompletionMessage object
    chat_completion_message = completion.choices[0].message

    # Extract the content from the message
    content = chat_completion_message.content

    # Find the index of "Snippet:" and "Quiz:"
    snippet_index = content.find("Snippet:")
    quiz_index = content.find("Quiz:")

    # Extract the Snippet and remove the label
    snippet_label_length = len("Snippet:")
    snippet = content[snippet_index + snippet_label_length:quiz_index].strip()

    # Extract the Quiz and remove the label
    quiz_label_length = len("Quiz:")
    quiz = content[quiz_index + quiz_label_length:].strip()

    """# Print the Snippet and Quiz
    print("Snippet:")
    print(snippet)
    print("\nQuiz:")
    print(quiz)"""

    email_string = snippet + '\n\n' + generated_summary + '\n\n Quiz: ' + quiz

    return email_string

with open("user_info.csv") as file:
            reader = csv.reader(file)
            next(reader)  # Skip header row
            for user in reader:
                first_name = user[0]
                last_name = user[1]
                email = user[2]
                level = user[3]
                interests = user[4]
                date_time = user[5]

                email_string = openai_summary(level, interests)






def send_mail(news, summary):

    from_address = "finbytes.info@gmail.com"
    email_password = "ytge xsnj zrnl xigg"

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(from_address, email_password)

        with open("user_info.csv") as file:
            reader = csv.reader(file)
            next(reader)  # Skip header row
            for user in reader:
                first_name = user[0]
                last_name = user[1]
                email = user[2]
                level = user[3]
                interests = user[4]
                date_time = user[5]

                email_string = openai_summary(level, interests)

                message = """Subject: Weekly Fin Byte!

                Hi {firstName} {lastName}, here is your weekly update on {interests} 

                {email_string}

                Best Wishes,

                Team FinBytes
                """

                server.sendmail(
                    from_address,
                    email,
                    message.format(firstName=first_name,lastName=last_name, interests=interests, email_string=email_string),
            )

send_mail()














