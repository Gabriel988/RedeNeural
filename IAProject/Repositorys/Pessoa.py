from Connections.MySQLConnective import ConnectionToServer
from Models.Pessoa import Pessoa
from Mapper.Mapeamento import Map


class PessoaRepository:

    def __init__(self):
        self.conexao = ConnectionToServer()

    def get_all(self):
        self.conexao.connect_to_server()
        cursor = self.conexao.cursor()
        try:
            query = "SELECT * FROM Pessoa"
            cursor.execute(query)
            res = cursor.fetchall()
            list_pessoa = Map().map_all(model=Pessoa, list_cursor=res)
        except Exception as e:
            print(f"Ocorreu um erro na get_all: {e}")
            list_pessoa = None
        finally:
            cursor.close()
            self.conexao.close_connection()
            print(f'Conexão com a base de dados {self.conexao.database} encerrada')
        return list_pessoa

    def get_by_Id(self, id):
        self.conexao.connect_to_server()
        cursor = self.conexao.cursor()
        try:
            query = "SELECT * FROM Pessoa WHERE Id = %(id)s"
            cursor.execute(query, {'id': id})
            res = cursor.fetchone()
            pessoa = Map().map_one(model=Pessoa, cursor=res)
        except Exception as e:
            print(f"Ocorreu um erro na get_by_Id: {e}")
            pessoa = None
        finally:
            cursor.close()
            self.conexao.close_connection()
            print(f'Conexão com a base de dados {self.conexao.database} encerrada')
        return pessoa