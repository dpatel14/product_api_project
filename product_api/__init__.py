from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)

app.config['DB2_HOSTNAME'] = 'Mysql@localhost:3306'
app.config['DB2_PORT'] = 3306
app.config['DB2_PROTOCOL'] = 'TCP/IP'
app.config['DB2_DATABASE'] = 'texada'
app.config['DB2_USER'] = 'root'
app.config['DB2_PASSWORD'] = 'root'

app.config['SECRET_KEY'] = '\xd7@\xc6\x1a\x1bb\xc1\xce\n\xf2\x06\x8c\xf5\xbf\xe4\xd1\x12U\x9f\xa4C\xac\x15l'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)
ma = Marshmallow(app)

from product_api import routes

