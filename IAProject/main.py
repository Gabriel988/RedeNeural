from Repositorys.Pessoa import PessoaRepository
from Repositorys.Financeiro import FinanceiroRepository
from Repositorys.FinanceiroResumo import FinanceiroResumoRepository
from Models.Pessoa import Pessoa
from Models.Financeiro import Financeiro
from Models.FinanceiroResumo import FinanceiroResumo
from TableManeger.Tabela import Tabela
from sklearn.preprocessing import LabelEncoder

header_pessoa = list(Pessoa().__dict__.keys())
header_financeiro = list(Financeiro().__dict__.keys())
header_financeiro_resumo = list(FinanceiroResumo().__dict__.keys())

query_financeiro_Resumo = FinanceiroResumoRepository().get_all()
Tabela().render_table(header_financeiro_resumo, query_financeiro_Resumo)

label_encoder_receita = LabelEncoder()
label_encoder_despesa = LabelEncoder()
label_encoder_emprestimos_feitos = LabelEncoder()
label_encoder_emprestimos_pagos = LabelEncoder()
label_encoder_nome_sujo = LabelEncoder()
label_encoder_score_serasa = LabelEncoder()

list_encoder = list()
len_list_keys = FinanceiroResumo().__dict__.keys().__len__()
list_keys = FinanceiroResumo().__dict__.keys()

Tabela().extractor()

Tabela().render_table(header_financeiro_resumo, list_encoder)

