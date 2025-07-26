# imports
# If these fail, please check you're running from an 'activated' environment with (llms) in the command prompt

import os
import requests
import json
from typing import List
from dotenv import load_dotenv
from bs4 import BeautifulSoup
from IPython.display import Markdown, display, update_display
from openai import OpenAI

# Rich text TUI

from rich import print as rprint
from rich.markdown import Markdown

# Initialize and constants

load_dotenv(override=True)
api_key = os.getenv("OPENAI_API_KEY")

if api_key and api_key.startswith("sk-proj-") and len(api_key) > 10:
    rprint("API key looks good so far")
else:
    print(
        "There might be a problem with your API key? Please visit the troubleshooting notebook!"
    )

MODEL = "gemma3:12b-it-qat"
# openai = OpenAI()
openai = OpenAI(base_url="http://localhost:11434/v1", api_key="ollama")
