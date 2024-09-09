import json

import click
import openai
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

MODEL = "gpt-4o-mini-2024-07-18"


@click.command()
@click.argument("messages_file")
def chat_with_openai(messages_file: str):
    messages = json.load(open(messages_file))
    try:
        response = openai.chat.completions.create(
            model=MODEL,
            messages=messages,
        )
        print(response.choices[0].message.content)
    except Exception as e:
        print(f"An error occurred: {e!s}")


if __name__ == "__main__":
    chat_with_openai()
