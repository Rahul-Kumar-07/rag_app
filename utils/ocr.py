from google import genai

from PIL import Image

from core.config import GOOGLE_API_KEY
from core.prompts import OCR_PROMPT

client = genai.Client(
    api_key=GOOGLE_API_KEY
)

def extract_text_from_image(path):

    image = Image.open(path)

    response = client.models.generate_content(

        model="gemini-2.5-flash",

        contents=[
            OCR_PROMPT,
            image
        ]
    )

    return response.text