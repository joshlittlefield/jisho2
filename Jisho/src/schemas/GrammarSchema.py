from main import ma
from models.Grammar import Grammar
from marshmallow.validate import Length
from schemas.UserSchema import UserSchema

class GrammarSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Grammar

    
    grammar_id = ma.auto_field()
    grammar_level = ma.auto_field()
    character = ma.String(required=True)
    meaning = ma.String(required=True)
    sentence = ma.String()
    
    
    
grammar_schema = GrammarSchema()
grammars_schema = GrammarSchema(many=True)
