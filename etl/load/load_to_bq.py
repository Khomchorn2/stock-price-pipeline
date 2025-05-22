# load_to_bq.py
from google.cloud import bigquery
import pandas as pd

def load_to_bigquery(csv_file, dataset_id, table_id, project_id):
    client = bigquery.Client(project=project_id)
    df = pd.read_csv(csv_file)

    job_config = bigquery.LoadJobConfig(
        write_disposition="WRITE_TRUNCATE",
        autodetect=True,
        source_format=bigquery.SourceFormat.CSV,
        skip_leading_rows=1,
    )

    with open(csv_file, "rb") as source_file:
        job = client.load_table_from_file(
            source_file,
            f"{project_id}.{dataset_id}.{table_id}",
            job_config=job_config
        )

    job.result()
    print("✅ Loaded to BigQuery")

# Example use
# load_to_bigquery("stock_data.csv", "my_dataset", "stock_prices", "my_project")
