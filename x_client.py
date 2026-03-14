import os
import tweepy
from dotenv import load_dotenv

load_dotenv()

class XClient:
    def __init__(self):
        self.client = tweepy.Client(
            consumer_key=os.getenv("X_API_KEY"),
            consumer_secret=os.getenv("X_API_SECRET"),
            access_token=os.getenv("X_ACCESS_TOKEN"),
            access_token_secret=os.getenv("X_ACCESS_SECRET")
        )
    
    def post_tweet(self, tweet):
        try:
            response = self.client.create_tweet(text=tweet)
            return response
        except Exception as e:
            print(f"Error while posting: {e}")
            return None