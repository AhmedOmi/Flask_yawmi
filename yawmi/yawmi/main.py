from flask import Flask, Blueprint, render_template,redirect
from flask_login import login_required, current_user
from .models import Cours,Clic
from datetime import datetime
from . import db
main = Blueprint('main', __name__)



@main.route('/')
def index():
    return render_template('interfaces/index.html')


@main.route('/feature')
def feature():
    return render_template('interfaces/feature.html')


@main.route('/connect')
def connect():
    return render_template('index.html')


@main.route('/bog')
def blog():
    return render_template('interfaces/blog.html')


@main.route('/contact')
def contact():
    return render_template('/interfaces/contact.html')


@main.route('/profile')
@login_required
def profile():
    cours=Cours.query.limit(30).all()
    return render_template('profile.html', name=current_user.name,cours_list=cours)

@main.route('/follow_course/<int:cours_id>')
@login_required
def follow_course(cours_id):

    clic=Clic(id_user=current_user.id,id_cours=cours_id,date=datetime.now())
    db.session.add(clic)
    db.session.commit()
    return redirect(Cours.query.get(cours_id).url)
