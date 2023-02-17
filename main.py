from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/contato')
def hello_world():
    return render_template('contato.html')


if __name__ == '__main__':
    app.run()