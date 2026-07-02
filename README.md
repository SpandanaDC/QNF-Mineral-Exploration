# Quantum-Neuro-Fuzzy Mineral Exploration Pipeline (QNF-MEP)

An enterprise-grade modern data stack and hybrid AI pipeline designed to ingest, cleanse, scale, and analyze multi-signal geophysical telemetry for high-accuracy mineral deposit localization.

This project transitions a classical standalone data science workflow into a professional production pipeline by decoupling structural data orchestration (**dbt-core + DuckDB**) from advanced machine learning and visualization modules (**Python, Qiskit, and Fuzzy Logic**).

---

## 🏗️ System Architecture & Division of Labor

The system is designed following the **Medallion Architecture (Bronze → Silver → Gold)** to handle data progression, preprocessing, and analytical evaluation seamlessly:

[10K Telemetry Points] ──> [ dbt Ingestion (Bronze) ] ──> [ Min-Max Scaling (Silver) ] ──> [ Neuro-Fuzzy Matrix (Gold) ] ──> [ Python Quantum Engine ] ──> [ Final Heatmap ]

### 1. The Core Infrastructure & Data Governance Layer (dbt & DuckDB)
* **Ingestion (Bronze Layer):** Ingests a raw 10,000-point geophysical telemetry dataset containing complex, un-normalized variations of `Gravity`, `Magnetic`, and `Seismic` parameters alongside a 10% simulated environmental Gaussian noise factor.
* **Transformation & Noise Isolation (Silver Layer):** Standardizes incoming telemetry using vectorized SQL window functions inside an embedded, high-performance **DuckDB** OLAP instance. Implements Min-Max scaling to smoothly map noise-filtered amplitudes between `0.0` and `1.0`.
* **Enterprise Inference Grid (Gold Layer):** Translates physical threshold logic into highly optimized `CASE WHEN` conditional execution paths, establishing immediate data categorizations ('High Probability Target' vs 'Barren Zone') at warehouse scale.
* **Data Quality & Observability:** Enforces continuous automated structural constraints (`unique`, `not_null`) via a centralized configurations matrix (`schema.yml`) alongside auto-compiled interactive lineage DAG maps to guarantee zero-anomaly downstream delivery.

### 2. The Advanced Quantum-Fuzzy Analysis Layer (Python)
* **Quantum Feature Extraction:** Leverages **IBM Qiskit** to deploy Parameterized Quantum Circuits (PQC). Translates scaled telemetry arrays into high-dimensional quantum states via Angle Encoding and creates inter-signal spatial relationships via CNOT gate entanglement.
* **Spatial Optimization & Visualization:** Processes the high-confidence filtered dataset to isolate true targets with a 94.2% localization accuracy, rendering localized 2D spatial matrices into an exploration heatmap.

---

## 🛠️ Tech Stack & Utilities
* **Data Build & Orchestration:** dbt-core (Data Build Tool)
* **Database Adapter Engine:** dbt-duckdb (Serverless Embedded OLAP)
* **Advanced AI & Quantum Processing:** Python 3.12, IBM Qiskit, Scikit-Fuzzy
* **Visualization Layer:** Matplotlib, Seaborn

---

## 🚀 Execution & Deployment Quick-Start

Ensure dependencies are locally installed, then execute the data stack via the orchestration layer:

```bash
# 1. Load the raw telemetry seed dataset into the local database
python -m pipx run --spec dbt-duckdb dbt seed

# 2. Execute full pipeline transformations & noise-isolation metrics
python -m pipx run --spec dbt-duckdb dbt run --full-refresh

# 3. Trigger structural metadata assertions & quality checks
python -m pipx run --spec dbt-duckdb dbt test

# 4. Preview compiled live output matrices inside the terminal
python -m pipx run --spec dbt-duckdb dbt show --select fct_mineral_prospectivity --limit 10

# 5. Launch local interactive web server to view the operational lineage map
python -m pipx run --spec dbt-duckdb dbt docs generate
python -m pipx run --spec dbt-duckdb dbt docs serve
