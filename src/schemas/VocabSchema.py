from main import ma
from models.Vocab import Vocab
from marshmallow.validate import Length
from schemas.UserSchema import UserSchema

class VocabSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Vocab

    
    vocab_id = ma.auto_field()
    heisig_level = ma.auto_field()
    word = ma.String(required=True)
    meaning = ma.String(required=True)
    reading = ma.String(required=True)
    sentence = ma.String()
   
    
    
vocab_schema = VocabSchema()
vocabs_schema = VocabSchema(many=True)
