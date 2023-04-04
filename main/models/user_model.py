from .. import db, bcrypt
from ..schema.user_schema import UserSchema
from flask import json
import jwt
from datetime import datetime, timedelta
from ..static.sqlToJSON import converUserToJSON

class User_model():
    def signup(self, userInfo):
        user=UserSchema.query.filter_by(email=userInfo['email']).first()
        if not user:
            name=userInfo['name']
            email=userInfo['email']
            password=userInfo['password']
            newUser=UserSchema(name, email, password)
            db.session.add(newUser)
            db.session.commit()
            return json.dumps({
                "success":True,
                "message":"New user is created",
            }), 200
        else:
             return json.dumps({
                "success":False,
                "message":"User already exist",
            }), 400



    def login(self, userInfo):
        loggingUser=UserSchema.query.filter_by(email=userInfo['email']).first()
        if not loggingUser:
            return json.dumps({
                "success":False,
                "message":"User is not exist"
            }), 400
           
            
        elif bcrypt.check_password_hash(loggingUser.password, userInfo['password']):
              loggingUser=converUserToJSON(loggingUser)
              expTime=datetime.now()+ timedelta(hours=15)
              expEpochTime=int(expTime.timestamp())

              payload={
                   "payload":loggingUser,
                   "exp":expEpochTime
              }

              jwtToken=jwt.encode(payload, "secret", algorithm="HS256")

              return json.dumps({
                "success":True,
                "message":"User Found",
                "data":{
                   "token":jwtToken,
                   "user":loggingUser
                }
            }), 200
        else:
               return json.dumps({
                "success":False,
                "message":"Username or password is wrong"
            }), 200

    
     