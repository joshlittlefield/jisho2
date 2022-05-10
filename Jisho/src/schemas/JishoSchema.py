from main import ma
from models.Jisho import Jisho
from marshmallow.validate import Length
from schemas.UserSchema import UserSchema

class JishoSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Jisho

    jisho_title = ma.String(required=True, validate=Length(min=1))
    jisho_content = ma.String(required=True, validate=Length(min=1))
    jap_translation = ma.String(required=True,validate=Length(min=1))
    date_created = ma.DateTime(required=True)
    user_id =  ma.Nested(UserSchema)
    
jisho_schema = JishoSchema()
jishos_schema = JishoSchema(many=True)