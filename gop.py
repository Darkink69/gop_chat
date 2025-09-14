import os
from openai import OpenAI


def get_gop():
    client = OpenAI(
        api_key=os.environ.get("OPENAI_API_KEY"),
    )

    response = client.responses.create(
        model="gpt-5-nano",
        instructions="Вы опытный повар",
        input="Как правильно варить макароны?",
    )

    print(response.output_text)
    return response.output_text
    # return "Как правильно варить макароны?"