from Connections.MySQLConnective import ConnectionToServer
from Models.FinanceiroResumo import FinanceiroResumo
from Mapper.Mapeamento import Map


class FinanceiroResumoRepository:

    def __init__(self):
        self.conexao = ConnectionToServer()

    def get_all(self):
        self.conexao.connect_to_server()
        cursor = self.conexao.cursor()
        try:
            query = "SELECT * FROM FinanceiroResumo"
            cursor.execute(query)
            res = cursor.fetchall()
            list_financeiro_resumo = Map().map_all(model=FinanceiroResumo, list_cursor=res)
        except Exception as e:
            print(f"Ocorreu um erro na get_all: {e}")
            list_financeiro_resumo = None
        finally:
            cursor.close()
            self.conexao.close_connection()
            print(f'Conexão com a base de dados {self.conexao.database} encerrada')
        return list_financeiro_resumo

    def get_by_Id(self, id):
        self.conexao.connect_to_server()
        cursor = self.conexao.cursor()
        try:
            query = "SELECT * FROM FinanceiroResumo WHERE Id = %(id)s"
            cursor.execute(query, {'id': id})
            res = cursor.fetchone()
            financeiro_resumo = Map().map_one(model=FinanceiroResumo, cursor=res)
        except Exception as e:
            print(f"Ocorreu um erro na get_by_Id: {e}")
            financeiro_resumo = None
        finally:
            cursor.close()
            self.conexao.close_connection()
            print(f'Conexão com a base de dados {self.conexao.database} encerrada')
        return financeiro_resumo

    def risk_analysis(self):
        self.conexao.connect_to_server()
        cursor = self.conexao.cursor()
        try:
            cursor.callproc('RiskAnalysis')
        except Exception as e:
            print(f"Ocorreu um erro na risk_analysis: {e}")
        finally:
            cursor.close()
            self.conexao.close_connection()
            print(f'Conexão com a base de dados {self.conexao.database} encerrada')

