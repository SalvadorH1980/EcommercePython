
# invoco flask para ocupar metodos web
# invoco render_template para retornar htmls

from flask import Flask, render_template

app=Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/index')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

"""
Para llamar el codigo,
python index.py
"""

