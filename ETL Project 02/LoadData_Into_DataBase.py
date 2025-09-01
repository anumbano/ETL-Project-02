import pandas as pd
from sqlalchemy import create_engine
from urllib.parse import quote_plus  # to encode special characters

user = "root"
password = quote_plus("Anum@1234")   # safely encode
host = "localhost"
port = 3306
database = "mini_etl_project"

# Connection string
engine = create_engine(f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}")

# Read CSV_file
df = pd.read_csv(r"C:\Users\PMLS\Documents\D.E PROJECT\ETL Project 01\Cleaned_Product-Sales-Region_Data.csv")

# Fix column names
df.columns = [col.replace(" ", "_").replace("-", "_") for col in df.columns]

# Write to MySQL
df.to_sql("Cleaned_DataSet", con=engine, if_exists="replace", index=False)

print("Data successfully loaded into MySQL!")

