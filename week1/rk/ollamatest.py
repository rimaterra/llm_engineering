from openai import OpenAI

MODEL = "gemma3:27b-it-qat"
openai = OpenAI(base_url="http://localhost:11434/v1", api_key="ollama")

response = openai.chat.completions.create(
    model=MODEL, messages=[{"role": "user", "content": "What is 2 + 2?"}]
)

print(response.choices[0].message.content)
