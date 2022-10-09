from api import ma
from ..models import conta_model
from marshmallow import fields

class ContaSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = conta_model.Conta
        load_instance = True

        nome = fields.String(required=True)
        resumo = fields.String(required=True)
        valor = fields.Float(required=True)