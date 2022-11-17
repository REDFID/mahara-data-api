import redis
from flask import Flask
from flask_session import Session
from flask_bcrypt import Bcrypt
from flask_cors import CORS
from dotenv import load_dotenv
load_dotenv()

from .settings import *

app = Flask(__name__)

app.config["SECRET_KEY"] = SECRET_KEY
app.config["DEBUG"] = DEBUG

app.config["SESSION_TYPE"] = 'redis'
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_USE_SIGNER"] = True
app.config["SESSION_REDIS"] = redis.from_url(REDIS_URL)
server_session = Session(app)

bcrypt = Bcrypt(app)
CORS(app, supports_credentials=True)

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://{}:{}@{}:{}/{}".format(DB_USER, DB_PASSWORD, DB_HOST, DB_PORT, DB_NAME)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
from .models import db
db.init_app(app)

from .views import views as views_blueprint
app.register_blueprint(views_blueprint)

