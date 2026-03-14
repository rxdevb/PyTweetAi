from llm_agent import Agent
from x_client import XClient

def run_agent():
    print("Starting X-Agent...")

    agent = Agent()
    x_bot = XClient()

    print("Generating post...")
    tweet_content = agent.generate_content()
    print(f"Generated content: {tweet_content}")

    print("Posting to X...")
    success = x_bot.post_tweet(tweet_content)

    if success:
        print("Tweet posted successfully.")
    else:
        print("Failed to post.")

if __name__ == "__main__":
    run_agent()
