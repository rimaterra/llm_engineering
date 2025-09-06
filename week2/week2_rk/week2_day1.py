# imports

import os
from dotenv import load_dotenv
from openai import OpenAI

# import anthropic
from rich import print as rprint
from rich.markdown import Markdown

# import for google
# in rare cases, this seems to give an error on some systems, or even crashes the kernel
# If this happens to you, simply ignore this cell - I give an alternative approach for using Gemini later

import google.generativeai

# Load environment variables in a file called .env
# Print the key prefixes to help with any debugging

load_dotenv(override=True)
openai_api_key = os.getenv("OPENAI_API_KEY")
anthropic_api_key = os.getenv("ANTHROPIC_API_KEY")
google_api_key = os.getenv("GOOGLE_AI_API_KEY")

if openai_api_key:
    print(f"OpenAI API Key exists and begins {openai_api_key[:8]}")
else:
    print("OpenAI API Key not set")

if google_api_key:
    print(f"Google API Key exists and begins {google_api_key[:8]}")
else:
    print("Google API Key not set")
    # Connect to OpenAI, Anthropic

# Connect to OpenAI

openai = OpenAI(base_url="http://localhost:11434/v1", api_key="ollama")
# MODEL = "gemma3:4b-it-qat"
MODEL = "gemma3n"

# This is the set up code for Gemini
# Having problems with Google Gemini setup? Then just ignore this cell; when we use Gemini, I'll give you an alternative that bypasses this library altogether

# google.generativeai.configure()

system_message = "You are an assistant that is great at telling jokes"
user_prompt = "Tell a light-hearted joke for an audience of Data Scientists"

prompts = [
    {"role": "system", "content": system_message},
    {"role": "user", "content": user_prompt},
]

# GPT

# completion = openai.chat.completions.create(model=MODEL, messages=prompts)
# print(completion.choices[0].message.content)

# Temperature setting controls creativity

# completion = openai.chat.completions.create(
#     model=MODEL, messages=prompts, temperature=0.7
# )
# print(completion.choices[0].message.content)

# As an alternative way to use Gemini that bypasses Google's python API library,
# Google released endpoints that means you can use Gemini via the client libraries for OpenAI!
# We're also trying Gemini's latest reasoning/thinking model

gemini_via_openai_client = OpenAI(
    api_key=google_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

response = gemini_via_openai_client.chat.completions.create(
    model="gemini-2.5-flash", messages=prompts, temperature=0.9
)
rprint(Markdown("# Response from Gemini Flash"))
rprint(Markdown("## Tell a light-hearted joke for an audience of Data Scientists"))
rprint(Markdown(response.choices[0].message.content))

# Gemma3n with the original question

rprint(Markdown("# Response from gemma3n"))
rprint(Markdown("## Tell a light-hearted joke for an audience of Data Scientists"))

prompts = [
    {
        "role": "system",
        "content": "You are a helpful assistant that responds in Markdown",
    },
    {
        "role": "user",
        "content": "Tell a light-hearted joke for an audience of Data Scientists",
        # "content": "Who are you? Please respond in Markdown.",
        # "content": "How do I decide if a business problem is suitable for an LLM solution? Please respond in Markdown.",
    },
]

# Have it stream back results in markdown
#
# The `openai.chat.completions.create` method, when used in streaming
# mode, returns an iterator that yields `ChatCompletionChunk` objects.
# Each `ChatCompletionChunk` object represents a part of the streamed
# response and contains a `delta` object. The `delta` object has a
# `content` attribute, which holds a fragment of the Markdown text.
#
# To print the complete Markdown response to the console, you need to
# iterate through the stream and concatenate the `content` from each
# `delta` object.


stream = openai.chat.completions.create(
    model=MODEL, messages=prompts, temperature=0.7, stream=True
)

reply = ""

for chunk in stream:
    if chunk.choices[0].delta.content is not None:
        # Print the raw contents. It looks like we're getting one token
        # in every chunk.
        # Suppress the automatic newline in print by using the "end" option.
        print(chunk.choices[0].delta.content, end="")
        reply += chunk.choices[0].delta.content

# We've seen the raw contents. All the contents have been concatenated into "reply"
# Now let's view the formatted output using the Rich library.
rprint(Markdown("\n\n# Full response received and printed."))
rprint(Markdown(reply))
