# Enterprise Financial Intelligence Engine

**Stateful Multi-Agent Analytics over Databricks & Snowflake**

A production-style system that ingests unstructured corporate financial data (PDFs, CSVs) at scale, processes it through a PySpark/Databricks pipeline into Snowflake, and exposes it to a team of cooperative LangGraph AI agents that can query data warehouses, run code in secure sandboxes, and compile business reports — with self-correcting SQL generation and RAG-based context retrieval.

---

## 🏗️ Architecture

<img width="989" height="328" alt="image" src="https://github.com/user-attachments/assets/4450754e-4b6d-42f6-938f-8ab1e108213a" />

**Flow summary:**
1. Raw financial ledgers and vendor documents land in Databricks.
2. PySpark cleans, normalizes, and chunks the data.
3. Structured data is written to Snowflake (SCD Type 1/2); unstructured text is embedded and indexed for semantic search.
4. A LangGraph supervisor routes each user query to the right agent(s).
5. The SQL agent queries Snowflake; a validator sandbox checks the result and loops back on error.
6. The report agent compiles a narrative with citations pulled from the RAG store.

---

## 🧰 Tech Stack

| Layer | Tools |
|---|---|
| Data Engineering | PySpark, Databricks Workflows |
| Storage / Warehouse | Snowflake (SCD Type 1 & 2), Microsoft Fabric |
| Vector Search | Snowflake Cortex Search / Databricks Vector Search |
| Orchestration | LangGraph, LangChain |
| Execution | Python sandbox (Pandas, Matplotlib) |
| Observability | LangSmith |

---

## 🤖 Agent Roles

- **Database Specialist** — reads schema metadata, writes and executes SQL against Snowflake.
- **Data Validator / Execution Sandbox** — validates the returned dataframe; on error, sends a diagnostic traceback back to the Database Specialist to self-correct.
- **Report Generator & Visualizer** — builds charts and a final narrative summary with citations from the RAG store.

---

## 📁 Repo Structure

```
├── notebooks/       # Databricks / PySpark notebooks
├── src/             # LangGraph agents, tools, state definitions
├── docs/            # Architecture notes, schema docs
└── README.md
```

---
