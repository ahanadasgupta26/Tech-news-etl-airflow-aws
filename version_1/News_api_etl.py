import pandas as pd
import requests
import os
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

def run_news_etl():
    api_key = os.getenv("NEWS_API_KEY")
    base_url = "https://newsapi.org/v2/everything"

    params = {
        "q": "artificial intelligence",
        "language": "en",
        "pageSize": 100,
        "apiKey": api_key
    }

    response = requests.get(base_url, params=params)

    if response.status_code != 200:
        raise Exception(f"API Error: {response.text}")

    data = response.json()
    articles = data.get("articles", [])

    news_list = []

    for article in articles:
        news_list.append({
            "source": article.get("source", {}).get("name", ""),
            "author": article.get("author", ""),
            "title": article.get("title", ""),
            "description": article.get("description", ""),
            "url": article.get("url", ""),
            "publishedAt": article.get("publishedAt", ""),
            "content": article.get("content", "")
        })

    df = pd.DataFrame(news_list)

    filename = f"News_AI_ETL_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
    s3_path = f"s3://airflow-news-bucket/news/{filename}"

    df.to_csv(s3_path, index=False)