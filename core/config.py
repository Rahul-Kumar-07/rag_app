from dotenv import load_dotenv
import os

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
GOOGLE_API_KEY = os.getenv("GEMINI_API_KEY")

PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
PINECONE_INDEX_NAME = os.getenv("PINECONE_INDEX")

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")



# from dotenv import load_dotenv

# from pydantic_settings import BaseSettings
# from pydantic import ConfigDict

# load_dotenv()


# class Settings(BaseSettings):

#     # Gemini
#     GEMINI_API_KEY: str

#     # Pinecone
#     PINECONE_API_KEY: str
#     PINECONE_INDEX_NAME: str

#     # Supabase
#     SUPABASE_URL: str
#     SUPABASE_KEY: str

#     model_config = ConfigDict(
#         env_file=".env",
#         extra="ignore"
#     )


# settings = Settings()