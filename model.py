from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Pets(db.Model):
    """Pet Model"""
    __tablename__ = "Pets"
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    name = db.Column(db.Sting(50), nullable = False)
    species = db.Column(db.String(200), nullable = False)
    photo_url = db.Column(db.String, nullable = True)
    age = db.Column(db.Integer, nullable = True)
    notes = db.Column(db.String, nullable = True)
    available = db.Column(db.Boolean, nullable = False, default = True)