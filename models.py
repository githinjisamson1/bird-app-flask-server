# models.py

from config import db
from sqlalchemy_serializer import SerializerMixin


class Bird(db.Model, SerializerMixin):
    __tablename__ = 'birds'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    species = db.Column(db.String)

    def __repr__(self):
        return f'<Bird {self.name} | Species: {self.species}>'
