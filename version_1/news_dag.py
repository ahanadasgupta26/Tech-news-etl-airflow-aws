from datetime import datetime, timedelta
from airflow import DAG
from airflow.providers.standard.operators.python import PythonOperator
from datetime import datetime
from News_api_etl import run_news_etl

default_args = {
    "owner": "ahana",
    "depends_on_past": False,
    "email_on_retry": False,
    "email_on_failure": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

dag=DAG(
    dag_id="news_api_etl",
    default_args=default_args,
    description='ETL for AI news using news API',
    start_date=datetime(2023,1,1),
    schedule='@daily',
    catchup=False
)

task=PythonOperator(
    task_id="news_etl",
    python_callable=run_news_etl,
    dag=dag,
)

task