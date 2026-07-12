# Tech News ETL Pipeline with Airflow & AWS

## An end-to-end Data Engineering project that extracts technology news from NewsAPI, transforms it using Python and Pandas, and stores the processed data in Amazon S3. The project is orchestrated using Apache Airflow and demonstrates how an ETL pipeline can evolve from a simple implementation to a modular, production-ready architecture.

---


|  Version      | Highlights |
|---------------|------------|
| **Version 1** | Single-file ETL implementation with a separate Airflow DAG. Processes **AI news** only. Best for understanding the fundamentals of an ETL pipeline. |
| **Version 2** | Fully modular ETL pipeline with separate modules for extraction, transformation, loading, and utility functions. Supports multiple news categories including **AI, Cybersecurity, Data Science, Machine Learning, Cloud Computing**, and more. Designed for better scalability and maintainability. |
