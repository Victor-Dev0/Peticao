from flask import Flask, render_template, request, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'peticaoMilitao'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///peticao.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


#Modelo da resposta do usuario
class Peticao(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), nullable=False)
    resposta = db.Column(db.String(50), nullable=False)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        nome = request.form['nome']
        resposta = request.form['resposta'].lower()

        if resposta == 'sim':
            nova_pessoa = Peticao(nome=nome, resposta=resposta)
            db.session.add(nova_pessoa)
            db.session.commit()
            flash('Obrigado por participar!', 'success')
        elif resposta == 'não':
                nova_pessoa = Peticao(nome=nome, resposta=resposta)
                db.session.add(nova_pessoa)
                db.session.commit()
                flash('Obrigado por participar!', 'success')
        elif resposta == 'nao':
            nova_pessoa = Peticao(nome=nome, resposta=resposta)
            db.session.add(nova_pessoa)
            db.session.commit()
            flash('Obrigado por participar!', 'success')
            
        else:
            flash('Resposta inválida, somente o que está entre parenteses!', 'error')

    return render_template('home.html')


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)