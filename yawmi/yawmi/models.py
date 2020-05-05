from flask_login import UserMixin
from . import db
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy 
from flask_wtf import FlaskForm
from wtforms_sqlalchemy.fields import QuerySelectField

class Cours(db.Model):
    __Tablename__ = 'cours'
    id = db.Column(db.Integer,
                   unique=True, autoincrement=True)
    name = db.Column(db.String(100),primary_key=True,)
    images = db.Column(db.LargeBinary, nullable = True)
    url = db.Column(db.String())
    category = db.Column(db.String(100))

class Planning(db.Model):
    __Tablename__ = 'planning'
    id = db.Column(db.Integer, primary_key=True,
                   unique=True, autoincrement=True)
    name_cours = db.Column(db.Integer, db.ForeignKey('Cours.name'))
    id_user = db.Column(db.Integer, db.ForeignKey('User.id'))
    start_date = db.Column(db.DateTime)
    end_date = db.Column(db.DateTime)
    
    def __repr__(self):
        return '[Plannings {}]'.format(self.id_cours)

def planning_query():
    return Planning.query 

class ChoiceForm(FlaskForm):
    opts = QuerySelectField(query_factory=planning_query, allow_blank=False, get_label='name_cours')

class User(UserMixin, db.Model):
    # primary keys are required by SQLAlchemy
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
