from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username =  db.Column(db.String(50), nullable=False, unique=True)
    email = db.Column(db.String(50), nullable=False, unique=True)
    password =  db.Column(db.String(50), nullable=False)
    post = db.relationship('Pokedex', backref='Discoverer', lazy = True)

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password
        

class Pokedex(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    img_url = db.Column(db.String(), nullable=False, unique=True)
    type = db.Column(db.String(50), nullable=False )
    ability = db.Column(db.String(50), nullable=False)
    hp = db.Column(db.String(50), nullable=False)
    attack = db.Column(db.String(50), nullable=False)
    defense = db.Column(db.String(50), nullable=False)
    special_attack = db.Column(db.String(50), nullable=False)
    special_defense = db.Column(db.String(50), nullable=False)
    speed = db.Column(db.String(50), nullable=False)
    date_created = db.Column(db.DateTime, nullable = False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __init__(self, name, img_url, type, ability, hp, attack, defense, special_attack, special_defense, speed, date_created, user_id):
        self.name = name
        self.img_url = img_url
        self.type = type
        self.ability = ability
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.special_attack = special_attack
        self.special_defense = special_defense
        self.speed = speed
        self.date_created = date_created
        self.user_id = user_id
        
