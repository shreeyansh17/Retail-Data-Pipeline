import logging
from extract import extract_data
from transform import transform_data
from load import load_data

logging.basicConfig(
    filename='../logs/pipeline.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

try:
    logging.info("Pipeline started")

    df = extract_data()

    if df.empty:
        raise Exception("No data found!")

    df = transform_data(df)

    load_data(df)

    logging.info("Pipeline completed successfully")

    print("Pipeline ran successfully 🚀")

except Exception as e:
    logging.error(f"Error: {e}")
    print("Error occurred:", e)