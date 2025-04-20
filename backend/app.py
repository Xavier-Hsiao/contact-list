from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from config import Config

app = Flask(__name__)
CORS(app)

app.config.from_object(Config)

db = SQLAlchemy(app)

import routes

with app.app_context():
      db.create_all()

if __name__ == "__main__":
      app.run(debug=True)
