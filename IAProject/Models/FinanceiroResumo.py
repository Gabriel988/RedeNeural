
class FinanceiroResumo:

    def __init__(self, **kwargs):
        self.id = kwargs.get('id')
        self.id_financeiro = kwargs.get('id_financeiro')
        self.receita_status = kwargs.get('receita_status')
        self.despesa_status = kwargs.get('despesa_status')
        self.emprestimos_feitos_status = kwargs.get('emprestimos_feitos_status')
        self.emprestimos_pagos_status = kwargs.get('emprestimos_feitos_status')
        self.nome_sujo_status = kwargs.get('nome_sujo_status')
        self.score_serasa_status = kwargs.get('score_serasa_status')

    def __str__(self):
        return [self.id, self.id_financeiro, self.receita_status, self.despesa_status, self.emprestimos_feitos_status
            , self.emprestimos_pagos_status, self.nome_sujo_status, self.score_serasa_status]