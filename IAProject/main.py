from Repositorys.Pessoa import PessoaRepository
from Repositorys.Financeiro import FinanceiroRepository
from Models.Pessoa import Pessoa
from Models.Financeiro import Financeiro
from TableManeger.Tabela import Tabela


header_pessoa = list(Pessoa().__dict__.keys())
header_financeiro = list(Financeiro().__dict__.keys())

query_pessoa = PessoaRepository().get_all()
Tabela().render_table(header_pessoa, query_pessoa)

