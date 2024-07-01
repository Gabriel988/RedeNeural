from Connections.MySQLConnective import ConnectionToServer
from Models.Financeiro import Financeiro
from Mapper.Mapeamento import Map


class FinanceiroRepository:

    def __init__(self):
        self.conexao = ConnectionToServer()

    def get_all(self):
        self.conexao.connect_to_server()
        cursor = self.conexao.cursor()
        try:
            query = "SELECT * FROM Financeiro"
            cursor.execute(query)
            res = cursor.fetchall()
            list_financeiro = Map().map_all(model=Financeiro, list_cursor=res)
            print('Query realizada com sucesso!')
        except Exception as e:
            print(f"Ocorreu um erro na get_all: {e}")
            list_financeiro = None
        finally:
            cursor.close()
            self.conexao.close_connection()
            print(f'Conexão com a base de dados {self.conexao.database} encerrada')
        return list_financeiro

    def get_by_Id(self, id):
        self.conexao.connect_to_server()
        cursor = self.conexao.cursor()
        try:
            query = "SELECT * FROM Financeiro WHERE Id = %(id)s"
            cursor.execute(query, {'id': id})
            res = cursor.fetchone()
            financeiro = Map().map_one(model=Financeiro, cursor=res)
            print('Query realizada com sucesso!')
        except Exception as e:
            print(f"Ocorreu um erro na get_by_Id: {e}")
            financeiro = None
        finally:
            cursor.close()
            self.conexao.close_connection()
            print(f'Conexão com a base de dados {self.conexao.database} encerrada')
        return financeiro
