from flask import Flask, render_template, request, redirect, url_for
from database import load_jobs_from_db, load_job_from_db, add_application_to_db, add_signup_to_db

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

@app.route('/getupdates', methods=['GET', 'POST'])
def get_updates():
    if request.method == 'POST':
        # Capture the form data
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        
        # Call the function to save the data to the database
        add_signup_to_db(first_name, last_name, email)
        
        # Redirect to the "Signed Up" page after successful submission
        return redirect(url_for('signedup'))

    return render_template('getupdates.html')


# Signed Up Page

@app.route('/signedup')
def signedup():
    return render_template('signedup.html')   


# Job Description Page

@app.route('/job/<id>')
def show_job(id):
    job = load_job_from_db(id)
    
    if not job:
        return "Not Found!", 404
    return render_template('jobpage.html', job=job)


# Application Form Page

@app.route('/job/<id>/apply', methods=['GET', 'POST'])
def apply_to_job(id):
    job = load_job_from_db(id)
    if not job:
        return "Job not found", 404

    if request.method == 'POST':
        data = request.form
        add_application_to_db(id, data)
        return render_template('application_submitted.html', application=data, job=job)

    return render_template('application_form.html', job=job)
    
    
if __name__ == "__main__":
    app.run(debug = False)