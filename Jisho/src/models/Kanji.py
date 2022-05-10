from main import db
from datetime import datetime




class Kanji(db.Model):
    __tablename__ = "kanjis"
    
    kanji_id = db.Column(db.Integer, primary_key=True)
    heisig_level=db.Column(db.Integer)
    jlpt_level=db.Column(db.Integer)
    school_level=db.Column(db.Integer)
    character=db.Column(db.String(200),nullable=False)
    meaning=db.Column(db.String(200),nullable=False)
    onyomi=db.Column(db.String(200),nullable=False)
    kunyomi=db.Column(db.String(200),nullable=False)
    is_radical=db.Column(db.String(200))
    R1_radical_used=db.Column(db.String(200))
    R2_radical_used=db.Column(db.String(200))
    R3_radical_used=db.Column(db.String(200))
    R4_radical_used=db.Column(db.String(200))
    R5_radical_used=db.Column(db.String(200))
    story=db.Column(db.String(200))
    
    
    def __repr__(self):
        return f"<Kanji ( '{self.kanji_id}','{self.heisig_level}', '{self.character}', '{self.meaning}', '{self.onyomi}', '{self.kunyomi}'>" 