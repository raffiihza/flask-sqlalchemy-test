from flask import render_template, request, redirect, url_for, flash
from models import Informasi, db

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
