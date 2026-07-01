import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("NEWS_API_KEY")
BASE_URL = "https://newsapi.org/v2/everything"


def extract_news(query):

    params = {
        "q": query,
        "language": "en",
        "pageSize": 100,
        "apiKey": API_KEY,
    }

    response = requests.get(
        BASE_URL,
        params=params,
        timeout=30,
    )

    if response.status_code != 200:
        raise Exception(response.text)

    return response.json().get("articles", [])