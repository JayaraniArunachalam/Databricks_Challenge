# Databricks_Challenge
This repository documents my learning and hands-on implementation as part of the **Databricks 14 Days Challenge**, focused on understanding **Lakehouse architecture**, **Apache Spark**, and **Delta Lake** using Databricks Community Edition.

Databricks is a unified, open analytics platform for building, deploying, sharing, and maintaining enterprise-grade data, analytics, and AI solutions at scale. The Databricks Data Intelligence Platform integrates with cloud storage and security in the cloud account, and manages and deploys cloud infrastructure.

---

## 📌 Objective
- Understand why Databricks is used over Pandas and Hadoop for large-scale data processing
- Learn Lakehouse architecture fundamentals
- Learn Apache Spark fundamentals, Lazy Evaluation
- Magic Commands in Databricks
- Work with Databricks workspace, compute, and data organization
- Build scalable data pipelines using Spark and Delta Lake
- Follow Medallion Architecture (Bronze, Silver, Gold)

---

## 🛠️ Tools & Technologies
- Databricks Community Edition
- Apache Spark (PySpark)
- Delta Lake
- Cloud Object Storage (via Databricks Volumes)
- Python & SQL

---

## 📂 Dataset
**E-commerce Behavior Dataset**  
Source: Kaggle  
Contains user interaction events such as views, cart additions, and purchases.

---

## 🧱 Architecture Overview
This project follows **Lakehouse architecture**, where:
- Data is stored in cloud object storage (data lake)
- Delta Lake adds reliability and structure
- Data flows through Bronze → Silver → Gold layers

---

## 📅 Day-wise Progress

### ✅ Day 0 – Setup & Data Loading
- Created Databricks Community Edition account
- Configured Kaggle API credentials
- Created schema and volume in Databricks
- Downloaded and extracted dataset into Databricks Volume
- Loaded October and November 2019 data using Spark

### ✅ Day 1 – Platform Setup & First Steps
- Understood why Databricks vs Pandas/Hadoop
- Learned Lakehouse architecture basics
- Explored Databricks workspace structure
- Studied real-world use cases (Netflix, Shell, Comcast)
- Created first PySpark notebook
- Implemented reusable data loading function
- Ran basic Spark DataFrame operations

### ✅ Day 2 – Apache Spark Fundamentals
- Spark architecture (driver, executors, DAG)
- DataFrames vs RDDs
- Lazy evaluation
- Notebook magic commands (`%sql`, `%python`, `%fs`)

(Future days will be added progressively.)

---

## 📁 Repository Structure
```
Databricks_Challenge/
│
├── Key Notes/
│ ├── Points to remember.md
├── diagrams/
│ ├── apache spark component.png
│ ├── lazy evaluation.jpg
│ └── master worker paradigm.png
├── docs/
│ ├── Databricks platform setup and overview.md
│ └── Apache Spark Fundamentals IN DATABRICKS.pdf
├── scripts/
│ ├── load-data_from_csv.py
│ └── Day 2 Basic operations.ipynb
└── README.md
```

---

## 📘 Learning Notes & Key Takeaways

Along with daily learning folders, I maintain a living document
to capture my personal understanding and mental models.

👉 [Points to Remember – Key Learnings](https://github.com/JayaraniArunachalam/Databricks_Challenge/blob/main/Key%20Notes/Points%20to%20remember.md)

---

## 🚀 Next Steps
- Build Bronze Delta tables
- Implement Silver transformations
- Create Gold analytical views
- Automate pipelines using Databricks Jobs

---

📌 *This repository is continuously updated as part of the learning journey.*

