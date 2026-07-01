import pandas as pd

def transform_news(category, ti):
    articles = ti.xcom_pull(
        task_ids=f"extract_{category.lower().replace(' ', '_')}_news"
    )

    news = []

    for article in articles:
        news.append({
            "category": category,
            "source": article.get("source", {}).get("name", ""),
            "author": article.get("author", ""),
            "title": article.get("title", ""),
            "description": article.get("description", ""),
            "url": article.get("url", ""),
            "publishedAt": article.get("publishedAt", ""),
            "content": article.get("content", "")
        })

    df = pd.DataFrame(news)

    df.drop_duplicates(subset=["url"], inplace=True)

    df.fillna("", inplace=True)

    return df.to_dict(orient="records")