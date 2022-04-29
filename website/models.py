from . import db 
from flask_login import UserMixin
from sqlalchemy.sql import func

class Note(db.Model):
    id = db.Column(db.Integer,primary_key=True) #id primary key
    data = db.Column(db.String(10000)) #content of note
    date = db.Column(db.DateTime(timezone=True),default = func.now()) #automatic date using func store the current date 
    user_id = db.Column(db.Integer,db.ForeignKey('user.id')) #Foreign key for user who create Note
    

class User(db.Model,UserMixin):
    id = db.Column(db.Integer,primary_key=True) #id primary key
    email = db.Column(db.String(150),unique=True)  #unique email
    password = db.Column(db.String(150)) #password not encrypted 
    first_name = db.Column(db.String(150)) #name 
    notes = db.relationship('Note')
    
    
    