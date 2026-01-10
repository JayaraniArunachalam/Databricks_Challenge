# Points to remember
This points to remember is to document my personal key takeaways, important concepts, points, and key notes that I understood during this Databricks Journey.

---

Databricks is a cloud native platform. Databricks is a unified, open analytics platform for building, deploying, sharing, and maintaining enterprise-grade data, analytics, and AI solutions at scale. 
The Databricks Data Intelligence Platform integrates with cloud storage and security in the cloud account, and manages and deploys cloud infrastructure.

## Cloud, Servers, and Clusters

- Cloud providers own physical servers in data centers
- A Databricks cluster is a group of cloud servers running Spark
- I don’t manage servers directly; Databricks abstracts it.

Data processing in Databricks is better than python's pandas library and Hadoop for data processing in terms of scalability and complexity. 
Because it can process large volume of data compared to Pandas and ease to use compared to Hadoop.

- Databricks runs on major cloud service providers like Azure, AWS, Google Cloud Platform.
- Looking at the interface of the Databricks. It has workspace, catalog.
- Schema can be created in workspaces to store tables.
- Volumes can be created in schemas, whereas raw files are held under volumes

Databricks uses Apache Spark Engine as its processing Engine which enables fast and in memory data processing.

---
## Datbricks lakehouse  Architecture

The Databricks Lakehouse is a modern data architecture that combines the best features of Data Warehouses (performance and reliability) with Data Lakes (low cost and flexibility).
In a traditional setup, you had to move data from a Data Lake to a Data Warehouse to do analytics. The Lakehouse eliminates this "double hop" by allowing you to run your BI, SQL, 
and Machine Learning directly on your cloud storage.

**1. The Three Layers of a Lakehouse**
     The architecture is logically organized into three layers, often called the Medallion Architecture.
   
   **Bronze (Raw Zone)**
       - Source: Ingests raw data from APIs, IoT sensors, or CSVs/JSONs.
       - State: Data is kept in its original format. It is often messy and contains duplicates.
       - Purpose: To have a historical record of exactly what was received.
   
   **Silver (Filtered/Cleaned Zone)**
       - Process: Data is cleaned, filtered, and joined.
       - State: We apply a Schema here. Null values are handled, and data types are corrected (e.g., converting a string date to a proper date format).
       - Purpose: Provides a "Single Source of Truth" for data scientists and engineers.
   
   **Gold (Business Ready)**
       - Process: Aggregated data (e.g., "Daily Sales Summary" or "Monthly Profit").
       - State: Highly optimized tables, often small and very fast to query.
       - Purpose: Powering Dashboards, BI tools (like Power BI or Tableau), and final reports.
   
**2. The "Secret Sauce": Delta Lake**
   The Lakehouse exists because of Delta Lake. Delta Lake is an open-source storage layer that sits on top of your files (Parquet) and adds critical features
   - ACID Transactions: Ensures that if a job fails halfway through, the data isn't left "corrupted." It either finishes completely or not at all.
   - Time Travel: You can query an older version of your data (e.g., "Show me what this table looked like last Tuesday").
   - Schema Enforcement: Prevents "bad data" from entering your clean tables by blocking rows that don't match your defined structure.
     
**3. Unity Catalog (The Governance Layer)**
   This is the "Security Guard" of the Lakehouse.
   -It manages permissions across all your Catalogs, Schemas, and Volumes.
   -It provides Lineage, showing you exactly which Bronze table was used to create which Gold table.

**4. Why Use Lakehouse?**
   | Feature | Old Way (Lake + Warehouse) | New Way (Databricks Lakehouse) |
   |------|--------|-----------|
   | Data Movement | Constant moving of data (ETL).| Data stays in your Cloud Storage. |
   | Data Types | Hard to do ML on Data Warehouses. | ML and SQL run on the same data. |
   | Cost | Expensive proprietary storage. | Low-cost storage (S3/ADLS). |
   | Speed | Slow "Batch" updates. | Real-time streaming and batch combined. |

---

## Spark Architecture (Runtime)

- Driver, Executors, and DAG are **created at runtime**
- They are **not functions or methods**
- Driver plans and coordinates
- Executors execute tasks in parallel
  
![](https://github.com/JayaraniArunachalam/Databricks_Challenge/blob/main/diagrams/apache%20spark%20component.png)
---

## DAG & Lazy Evaluation

- Spark does not execute transformations immediately
- It builds a DAG (logical plan)
- Execution happens only when an **action** is called
- Errors can appear late due to lazy evaluation
  
![lazy evaluation](https://github.com/JayaraniArunachalam/Databricks_Challenge/blob/main/diagrams/lazy%20evaluation.jpg)


---

## DataFrames vs RDDs

- DataFrames are high-level and optimized
- Catalyst and Tungsten make DataFrames fast
- RDDs give low-level control but are rarely needed
- Default choice should always be DataFrames


