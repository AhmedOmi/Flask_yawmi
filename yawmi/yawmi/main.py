import pandas as pd
import numpy as np
from flask import Flask, Blueprint, render_template
from flask_login import login_required, current_user

main = Blueprint('main', __name__)

data = pd.read_csv("csv/file.csv")
dff = np.asarray(data)


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
    return render_template('profile.html', name=current_user.name)
