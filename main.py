from flask import Flask, render_template, url_for

# Criação da página Flask
app = Flask(__name__, static_folder='static' )
app.config['SECRET_KEY'] = 'e7d749e499af22c81881782c5e957bf0'

# Criação da página homepage  
@app.route('/')
def home():
    return render_template('home.html')

# Criação da página contato 
@app.route('/contato')
def contato():
    return render_template('contato.html')

# Criação da página respositório
@app.route('/repositorio')
def repositorio():
    return render_template('repositorio.html')

# Para rodar a página
if __name__ == '__main__':
    app.run(debug=True)
    