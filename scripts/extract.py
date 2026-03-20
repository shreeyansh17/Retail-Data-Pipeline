import pandas as pd
from sqlalchemy import create_engine

def extract_data():
    # SQLAlchemy engine
    engine = create_engine(
        "mssql+pyodbc://LAPTOP-E7JAAPS0\\SQLEXPRESS/RetailDB?driver=SQL+Server"
    )

    query = "SELECT * FROM sales_data"
    df = pd.read_sql(query, engine)

    return df