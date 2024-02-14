from flask import Flask, render_template
from werkzeug.urls import url_quote


app = Flask(__name__)

# Sample player data
players = [
    {
        'name': 'Raman',
        'country': 'India',
        'role': 'Batsman',
        'image': 'C:\Users\dell\cricket-players\Raman.jfif',
        'history': 'One of the best batsmen in the world.'
    },
    {
        'name': 'Kannan',
        'country': 'Australia',
        'role': 'Batsman',
        'image': 'C:\Users\dell\cricket-players\prem.jfif',
        'history': 'Known for his unorthodox batting style.'
    },
    # Add more player data as needed
]

@app.route('/')
def index():
    return render_template('index.html', players=players)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=5000)
