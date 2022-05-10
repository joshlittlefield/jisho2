from main import db
from datetime import datetime




class Grammar(db.Model):
    __tablename__ = "grammars"
    
    grammar_id = db.Column(db.Integer, primary_key=True)
    grammar_level=db.Column(db.Integer)
    character=db.Column(db.String(200),nullable=False)
    meaning=db.Column(db.String(200),nullable=False)
    sentence=db.Column(db.String(200),nullable=False)
    
    
    def __repr__(self):
        return f"<Grammar ( '{self.grammar_id}','{self.grammar_level}', '{self.character}', '{self.meaning}', '{self.sentence}'>" 