# Tech News ETL Pipeline with Airflow & AWS

An end-to-end Data Engineering project that extracts technology news from NewsAPI, transforms it using Python and Pandas, and stores the processed data in Amazon S3. The project is orchestrated using Apache Airflow and demonstrates how an ETL pipeline can evolve from a simple implementation to a modular, production-ready architecture.

---


|  Version      | Highlights |
|---------------|------------|
| **Version 1** | Single-file ETL implementation with a separate Airflow DAG. Processes **AI news** only. Best for understanding the fundamentals of an ETL pipeline. |
| **Version 2** | Fully modular ETL pipeline with separate modules for extraction, transformation, loading, and utility functions. Supports multiple news categories including **AI, Cybersecurity, Data Science, Machine Learning, Cloud Computing**, and more. Designed for better scalability and maintainability. |

---

# 📁 Version 1 – Basic ETL Pipeline

### Overview

Version 1 demonstrates the core ETL workflow in a simple and easy-to-understand structure.

### Key Characteristics

- Single ETL Python script containing the complete ETL logic
- Separate Apache Airflow DAG for orchestration
- Fetches **Artificial Intelligence** news from NewsAPI
- Cleans and transforms the data using Pandas
- Uploads the processed CSV to Amazon S3
- Ideal for learning the basics of ETL development

  ### Workflow

```text
NewsAPI (AI News)
        │
        ▼
Single ETL Script
(Extract + Transform + Load)
        │
        ▼
Amazon S3
        ▲
        │
Apache Airflow DAG
```
