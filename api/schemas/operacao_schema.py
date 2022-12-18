from api import ma
from ..models import operacao_model
from marshmallow import fields

class OperacaoSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = operacao_model.Operacao
        load_instance = True

        nome = fields.String(required=True)
        resumo = fields.String(required=True)
        custo = fields.Float(required=True)
        tipo = fields.String(required=True)