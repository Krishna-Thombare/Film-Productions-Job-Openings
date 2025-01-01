from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import os

# To hide DB info
load_dotenv(dotenv_path='secret.env')
db_connection_string = os.environ['DB_CONNECTION_STR']

engine = create_engine(db_connection_string)

def load_jobs_from_db():
    with engine.connect() as conn:
        result = conn.execute(text("select * from jobs")) 
        
        # Created list of dictionaries
        jobs = [dict(row._mapping) for row in result]
        print(jobs)
        return jobs

