from run import app,db
import pandas as pd
import numpy as np
from yawmi.models import Cours

pd.read_csv("yawmi/csv/file_clean.csv",sep=";")
with app.app_context():
    db.create_all()
    names=set()
    for image,name,url,category in [line.strip().split(';') for line in open("yawmi/csv/file_clean.csv").readlines()[1:] if line.strip()]:
        if name not in names and "pluralsight" not in url:
            cours=Cours(name=name,image=image,url=url,category=category)
            print("name:"+name)
            print("image:" + image)
            print("url:"+url)
            db.session.add(cours)
            db.session.commit()
            names.add(name)
