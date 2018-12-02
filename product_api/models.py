from product_api import db
from datetime import datetime
from product_api import app,db

class Product(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(20), unique=True, nullable=False)

db.create_all()

