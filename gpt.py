import os
from openai import OpenAI

client = OpenAI(
    # This is the default and can be omitted
    # api_key=os.environ.get("OPENAI_API_KEY"),
    # api_key='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'
)

response = client.responses.create(
    model="gpt-4o",
    instructions="You are a coding assistant that talks like a pirate.",
    input="How do I check if a Python object is an instance of a class?",
)

print(response.output_text)