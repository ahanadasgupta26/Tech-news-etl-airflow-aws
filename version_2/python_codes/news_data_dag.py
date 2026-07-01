from airflow import DAG
from airflow.providers.standard.operators.python import PythonOperator
from datetime import datetime, timedelta
from extract import extract_news
from transform import transform_news
from combine import combine_news
from load import upload_to_s3

default_args = {
    "owner": "ahana",
    "depends_on_past": False,
    "email_on_retry": False,
    "email_on_failure": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

dag = DAG(
    dag_id="tech_news_etl",
    default_args=default_args,
    description="ETL Pipeline for Tech News",
    start_date=datetime(2023, 1, 1),
    schedule="@daily",
    catchup=False,
)

# ---------------------- Extract Tasks ----------------------

extract_ai = PythonOperator(
    task_id="extract_ai_news",
    python_callable=extract_news,
    op_kwargs={"query": "artificial intelligence"},
    dag=dag,
)

extract_ds = PythonOperator(
    task_id="extract_data_science_news",
    python_callable=extract_news,
    op_kwargs={"query": "data science"},
    dag=dag,
)

extract_ml = PythonOperator(
    task_id="extract_machine_learning_news",
    python_callable=extract_news,
    op_kwargs={"query": "machine learning"},
    dag=dag,
)

extract_cloud = PythonOperator(
    task_id="extract_cloud_news",
    python_callable=extract_news,
    op_kwargs={"query": "cloud computing"},
    dag=dag,
)

extract_cyber = PythonOperator(
    task_id="extract_cybersecurity_news",
    python_callable=extract_news,
    op_kwargs={"query": "cybersecurity"},
    dag=dag,
)

# ---------------------- Transform Tasks ----------------------

transform_ai = PythonOperator(
    task_id="transform_ai_news",
    python_callable=transform_news,
    op_kwargs={"category": "AI"},
    dag=dag,
)

transform_ds = PythonOperator(
    task_id="transform_data_science_news",
    python_callable=transform_news,
    op_kwargs={"category": "Data Science"},
    dag=dag,
)

transform_ml = PythonOperator(
    task_id="transform_machine_learning_news",
    python_callable=transform_news,
    op_kwargs={"category": "Machine Learning"},
    dag=dag,
)

transform_cloud = PythonOperator(
    task_id="transform_cloud_news",
    python_callable=transform_news,
    op_kwargs={"category": "Cloud"},
    dag=dag,
)

transform_cyber = PythonOperator(
    task_id="transform_cybersecurity_news",
    python_callable=transform_news,
    op_kwargs={"category": "Cybersecurity"},
    dag=dag,
)

# ---------------------- Combine Task ----------------------

combine = PythonOperator(
    task_id="combine_all_news",
    python_callable=combine_news,
    dag=dag,
)

# ---------------------- Upload Task ----------------------

upload = PythonOperator(
    task_id="upload_to_s3",
    python_callable=upload_to_s3,
    dag=dag,
)

# ---------------------- Dependencies ----------------------

extract_ai >> transform_ai
extract_ds >> transform_ds
extract_ml >> transform_ml
extract_cloud >> transform_cloud
extract_cyber >> transform_cyber

[
    transform_ai,
    transform_ds,
    transform_ml,
    transform_cloud,
    transform_cyber,
] >> combine >> upload