from main import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
    
    
    
class User(db.Model, UserMixin):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20),unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String,nullable=False, default='netflix_logo.png')
    password = db.Column(db.String(60), nullable=False)
    jishos = db.relationship("Jisho", backref="user", lazy="dynamic")

    def __repr__(self):
        return f"<User( '{self.username}','{self.email}','{self.image_file}')>"