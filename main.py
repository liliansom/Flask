from flask import Flask, render_template, url_for
from forms import FormLogin


app = Flask(__name__, static_folder='static' )
app.config['SECRET_KEY'] = 'e7d749e499af22c81881782c5e957bf0'

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/contato')
def contato():
    return render_template('contato.html')

@app.route('/repositorio')
def repositorio():
    return render_template('repositorio.html')

if __name__ == '__main__':
    app.run(debug=True)
    