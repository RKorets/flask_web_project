from . import db


class User(db.Model):
    __tablename__ = 'user_contact'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), index=True, unique=True)
    address = db.Column(db.String(150), nullable=True)

    email = db.relationship('Email', back_populates='user', cascade="all, delete")
    phone = db.relationship('Phone', back_populates='user', cascade="all, delete")


class Email(db.Model):
    __tablename__ = "email"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(50), nullable=True)

    user_id = db.Column(db.Integer, db.ForeignKey('user_contact.id', ondelete="CASCADE"), nullable=True)
    user = db.relationship('User', back_populates='email')


class Phone(db.Model):
    __tablename__ = "phone"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    phone = db.Column(db.String(50), nullable=True)

    user_id = db.Column(db.Integer, db.ForeignKey('user_contact.id', ondelete="CASCADE"), nullable=True)
    user = db.relationship('User', back_populates='phone')
