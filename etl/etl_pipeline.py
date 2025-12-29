import pandas as pd
import sqlite3
import time

start_time = time.time()

# extract
df = pd.read_csv('data/raw_data.csv')

# transform
df = df.dropna()
df = df.drop_duplicates()

# load
conn = sqlite3.connect('db/pipeline.db')
df.to_sql('clean_data', conn, if_exists='replace', index=False)
conn.close()

end_time = time.time()

print("Records processed:", len(df))
print("Time taken:", round(end_time - start_time, 2), "seconds")


import logging
logging.basicConfig(
    filename='logs/etl.log',
    level=logging.INFO,
    format='%(asctime)s - %(message)s'
)
logging.info(f"Records processed: {len(df)}")
logging.info(f"Time taken: {round(end_time - start_time, 2)} seconds")
