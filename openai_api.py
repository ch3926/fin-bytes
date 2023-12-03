from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

# Variables for user experience level and interests
user_experience = "intermediate"
user_interests = "Stocks, Cryptocurrency"

week_number = 2

# Format the user prompt using f-string
user_prompt = f"Create a weekly snippet for a user who is a {user_experience} at investing, and is interested in investing in {user_interests}. This is for Week {week_number}"

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

# Print the Snippet and Quiz
print("Snippet:")
print(snippet)
print("\nQuiz:")
print(quiz)