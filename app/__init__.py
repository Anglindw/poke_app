from flask import Flask
from config import Config
from .auth.routes import auth
from .dex.routes import dex
app = Flask(__name__)

app.config.from_object(Config)
app.register_blueprint(auth)
app.register_blueprint(dex)

from . import routes