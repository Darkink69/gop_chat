import os
from openai import OpenAI


def get_gop(prompt):
    client = OpenAI(
        api_key=os.environ.get("OPENAI_API_KEY"),
    )

    response = client.responses.create(
        model="gpt-5-nano",
        input=prompt,
        store=True,
    )

    print(response.output_text)
    return response.output_text
    # return "Как правильно варить макароны?"