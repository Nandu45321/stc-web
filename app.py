from flask import Flask, render_template

app = Flask(__name__)

# Mock data for demonstration
clubs = [
    {"name": "Coding Club", "description": "Programming and development club"},
    {"name": "CMIT", "description": "Mathematics and computing club"},
    {"name": "Parsec Club", "description": "Astronomy and astrophysics club"},
    {"name": "PSIT", "description": "Physics society"},
]

events = [
    {"title": "Tech Symposium", "date": "2023-08-15"},
    {"title": "Hackathon", "date": "2023-09-10"},
]

@app.route('/')
def index():
    return render_template('index.html', events=events[:3])

@app.route('/clubs')
def clubs_page():
    return render_template('clubs.html', clubs=clubs)

@app.route('/events')
def events_page():
    return render_template('events.html', events=events)

@app.route('/admin')
def admin():
    return render_template('admin.html')

if __name__ == '__main__':
    app.run(debug=True)