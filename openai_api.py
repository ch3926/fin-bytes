from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

# Variables for user experience level and interests
user_experience = "beginner"
user_interests = "Stocks"

# Format the user prompt using f-string
user_prompt = f"Create a weekly snippet for a user who is a {user_experience} at investing, and is interested in investing in {user_interests}. This is for Week 1"

completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant who creates useful and educational snippets of information that would go out to a user on a week by week basis. These snippets will cater to information regarding investing, and should range between 500 - 700 words. You must not repeat information mentioned in a previous email, and strive to provide all information that a user may need to get into investing. The tone should be friendly, yet formal. The level of the weekly snippets should also increase week by week. "},

        {"role": "user", "content": user_prompt}
    ]
)

print(completion.choices[0].message['content'])
