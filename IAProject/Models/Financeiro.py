
class Financeiro:
    def __init__(self, **kwargs):
        self.id = kwargs.get('id')
        self.id_pessoa = kwargs.get('id_pessoa')
        self.receita = kwargs.get('receita')
        self.despesa = kwargs.get('despesa')
        self.emprestimos_feitos = kwargs.get('emprestimos_feitos')
        self.emprestimos_pagos = kwargs.get('emprestimos_feitos')
        self.nome_sujo = kwargs.get('nome_sujo')
        self.score_serasa = kwargs.get('score_serasa')
