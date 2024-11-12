from openai import OpenAI
from config import logger, OPENAI_MODEL, SYSTEM_PROMPT


class OpenAIService:
    def __init__(self):
        self.client = OpenAI()

    def generate_response(self, username: str, message: str) -> str:
        try:
            completion = self.client.chat.completions.create(
                model=OPENAI_MODEL,
                messages=[
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {
                        "role": "user",
                        "content": f"Write a get well soon message reply for {username}. He/She texted in the office group that {message}",
                    },
                ],
            )
            return completion.choices[0].message.content
        except Exception as e:
            logger.error(f"Error generating OpenAI response: {str(e)}")
            return "Sorry, I encountered an error generating a response."
