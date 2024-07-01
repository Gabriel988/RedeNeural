from Repositorys.Pessoas import PessoasRepository
from Repositorys.Financeiro import FinanceiroRepository
from tabulate import tabulate

list_pessoa = PessoasRepository().get_all()
list_financeiro = FinanceiroRepository().get_all()
cabecalho_pessoa = ['id', 'nome', 'idade', 'sexo', 'documento']

data = [cabecalho_pessoa]
for i in list_pessoa:
    data.append(i.__str__())

print(tabulate(data, headers='firstrow', tablefmt="grid"))
