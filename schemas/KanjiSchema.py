from main import ma
from models.Kanji import Kanji
from marshmallow.validate import Length
from schemas.UserSchema import UserSchema

class KanjiSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Kanji

    
    kanji_id = ma.auto_field()
    heisig_level = ma.auto_field()
    character = ma.String(required=True)
    meaning = ma.String(required=True)
    onyomi = ma.String()
    kunyomi = ma.String()
    
    
kanji_schema = KanjiSchema()
kanjis_schema = KanjiSchema(many=True)
