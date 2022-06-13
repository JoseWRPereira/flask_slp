from flask import Blueprint
from flask import make_response, jsonify, json
from app.db.dbcon import DBConn

api_bp = Blueprint('api_bp', __name__)

@api_bp.route('/api/help')
def api_help():
    response = make_response( jsonify({"Nome": "José"}), 200 )
    response.headers["Content-Type"] = "application/json"
    return response

@api_bp.route('/api/v1/users')
def api_v1_users():
    db = DBConn()
    users = db.sql_fetch("SELECT * from users;")
    header = ["id", "name", "email", "password", "nif", "admin"]

    dicio = []
    for user in users:
        dicio.append( dict( zip(header, user)) )

    response = make_response( jsonify(dicio, 200) )
    response.headers["Content-Type"] = "application/json"
    return response
