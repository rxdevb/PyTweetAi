import os
from dotenv import load_dotenv
from openai import OpenAI
import tweepy

load_dotenv()

openai_key = os.getenv("OPENAI_API_KEY")
x_api_key = os.getenv("X_API_KEY")
x_api_secret = os.getenv("X_API_SECRET")
x_access_token = os.getenv("X_ACCESS_TOKEN")
x_access_secret = os.getenv("X_ACCESS_SECRET")

print("Starting X-Agent...")

try:
    print("\n1. Waking up AI to write a tweet...")

    ai_client = OpenAI(api_key=openai_key)

    ai_response = ai_client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a senior enterprise software engineer writing plain text technical documentation. Do NOT write like a social media influencer. Zero emojis. Zero symbols. Only use standard ASCII characters."},
            {"role": "user", "content": "Write a short, engaging, and slightly humorous insight about Python programming. It must be genuinely valuable to a senior developer. \n\nRULES:\n- Output ONLY the text of the message.\n- NO emojis whatsoever.\n- NO unicode symbols.\n- End with exactly: #Python #SoftwareEngineering"}
        ]
    )

    generated_tweet = ai_response.choices[0].message.content
    
    generated_tweet = generated_tweet.encode('ascii', 'ignore').decode('ascii').strip()
    
    print(f"Generated tweet: \n{generated_tweet}\n")

    print("2. Connecting to X to publish the tweet...")

    x_client = tweepy.Client(
        consumer_key=x_api_key,
        consumer_secret=x_api_secret,
        access_token=x_access_token,
        access_token_secret=x_access_secret
    )

    tweet_response = x_client.create_tweet(text=generated_tweet)

    print("Tweet posted automatically! Check your X profile.")

except Exception as e:
    print(f"Error: Something went wrong. Details: {e}")