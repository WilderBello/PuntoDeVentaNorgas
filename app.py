from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', methods=('GET','POST'))
def login():
    return render_template('index.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/search')
def search():
    return render_template('search.html')

@app.route('/create')
def create():
    return render_template('create.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)