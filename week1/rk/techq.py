# imports

import os
import requests
from dotenv import load_dotenv
from bs4 import BeautifulSoup

from openai import OpenAI

# Rich text TUI

from rich import print as rprint
from rich.markdown import Markdown

# The large LLM to run
MODEL = "gemma3n:e2b"
# MODEL = "mistral-small3.2:24b-instruct-2506-q8_0"
# MODEL = "gemma3:27b-it-qat"
# MODEL = "mistral-small3.2"
# MODEL = "devstral:24b"

system_prompt = "You are a friendly expert Python programmer. \
Respond in markdown."

# set up environment

load_dotenv(override=True)
api_key = os.getenv("OPENAI_API_KEY")

# Check the key

if not api_key:
    print(
        "No API key was found - please head over to the troubleshooting notebook in this folder to identify & fix!"
    )
elif not api_key.startswith("sk-proj-"):
    print(
        "An API key was found, but it doesn't start sk-proj-; please check you're using the right key - see troubleshooting notebook"
    )
elif api_key.strip() != api_key:
    print(
        "An API key was found, but it looks like it might have space or tab characters at the start or end - please remove them - see troubleshooting notebook"
    )
else:
    print("\n")  # Looks good

openai = OpenAI(base_url="http://localhost:11434/v1", api_key="ollama")

# here is the question; type over this to ask something new

code_question = """
Please explain what this code does and why:
yield from {book.get("author") for book in books if book.get("author")}
"""


def user_prompt_for(question):
    user_prompt = f"Please provide an answer to the following technical question suitable to a beginner programmer."
    user_prompt += question
    return user_prompt


def messages_for(question):
    return [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt_for(question)},
    ]


def answer(question):
    response = openai.chat.completions.create(
        model=MODEL, messages=messages_for(question)
    )
    return response.choices[0].message.content


def display_answer(question):
    ans = answer(question)
    rprint(Markdown(ans))


rprint(Markdown("# Question"))
rprint(Markdown(code_question))

rprint(Markdown("## Answer"))
display_answer(code_question)

# Get the llm to answer, with streaming
