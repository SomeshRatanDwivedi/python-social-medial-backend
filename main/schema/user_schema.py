from .. import db, bcrypt

class UserSchema(db.Model):
    __tablename__='usertable'
    id=db.Column(db.Integer, primary_key=True, autoincrement=True)
    name=db.Column(db.String(20), nullable=False)
    email=db.Column(db.String(50), nullable=False, unique=True)
    password=db.Column(db.String(255), nullable=False)

    def __init__(self, name, email, password):
        self.name=name
        self.email=email
        self.password=bcrypt.generate_password_hash(password, 10).decode('utf-8')
