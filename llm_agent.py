import os
import random
from openai import OpenAI
from dotenv import load_dotenv
import config

load_dotenv()

class Agent:
    def __init__(self):
        self.client = OpenAI(api_key=os.getenv("OPEN_API_KEY"))
    
    def generate_content(self):
        selected_topic = random.choice(config.TOPICS)
    
        response = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": config.SYSTEM_PROMPT},
                {"role": "user", "content": f"Topic: {selected_topic}\n\nRules:\n{config.RULES}"}
            ]
        )

        content = response.choices[0].message.content.strip()
        return content.encode('ascii', 'ignore').decode('ascii')
    
