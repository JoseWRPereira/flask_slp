from flask import Flask, render_template
from app.auth.auth import auth_bp
from app.db.database import database_bp

app = Flask(__name__)
app.config.from_object('config')
app.register_blueprint(auth_bp)
app.register_blueprint(database_bp)

@app.route("/")
def index():
    return render_template('index.html')


