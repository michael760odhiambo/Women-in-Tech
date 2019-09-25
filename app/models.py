from . import db

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    message_id = db.Column(db.Integer,db.ForeignKey('messages.id'))
    
    def __repr__(self):
        return f'User{self.username}'
class Message(db.Model):
    __tablename__ = 'messages'

    id = db.Column(db.Integer,primary_key = True)
    message = db.Column(db.String(255))

    def __repr__(self):
        return f'User {self.message}'        