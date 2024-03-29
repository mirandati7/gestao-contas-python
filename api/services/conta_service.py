from api import db
from ..models import conta_model

def listar_contas(usuario):
    contas = conta_model.Conta.query.filter_by(usuario_id=usuario).all()
    return contas

def listar_conta_id(id):
    conta = conta_model.Conta.query.filter_by(id=id).first()
    return conta

def cadastrar_conta(conta):
    conta_bd  = conta_model.Conta(nome= conta.nome, resumo=conta.resumo, valor=conta.valor, usuario_id=conta.usuario)
    db.session.add(conta_bd)
    db.session.commit()
    return conta_bd


def atualizar_conta(conta, conta_nova):
    conta.nome = conta_nova.nome
    conta.resumo = conta_nova.resumo
    conta.valor = conta_nova.valor
    db.session.commit()
    return conta

def excluir_conta(conta):
    db.session.delete(conta)
    db.session.commit()
def alterar_saldo_conta(conta_id, operacao, tipo_funcao, valor_antigo=None):
    conta = listar_conta_id(conta_id)
    # tipo_função -> 1 = Cadastro de Operacao
    # tipo_função -> 2 = Atualização de Operação
    # tipo_função -> 3 = Remoção de Operação
    if tipo_funcao == 1:
        if operacao.tipo == "entrada":
            conta.valor += operacao.custo
        else:
            conta.valor -= operacao.custo
    elif tipo_funcao == 2:
        if operacao.tipo == "entrada":
            conta.valor -= valor_antigo
            conta.valor += operacao.custo
        else:
            conta.valor += valor_antigo
            conta.valor -= operacao.custo
    else:
        if operacao.tipo == "entrada":
            conta.valor += operacao.custo
        else:
            conta.valor -= operacao.custo

    db.session.commit()

