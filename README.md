# 📈 Stock Price Pipeline (Mock Project)

A simple data engineering pipeline that extracts stock price data (SET, Nasdaq), transforms it using Python, and loads it into BigQuery for analysis and visualization.

---

## 🔧 Tools & Tech Stack

- 🐍 Python (Requests, Pandas)
- ☁️ Google BigQuery
- ⏱ Airflow (หรือ Crontab สำหรับ schedule)
- 📊 Power BI / Looker Studio (Dashboard)
- 🔄 dbt (Optional)

---

## 🔄 ETL Pipeline Flow

```mermaid
graph LR
A[Extract from API] --> B[Transform with Pandas]
B --> C[Load to BigQuery]
C --> D[Dashboard Visualization]
