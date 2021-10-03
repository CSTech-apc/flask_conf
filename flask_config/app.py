from flask import Flask
from flask_config.ext import configuration
from flask_config.ext import appearance
from flask_config.ext import migrate
from flask_config.ext import views

app = Flask(__name__)
configuration.init_app(app)
appearance.init_app(app)
migrate.init_app(app)
db = migrate.db
views.init_app(app)
