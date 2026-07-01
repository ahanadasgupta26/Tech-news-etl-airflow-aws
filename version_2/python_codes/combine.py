import pandas as pd

def combine_news(ti):

    ai = ti.xcom_pull(task_ids="transform_ai_news")
    ds = ti.xcom_pull(task_ids="transform_data_science_news")
    ml = ti.xcom_pull(task_ids="transform_machine_learning_news")
    cloud = ti.xcom_pull(task_ids="transform_cloud_news")
    cyber = ti.xcom_pull(task_ids="transform_cybersecurity_news")

    all_news = ai + ds + ml + cloud + cyber

    df = pd.DataFrame(all_news)

    df.drop_duplicates(subset=["url"], inplace=True)

    df.fillna("", inplace=True)

    return df.to_dict(orient="records")