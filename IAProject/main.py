from Repositorys.Pessoa import PessoaRepository
from Repositorys.Financeiro import FinanceiroRepository
from Repositorys.FinanceiroResumo import FinanceiroResumoRepository
from Models.Pessoa import Pessoa
from Models.Financeiro import Financeiro
from Models.FinanceiroResumo import FinanceiroResumo
from TableManeger.Tabela import Tabela


header_pessoa = list(Pessoa().__dict__.keys())
header_financeiro = list(Financeiro().__dict__.keys())
header_financeiro_resumo = list(FinanceiroResumo().__dict__.keys())

query_financeiro_Resumo = FinanceiroResumoRepository().get_all()
Tabela().render_table(header_financeiro_resumo, query_financeiro_Resumo)

