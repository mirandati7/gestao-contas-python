from flask_restful import Resource
from ..schemas import  operacao_schema
from flask import request, make_response, jsonify
from ..entidades import operacao
from ..services import operacao_service
from api import api

class OperacaoList(Resource):
    def post(self):
        os = operacao_schema.OperacaoSchema()
        validate = os.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            nome = request.json["nome"]
            resumo = request.json["resumo"]
            custo = request.json["custo"]
            tipo = request.json["tipo"]

            operacao_nova = operacao.Operacao(
                nome=nome,
                resumo=resumo,
                custo=custo,
                tipo=tipo
            )
            resultado = operacao_service.cadastrar_operacao(operacao_nova)
            return make_response(os.jsonify(resultado), 201)





api.add_resource(OperacaoList, '/operacoes')