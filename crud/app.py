from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from config import Config
from datetime import datetime

# Initialization
app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

# Models
class Informasi(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    judul = db.Column(db.String(100), nullable=False)
    isi = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

# Migrations
with app.app_context():
    db.create_all()

# Controllers
def index():
    informasis = Informasi.query.all()
    return render_template('index.html', informasis=informasis)

def create():
    if request.method == 'POST':
        judul = request.form['judul']
        isi = request.form['isi']
        new_informasi = Informasi(judul=judul, isi=isi)
        try:
            db.session.add(new_informasi)
            db.session.commit()
            return redirect(url_for('index'))
        except:
            return 'There was an issue adding your information'
    else:
        return render_template('create.html')

def show(informasi_id):
    informasi = Informasi.query.get_or_404(informasi_id)
    return render_template('show.html', informasi=informasi)

def edit(informasi_id):
    informasi = Informasi.query.get_or_404(informasi_id)
    if request.method == 'POST':
        informasi.judul = request.form['judul']
        informasi.isi = request.form['isi']
        try:
            db.session.commit()
            return redirect(url_for('index'))
        except:
            return 'There was an issue updating your information'
    else:
        return render_template('edit.html', informasi=informasi)

def delete(informasi_id):
    informasi = Informasi.query.get_or_404(informasi_id)
    try:
        db.session.delete(informasi)
        db.session.commit()
        return redirect(url_for('index'))
    except:
        return 'There was a problem deleting that information'

# Routes
def register_routes(app: Flask):
    app.add_url_rule('/', view_func=index, methods=['GET'])
    app.add_url_rule('/create', view_func=create, methods=['GET', 'POST'])
    app.add_url_rule('/show/<int:informasi_id>', view_func=show, methods=['GET'])
    app.add_url_rule('/edit/<int:informasi_id>', view_func=edit, methods=['GET', 'POST'])
    app.add_url_rule('/delete/<int:informasi_id>', view_func=delete, methods=['POST'])

register_routes(app)

if __name__ == "__main__":
    app.run(debug=True)