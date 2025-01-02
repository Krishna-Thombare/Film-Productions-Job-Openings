from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import os

# To hide DB info
load_dotenv(dotenv_path='.env')
db_connection_string = os.environ['DB_CONNECTION_STR']

engine = create_engine(db_connection_string)

def load_jobs_from_db():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM jobs")) 
        
        # Created list of dictionaries
        jobs = [dict(row._mapping) for row in result]
        print(jobs)
        return jobs

def load_job_from_db(id):
    with engine.connect() as conn:
        result = conn.execute(
                text("SELECT * FROM jobs WHERE id = :val "),
                {"val" : id}
        )

        rows = result.all()
        if len(rows) == 0: 
            return None
        else:
            return dict(rows[0]._mapping)