from product_api import app,db
from datetime import datetime

from sqlalchemy import event, DDL
from sqlalchemy.event import listen

class Product(db.Model):	
	__tablename__ = 'product'
	
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(20), unique=True, nullable=False)
	
class ProductLog(db.Model):
	__tablename__ = 'productlog'	
	
	id = db.Column(db.Integer, primary_key=True,  autoincrement = True)
	posted_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
	longitude = db.Column(db.Float, nullable=False)
	latitude = db.Column(db.Float, nullable=False)
	elevation = db.Column(db.Integer, nullable=False)
	
	def __init__(self, posted_date,longitude,latitude,elevation):
		if posted_date is None:	
			self.posted_date = datetime.utcnow()
		else:
			self.posted_date = posted_date	
		self.longitude = longitude
		self.latitude = latitude
		self.elevation = elevation		
				
def product_insert_initial_values(*args, **kwargs):
	db.session.add(Product(name='Cesna 120'))	
	db.session.add(Product(name='DC-6 Twin Otter'))
	db.session.add(Product(name='Piper M600'))
	db.session.add(Product(name='Art Boom 6500'))
	db.session.commit()
	
def product_log_insert_initial_values(*args, **kwargs):
	db.session.add(ProductLog(posted_date=datetime(2016, 10, 14, 12),longitude=43.2583264,latitude=-81.8149807,elevation=500))
	db.session.add(ProductLog(posted_date=datetime(2016, 10, 14, 12),longitude=42.559112,latitude=-79.286693,elevation=550))
	db.session.add(ProductLog(posted_date=datetime(2016, 10, 14, 12),longitude=43.559112,latitude=-85.286693,elevation=600))
	db.session.add(ProductLog(posted_date=datetime(2016, 10, 15, 12),longitude=42.3119735,latitude=-83.0941179,elevation=650))	
	
	db.session.add(ProductLog(posted_date=datetime(2016, 10, 12, 12),longitude=43.459112,latitude=-80.386693,elevation=500))
	db.session.add(ProductLog(posted_date=datetime(2016, 10, 13, 12),longitude=42.459112,latitude=-79.386693,elevation=550))
	db.session.add(ProductLog(posted_date=datetime(2016, 10, 14, 12),longitude=43.459112,latitude=-85.386693,elevation=450))
	db.session.add(ProductLog(posted_date=datetime(2016, 10, 15, 12),longitude=44.459112,latitude=-81.386693,elevation=400))
	
	db.session.add(ProductLog(posted_date=datetime(2016, 10, 15, 12),longitude=44.459112,latitude=-81.386693,elevation=500))
	db.session.add(ProductLog(posted_date=datetime(2016, 10, 15, 12),longitude=45.459112,latitude=-82.386693,elevation=600))
	db.session.add(ProductLog(posted_date=datetime(2016, 10, 15, 12),longitude=46.459112,latitude=-83.386693,elevation=700))
	db.session.add(ProductLog(posted_date=datetime(2016, 10, 15, 12),longitude=47.459112,latitude=-84.386693,elevation=800))
	db.session.add(ProductLog(posted_date=datetime(2016, 10, 15, 12),longitude=48.459112,latitude=-85.386693,elevation=900))
	
	db.session.add(ProductLog(posted_date=datetime(2017, 8, 4, 14, 20, 38),longitude=43.7634618,latitude=-43.3688191,elevation=800))
	db.session.add(ProductLog(posted_date=datetime(2017, 8, 4, 16, 20, 38),longitude=43.8001468,latitude=-43.2342365,elevation=400))
	db.session.add(ProductLog(posted_date=datetime(2017, 8, 4, 14, 20, 38),longitude=44.51165,latitude=-44.51165,elevation=550))
	db.session.add(ProductLog(posted_date=datetime(2017, 8, 4, 14, 20, 38),longitude=43.1501439,latitude=-43.1501439,elevation=300))
	
	db.session.commit()
		
event.listen(Product.__table__, 'after_create', product_insert_initial_values)
event.listen(ProductLog.__table__, 'after_create', product_log_insert_initial_values)
