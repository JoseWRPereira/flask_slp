from flask import Flask, render_template
from app.auth.auth import auth_bp

app = Flask(__name__)
app.register_blueprint(auth_bp)


@app.route("/")
def hello():
    return render_template('index.html')


