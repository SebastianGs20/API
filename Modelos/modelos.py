from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Cancion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(128))
    minutos = db.Column(db.Integer)
    segundos = db.Column(db.Integer)
    interprete = db.Column(db.String(128))


class Album(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(128))
    ano = db.Column(db.Integer)
    descripcion = db.Column(db.String(128))
    medio = db.Column(db.Medio)


class Usuario(db.Model):
    id = db.Column (db.Integer, primary_key=True)
    nombre_usuario = db.Column(db.String(128))
    Contraseña = db.Column(db.String(128))


class Medio (db.Model):
    DISCO = db.Column(db.String(128))
    CASETE = db.Column(db.String(128))
    CD = db.Column(db.String(128))
