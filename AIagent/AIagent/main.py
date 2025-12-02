import os

from dotenv import load_dotenv
from google import genai


def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        raise RuntimeError("GEMINI_API_KEY environment variable not set")

    client = genai.Client(api_key="AIzaSyBwkNNj9EhkM1wBBWuRMHWZFHWipb7cnv8")
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents="Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum.",
    )
    
    print("Response:")
    print(response.text)
    print(response.usage_metadata.prompt_token_count)
    print(response.usage_metadata.candidates_token_count)

if __name__ == "__main__":
    main()
