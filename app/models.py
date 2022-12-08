from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash

db = SQLAlchemy()


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username =  db.Column(db.String(200), nullable=False, unique=True)
    email = db.Column(db.String(250), nullable=False, unique=True)
    password =  db.Column(db.String(300), nullable=False)
    post = db.relationship('Pokedex', backref='Discoverer', lazy = True)

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = generate_password_hash(password)

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
        

class Pokedex(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    entry = db.Column(db.String(50), nullable=False, unique=True)
    img_url = db.Column(db.String(), nullable=False, unique=True)
    ability = db.Column(db.String(50), nullable=False)
    hp = db.Column(db.String(50), nullable=False)
    attack = db.Column(db.String(50), nullable=False)
    defense = db.Column(db.String(50), nullable=False)
    special_attack = db.Column(db.String(50), nullable=False)
    special_defense = db.Column(db.String(50), nullable=False)
    speed = db.Column(db.String(50), nullable=False)
    date_created = db.Column(db.DateTime, nullable = False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __init__(self, entry, img_url, ability, hp, attack, defense, special_attack, special_defense, speed, user_id):
        self.entry = entry
        self.img_url = img_url
        self.ability = ability
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.special_attack = special_attack
        self.special_defense = special_defense
        self.speed = speed
        self.user_id = user_id

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def  delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

        
