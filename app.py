from flask import Flask, render_template, jsonify

app = Flask(__name__)

# List to store jobs information
JOBS = [
    {
        'id': 1,
        'title': 'Cinematographer',
        'location': 'Pune, India',
        'salary': 'Rs. 70,000'
    },
    
    {
        'id': 2,
        'title': 'Director',
        'location': 'Pune, India',
        'salary': 'Rs. 100,000'
    },
    
    {
        'id': 3,
        'title': 'Writer',
        'location': 'Pune, India',
        'salary': 'Rs. 85,000'
    },
    
    {
        'id': 4,
        'title': 'Editor',
        'location': 'Pune, India',
        'salary': 'Rs. 70,000'
    }
]

@app.route('/')
def home():
    return render_template('index.html', jobs=JOBS, company_name='FINISHER')

# To store jobs information in json format
@app.route('/api/jobs')       #api route
def list_jobs():
    return jsonify(JOBS)



if __name__ == "__main__":
    app.run(debug = True)