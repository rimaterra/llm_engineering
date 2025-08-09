# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "google.generativeai",
#     "python-dotenv",
#     "textual",
#     "openai",
# ]
# ///
import os
import argparse
import asyncio
import sys
import signal
from dotenv import load_dotenv
from textual.app import App, ComposeResult
from textual.widgets import Markdown
from openai import OpenAI
import google.generativeai

load_dotenv(override=True)
google_api_key = os.getenv("GOOGLE_AI_API_KEY")

# The LLM to run
# MODEL = "gemma3n:e2b"
MODEL = "gemini-2.5-flash-lite"
# MODEL = "gemini-2.5-flash"
# MODEL = "gemini-2.5-pro"
# MODEL = "mistral-small3.2:24b-instruct-2506-q8_0"
# MODEL = "gemma3:27b-it-qat"
# MODEL = "mistral-small3.2"
# MODEL = "devstral:24b"

system_prompt = "You are a helpful expert Python programmer. \
Respond in markdown."
# user_prompt = "Hello. Who are you?"
user_prompt = "What does temperature control in large language models?"


class MDApp(App):
    def __init__(self, usage: bool):
        super().__init__()
        self.usage = usage
        self.streaming = False

    def compose(self):
        yield Markdown()

    async def on_mount(self):
        # Set up signal handlers for proper cleanup
        signal.signal(signal.SIGINT, self._signal_handler)
        signal.signal(signal.SIGTERM, self._signal_handler)

        # Start streaming task
        self.streaming_task = asyncio.create_task(self._stream())

    def _signal_handler(self, signum, frame):
        """Handle Ctrl+C and other signals gracefully"""
        if self.streaming:
            self.streaming = False
        asyncio.create_task(self.exit())

    async def _stream(self):
        md = self.query_one(Markdown)
        self.streaming = True

        try:
            # Initialize OpenAI client for ollama
            # client = OpenAI(base_url="http://localhost:11434/v1", api_key="ollama")

            # Initialize OpenAI client for Google Gemini
            client = OpenAI(
                api_key=google_api_key,
                base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
            )

            # Create streaming completion
            stream = client.chat.completions.create(
                model=MODEL,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt},
                ],
                stream=True,
            )

            # Accumulate the response content
            content = ""

            # Process streaming chunks
            for chunk in stream:
                if not self.streaming:  # Check if we should stop
                    break

                # Extract content from chunk
                if chunk.choices and len(chunk.choices) > 0:
                    delta = chunk.choices[0].delta
                    if hasattr(delta, "content") and delta.content:
                        content += delta.content

                        # Update the markdown widget with accumulated content
                        await md.update(content)

                        # Small delay to prevent overwhelming the UI
                        await asyncio.sleep(0.01)

            # Add usage information if requested
            if self.usage and self.streaming:
                usage_info = "\n\n**Streaming completed**"
                content += usage_info
                await md.update(content)

        except KeyboardInterrupt:
            print("\nInterrupted by user")
            await md.update(content + "\n\n**Interrupted by user**")
        except Exception as e:
            error_msg = f"\n\n**Error: {str(e)}**"
            print(f"Error occurred: {e}")
            (
                await md.update(content + error_msg)
                if "content" in locals()
                else await md.update(f"**Error: {str(e)}**")
            )
        finally:
            self.streaming = False
            # Small delay before exit to show final content
            await asyncio.sleep(0.5)
            await self.exit()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--usage", action="store_true", help="Show usage")
    args = parser.parse_args()

    try:
        app = MDApp(args.usage)
        app.run(inline=True, inline_no_clear=True)
    except KeyboardInterrupt:
        print("\nExiting...")
        sys.exit(0)
