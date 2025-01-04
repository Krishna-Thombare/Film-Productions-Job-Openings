from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path='.env')
db_connection_string = os.environ['DB_CONNECTION_STR']

engine = create_engine(db_connection_string)

# Job Listing on Home Page - Table 1

def load_jobs_from_db():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM jobs")) 
        
        # Created list of dictionaries
        jobs = [dict(row._mapping) for row in result]
        return jobs
    
    
# Job Description Data - Table 1

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
        

# Application Form Data - Table 2 

def add_application_to_db(job_id, data):
    with engine.connect() as conn:
        query = text(
            "INSERT INTO applications ("
            "job_id, full_name, email, contact_no, address, portfolio_link, work_experience"
            ") VALUES ("
            ":job_id, :full_name, :email, :contact_no, :address, :portfolio_link, :work_experience"
            ")"
        )

        params = {
                'job_id': job_id,
                'full_name': data['full_name'],
                'email': data['email'],
                'contact_no': data['contact_no'],
                'address': data['address'],
                'portfolio_link': data['portfolio_link'],
                'work_experience': data['work_experience']
        }

        # Execute query and commit
        conn.execute(query, params)
        conn.commit()  # Commit the transaction
        

# Get Updates - Table 3

def add_signup_to_db(first_name, last_name, email):
    with engine.connect() as conn:
        query = text(
            "INSERT INTO get_updates (first_name, last_name, email) "
            "VALUES (:first_name, :last_name, :email)"
        )

        params = {
            'first_name': first_name,
            'last_name': last_name,
            'email': email
        }

        # Execute the query to insert the data
        conn.execute(query, params)
        conn.commit()  # Commit the transaction
    
