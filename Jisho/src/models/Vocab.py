from main import db
from datetime import datetime




class Vocab(db.Model):
    __tablename__ = "vocabs"
    
    vocab_id = db.Column(db.Integer, primary_key=True)
    kanji_id = db.Column(db.Integer, db.ForeignKey('kanjis.kanji_id'), nullable=False)
    heisig_level=db.Column(db.Integer)
    
    word=db.Column(db.String(200),nullable=False)
    meaning=db.Column(db.String(200),nullable=False)
    reading=db.Column(db.String(200),nullable=False)
    sentence=db.Column(db.String(200),nullable=False)
    
    
    
    def __repr__(self):
        return f"<Kanji ( '{self.vocab_id}','{self.kanji_id}','{self.heisig_level}', '{self.word}', '{self.meaning}', '{self.reading}', '{self.sentence}'>" 