# stock-price-pipeline
A mock ETL project that extracts Thai Government Lottery results from a website, transforms the data with Python, and loads it into BigQuery. Dashboard built with Power BI.

## 🔧 Tools Used
- Python (Requests, BeautifulSoup, Pandas)
- Google BigQuery
- dbt (optional)
- Power BI

## 🔄 ETL Pipeline
1. **Extract**: Scrape latest lottery results from website
2. **Transform**: Clean and format into structured table
3. **Load**: Upload to BigQuery via API
4. **Visualize**: Build Dashboard on Power BI

## 📊 Output Example
![dashboard](dashboard/screenshot.png)

## 🧠 What I Learned
- How to work with BigQuery API
- Practice scheduling ETL job
- Data cleaning using Pandas
