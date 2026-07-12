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
```
                NewsAPI
                   │
                   ▼
          Apache Airflow DAG
                   │
                   ▼
     Single ETL Python Script
 (Extract + Transform + Load)
                   │
                   ▼
        Processed CSV/DataFrame
                   │
                   ▼
          Upload to Amazon S3
```
---
# 📁 Version 2 – Modular ETL Pipeline

### Overview

Version 2 refactors the pipeline into a modular architecture following better software engineering practices. Each stage of the ETL process is separated into its own module, making the project easier to extend, maintain, and test.

### Key Improvements

- Separate modules for:
  - Data Extraction
  - Data Transformation
  - Data Loading
  - Data Conversion
  - Utility functions
- Dedicated Airflow DAG
- Cleaner project structure
- Easier debugging and maintenance
- Supports multiple technology news categories

### Supported Categories

- Artificial Intelligence
- Cybersecurity
- Data Science
- Machine Learning
- Cloud Computing
- Software Development
- DevOps
- Other technology-related topics

### Workflow
```
                NewsAPI
                   │
                   ▼
          Apache Airflow DAG
                   │
                   ▼
           Extract Module
                   │
                   ▼
          Transform Module
                   │
                   ▼
            Combine Module
                   │
                   ▼
             Load Module
                   │
                   ▼
        Processed CSV/DataFrame
                   │
                   ▼
          Amazon S3 Bucket
```
---

# 🚀 Evolution from Version 1 to Version 2

| Feature           | Version 1 | Version 2 |
|-------------------|-----------|-----------|
| Project Structure | Basic | Modular |
| ETL Logic | Single File | Multiple Modules |
| Airflow DAG | Separate | Separate |
| News Categories | AI Only | Multiple Categories |
| Scalability | Basic | High |
| Code Reusability | Limited | High |
| Maintainability | Moderate | Excellent |
| Extensibility | Limited | Easy |

---

## 🛠️ Technologies Used

- Python
- Apache Airflow
- Pandas
- NewsAPI
- AWS EC2
- Amazon S3
- Boto3
- Git & GitHub
