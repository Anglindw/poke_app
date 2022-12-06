from flask import Flask
from config import Config
from flask_migrate import Migrate
from .models import db
from .auth.routes import auth
from .dex.routes import dex
app = Flask(__name__)

app.config.from_object(Config)
app.register_blueprint(auth)
app.register_blueprint(dex)

db.init_app(app)
migrate = Migrate(app, db)

from . import routes
from . import models