from flask import Flask, render_template, jsonify
from database import load_jobs_from_db

app = Flask(__name__)

@app.route('/')
def home():
    jobs = load_jobs_from_db()
    return render_template('index.html', jobs=jobs)

# To store jobs information in json format
@app.route('/api/jobs')       #api route
def list_jobs():
    jobs = load_jobs_from_db()
    return jsonify(jobs)



if __name__ == "__main__":
    app.run(debug = True)