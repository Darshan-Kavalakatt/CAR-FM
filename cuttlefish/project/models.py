from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

db = SQLAlchemy()
bcrypt = Bcrypt()

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    password_hash = db.Column(db.String(128), nullable=False)
    first_name = db.Column(db.String(128), nullable=False)
    last_name = db.Column(db.String(128),nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    
    def set_password(self, password):
        self.password_hash = bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password_hash, password)
    
    def update_user(self,new_attrs):
        for key, value in new_attrs.items():
            if hasattr(self, key):
                setattr(self, key, value)
        db.session.commit()
    
    def __repr__(self):
        return f'<User> {self.first_name}'
    
    def __init__(self,first_name,last_name,password,email):
        self.first_name = first_name
        self.last_name = last_name
        self.set_password(password)
        self.email = email
