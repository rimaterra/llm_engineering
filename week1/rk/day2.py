# imports

import os
import requests
from bs4 import BeautifulSoup

# Rich text TUI

from rich import print as rprint
from rich.markdown import Markdown

# Constants

OLLAMA_API = "http://localhost:11434/api/chat"
HEADERS = {"Content-Type": "application/json"}
# MODEL = "llama3.2"
MODEL = "mistral-small3.2"

# Create a messages list using the same format that we used for OpenAI

messages = [
    {
        "role": "user",
        "content": "Describe some of the business applications of Generative AI",
    }
]
payload = {"model": MODEL, "messages": messages, "stream": False}
# If this doesn't work for any reason, try the 2 versions in the following cells
# And double check the instructions in the 'Recap on installation of Ollama' at the top of this lab
# And if none of that works - contact me!

response = requests.post(OLLAMA_API, json=payload, headers=HEADERS)
rprint(response.json()["message"]["content"])
