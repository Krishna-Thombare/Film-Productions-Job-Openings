from flask import Flask, render_template, jsonify, request
from database import load_jobs_from_db, load_job_from_db, add_application_to_db

app = Flask(__name__)

# Home Page
@app.route('/')
def home():
    jobs = load_jobs_from_db()
    return render_template('index.html', jobs=jobs)

# About Us Page
@app.route('/aboutus')
def about_us():
    return render_template('aboutus.html')

# Get Update Page
@app.route('/getupdates')
def get_updates():
    return render_template('getupdates.html')
    
# To store jobs information in json format
@app.route('/api/jobs')       #api route
def list_jobs():
    jobs = load_jobs_from_db()
    return jsonify(jobs)

# Job Description Page
@app.route('/job/<id>')
def show_job(id):
    job = load_job_from_db(id)
    
    if not job:
        return "Not Found!", 404
    return render_template('jobpage.html', job=job)

# Application Submitted Page
@app.route('/job/<id>/apply', methods=['POST'])
def apply_to_job(id):
    data = request.form
    job = load_job_from_db(id)
    
    add_application_to_db(id, data)
    
    return render_template('application_submitted.html', application=data, job=job)
    

if __name__ == "__main__":
    app.run(debug = True)