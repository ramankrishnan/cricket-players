from flask import Flask, render_template
from werkzeug.urls import url_quote


app = Flask(__name__)

# Sample player data
players = [
    {
        'name': 'Virat Kohli',
        'country': 'India',
        'role': 'Batsman',
        'image': 'virat_kohli.jpg',
        'history': 'One of the best batsmen in the world.'
    },
    {
        'name': 'Steve Smith',
        'country': 'Australia',
        'role': 'Batsman',
        'image': 'steve_smith.jpg',
        'history': 'Known for his unorthodox batting style.'
    },
    # Add more player data as needed
]

@app.route('/')
def index():
    return render_template('index.html', players=players)

if __name__ == '__main__':
    app.run(debug=True)
