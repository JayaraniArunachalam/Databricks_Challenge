# Databricks platform setup and overview

## 🎯 Objective
The goal of Day 0 is to set the foundation for learning Databricks and Apache Spark by understanding **why Databricks is needed**, how it fits into the modern data ecosystem, and what this learning challenge aims to achieve.

---

## ❓ Why Databricks?

Traditional data processing tools struggle when:
- Data volume grows rapidly
- Multiple teams (data engineers, analysts, ML engineers) work together
- Real-time or large-scale analytics is required

Databricks was created to solve these problems by providing:
- A **unified analytics platform**
- Built on top of **Apache Spark**
- Fully managed on the cloud

---

## 🧠 What is Databricks?

Databricks is a **cloud-based data analytics platform** that allows users to:
- Ingest and store large volumes of data
- Process data using Apache Spark
- Perform analytics, BI, and machine learning in one place

It acts as a **managed layer** over cloud providers like AWS, Azure, or GCP.

---

## 🏗️ High-Level Architecture

Databricks works on top of cloud infrastructure and abstracts away:
- Cluster setup
- Resource management
- Spark configuration

This allows users to focus on **data and logic**, not infrastructure.

---

## 🚀 Learning Approach

This challenge is designed to:
- Learn concepts step-by-step
- Combine theory with hands-on practice
- Build a GitHub repository as learning evidence
- Improve architectural and interview-level understanding

---

## How Databricks differs from traditional Hadoop/ Pandas

Databricks is:
- A **data processing and analytics platform**
- Built on **Apache Spark**
- Designed to work with cloud storage (Data Lake)

---

## 🧱 Key Concepts Learned

### 1️⃣ Cloud vs Server
- A **server** is a physical or virtual machine
- The **cloud** is a collection of servers hosted in data centers
- Cloud providers own and manage the servers
- Users rent compute and storage as needed

👉 Databricks runs Spark clusters on **cloud servers**

---

### 2️⃣ Hadoop vs Databricks (High Level)

| Aspect | Hadoop | Databricks |
|------|--------|-----------|
| Processing | Disk-based | In-memory (Spark) |
| Speed | Slower | Faster |
| Setup | Complex | Fully managed |
| Cloud-native | No | Yes |

Databricks replaces Hadoop’s complexity with **cloud-native Spark execution**.

---

### 3️⃣ Distributed File System (Concept)

In Hadoop:
- Data is stored across multiple machines (HDFS)
- Files appear as one logical unit to the user

In Databricks:
- Data is stored in **cloud object storage**
- Spark processes data in parallel across nodes

---

### 4️⃣ Who Uses Databricks?

Databricks is used by:
- **Data Engineers** – ingestion, transformation, pipelines
- **Data Analysts** – analytics and reporting
- **Data Scientists** – machine learning and experimentation

All users work on the **same platform**.

---

### 5️⃣ Databricks + Analytics Tools

Databricks can connect with:
- Power BI
- Tableau
- Other BI tools

Spark processes the data, and BI tools consume the results.

---

## 🛠️ Hands-On Exposure

- Explored Databricks workspace
- Understood notebooks and clusters
- Learned how Databricks abstracts Spark complexity

---

## 📌 Key Takeaways

- Databricks is a **unified analytics platform**
- Spark is the **processing engine**
- Cloud provides the **infrastructure**
- Users focus on **data, not servers**

---

