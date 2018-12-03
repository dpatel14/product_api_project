from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from product_api.config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
ma = Marshmallow(app)

from product_api import routes
from product_api.products import routes
from product_api.product_logs import routes
from product_api.pagination import routes
