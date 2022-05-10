from main import db
from datetime import datetime




class Jisho(db.Model):
    __tablename__ = "jishos"
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200),nullable=False)
    content = db.Column(db.String(30),nullable=False)
    jap_translation = db.Column(db.String(),default='This is a pineapple pen')
    date_created = db.Column(db.DateTime,default=datetime.utcnow,nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    
    def __repr__(self):
        return f"<Jisho ( '{self.title}', '{self.date_created}'>"