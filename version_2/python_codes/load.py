import pandas as pd
from datetime import datetime

def upload_to_s3(ti):

    data = ti.xcom_pull(task_ids="combine_all_news")

    df = pd.DataFrame(data)

    filename = f"Tech_News_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"

    path = f"s3://airflow-news-bucket/tech-news/{filename}"

    df.to_csv(path, index=False)

    print(f"Uploaded successfully to {path}")