# 🏥 Healing the Hospital Ledger: An End-to-End Azure Data Engineering Symphony

This project orchestrates a sophisticated data ecosystem designed to solve a critical challenge in the healthcare industry: **Revenue Cycle Management (RCM)**. By focusing on **Accounts Receivable (AR)**, this pipeline ensures that healthcare providers remain financially healthy while delivering quality care by optimizing how they collect payments from patients and insurance companies.

---

## 🌟 The Vision
In the complex world of healthcare, hospitals must manage a "Financial Lifeline" that starts the moment a patient schedules an appointment and ends when the provider is finally paid. This project simulates a real-world scenario where a hospital group (Hospitals A and B) must merge disparate data systems into a unified **Common Data Model (CDM)** to track every dollar across its journey.

## 🛠️ The Specialized Tech Stack
The solution is built on the **Azure Data Engineering Stack**, utilizing industry-leading tools to ensure scalability and security.

*   **Azure Data Factory (ADF):** The heart of the system, orchestrating **metadata-driven pipelines** and ingesting data from SQL databases and flat files.
*   **Azure Databricks:** The engine for transformation, where raw data is refined using **Spark** and organized into **Delta Tables**.
*   **ADLS Gen2:** The centralized repository, employing a **hierarchical namespace** to manage massive datasets efficiently.
*   **Azure Key Vault:** The high-security vault protecting sensitive credentials, connection strings, and access tokens.
*   **Unity Catalog:** The governance layer providing a centralized metadata repository across the entire Databricks workspace.

## 🧬 The Data Anatomy
To build a complete financial picture, the pipeline ingests and enriches data from four diverse sources:
1.  **Electronic Medical Records (EMR):** Critical patient, provider, department, and transaction data stored in **Azure SQL Databases**.
2.  **Claims Data:** Detailed insurance billing records provided as **CSV flat files** in the Landing Zone.
3.  **NPI Data:** National Provider Identifier details retrieved via **Public APIs** to uniquely identify every doctor.
4.  **Medical Codes (ICD & CPT):** Standardized codes used to classify diagnoses and procedures, mapped via APIs to ensure billing accuracy.

## 🏗️ The Architecture: Medallion Pattern
The data follows a rigorous "refinement" process, moving through layers to increase quality and usability.

*   **Landing Zone:** The entry point for raw insurance files.
*   **Bronze (Raw):** Ingested data from all sources preserved in its original form as **Parquet files**.
*   **Silver (Cleaned & Enriched):** The layer where data is standardized into a **Common Data Model**, bad data is **quarantined**, and historical changes are tracked using **SCD Type 2**.
*   **Gold (Curated):** The final destination, featuring optimized **Fact and Dimension tables** structured for high-performance business intelligence.

## 🚀 Key Engineering Highlights
*   **Metadata-Driven Scalability:** Rather than building individual pipelines for every table, a single **generic pipeline** reads configurations from a `load_config.csv` to dynamically handle multiple hospital branches.
*   **Parallel Processing:** Optimized for speed, the pipeline processes multiple data streams concurrently, moving away from slow sequential loads.
*   **Audit & Intelligence:** A custom `load_logs` table tracks the **Watermark** for every table, enabling intelligent **incremental loading** so only new or modified data is processed.
*   **Industrial Best Practices:** Implements **retries**, secure **secret scopes**, and **Unity Catalog** to mirror professional enterprise standards.

## 📈 Vital Signs: RCM Insights
The ultimate goal of this pipeline is to empower the reporting team to calculate critical financial KPIs:
*   **AR > 90 Days:** Identifying high-risk revenue that has been pending for over three months.
*   **Days in AR:** Measuring the average time it takes to convert a medical service into cash.
*   **Net Collection Rate:** Monitoring the percentage of billed amount actually collected to ensure zero revenue leakage.

---
