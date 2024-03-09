from . import db 
from flask_login import UserMixin
from sqlalchemy.sql import func
from datetime import datetime

class Friend(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    description = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    friend_type = db.Column(db.String(50))
    years = db.Column(db.Integer)
    common = db.Column(db.Text)
    likes = db.Column(db.Text)
    how_met = db.Column(db.Text)
    best_memory = db.Column(db.Text)
    additional_info = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return f"Friend('{self.name}', '{self.friend_type}')"

    @property
    def user(self):
        return User.query.get(self.user_id)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    friends = db.relationship('Friend', backref='owner', lazy=True)

    def __repr__(self):
        return f"User('{self.email}', '{self.first_name}')"


