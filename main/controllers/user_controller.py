from flask import Blueprint, request
from ..models.user_model import User_model
from ..models.jwt_auth import token_required
from ..static.sqlToJSON import converUserToJSON

user_route=Blueprint('user_route', __name__)

userModel=User_model()

@user_route.route('/')
def user():
    return "user route"

@user_route.route('/login', methods=['POST'])
def login():
    return userModel.login(request.form)

@user_route.route('/signup', methods=['POST'])
def signup():
    return userModel.signup(request.form)

@user_route.route('/edit_profile', methods=['POST'])
@token_required
def token(currentUser):
    currentUser=converUserToJSON(currentUser)
    print(request.form)
    return {
        "user":currentUser
    }, 200