from product_api import app,db
from flask_rest_jsonapi import Api

import json
api = Api(app)

@app.before_first_request
def setup():    
    db.drop_all()
    db.create_all()