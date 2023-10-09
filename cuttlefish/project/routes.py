from flask import Blueprint, jsonify, request,make_response
from flask_jwt_extended import create_access_token
from project.models import User, db
from project.util import *
from flask_wtf.csrf import generate_csrf

bp = Blueprint('routes', __name__)

@bp.route('/csrf-token', methods=['GET'])
def send_csrf_token():
    token = generate_csrf()
    response = make_response(jsonify(success=True, csrf_token=token))
    response.set_cookie('csrf_token', token, httponly=True, samesite='None')  # set it as HttpOnly cookie
    return response


@bp.route('/login', methods=['POST'])
def login():
    if request.json is None:
        return jsonify({"msg": "Missing JSON in request"}), 400

    email = request.json.get('email', None)
    password = request.json.get('password', None)

    user = User.query.filter_by(email=email).first()
    if user is None or not user.check_password(password):
        return jsonify({"msg": "Bad email or password"}), 401

    access_token = create_access_token(identity=email)
    response = make_response("Login Successful",200)
    response.set_cookie("access_token",access_token,httponly=True,secure=True,samesite='Strict')
    return response


# This is for registration page
@bp.route('/register',methods=['POST'])
def register():
    if not request.json:
        return jsonify({"msg":"Missing JSON in request"}), 400
    
    userAttr = convert_user_json_to_dict(request.json)


    user_with_email = User.query.filter_by(email=userAttr["email"]).first()
    if user_with_email:
        return jsonify({"msg":"Email is already in use"}),409

    db.session.commit()

    user = User(**userAttr)
    db.session.add(user)
    db.session.commit()
    return jsonify({"msg":"User successfully created"}),200
