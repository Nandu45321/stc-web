from flask import Flask, render_template
import os
import psycopg2
app = Flask(__name__)

# Database configuration
app.config['DATABASE'] = os.environ.get('POSTGRES_DB', 'stc_db')
app.config['DB_USER'] = os.environ.get('POSTGRES_USER', 'stc_user')
app.config['DB_PASSWORD'] = os.environ.get('POSTGRES_PASSWORD', 'stc_password')
app.config['DB_HOST'] = os.environ.get('DB_HOST', 'db')

def get_db_connection():
    conn = psycopg2.connect(
        database=app.config['DATABASE'],
        user=app.config['DB_USER'],
        password=app.config['DB_PASSWORD'],
        host=app.config['DB_HOST']
    )
    return conn


pathToClubsImages = "/images/clubs/"  # Do not add static to this path, it's already included by the clubs.html file
# Mock data for demonstration
clubs = [
    {"name": "Coding Club", "description": "Programming and development club", "image": pathToClubsImages + "coding_club.png"},
    {"name": "CMIT", "description": "Mathematics and computing club", "image": pathToClubsImages + "cmit.png"},
    {"name": "Parsec Club", "description": "Astronomy and astrophysics club", "image": pathToClubsImages + "parsec.png"},
    {"name": "PSIT", "description": "Physics society", "image": pathToClubsImages + "psit.png"},
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