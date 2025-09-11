import os
from google import genai
from google.genai import types
from PIL import Image
from io import BytesIO

def get_banana():
    client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

    # response = client.models.generate_content(
    #     model="gemini-2.5-flash", contents="Explain how AI works in a few words"
    # )
    # print(response.text)
    response = client.models.generate_images(
        model='imagen-4.0-generate-001',
        prompt='Robot holding a red skateboard',
        config=types.GenerateImagesConfig(
            number_of_images=1,
        )
    )
    for generated_image in response.generated_images:
        generated_image.image.show()
        return generated_image.image


