from Connections.MySQLConnective import ConnectionToServer
from Models.Pessoa import Pessoa
from Mapper.Mapeamento import Map


class PessoasRepositorys:

    def __init__(self):
        self.conexao = ConnectionToServer(),
        self.model = type(Pessoa)

    def get_all(self):
        self.conexao.connect_to_server()
        cursor = self.conexao.cursor()
        try:
            query = "SELECT * FROM Pessoa"
            cursor.execute(query)
            list_pessoas = cursor.fetchall()
        except Exception as e:
            print(f"Ocorreu um erro na get_all: {e}")
            list_pessoas = None
        finally:
            cursor.close()
            self.conexao.close_connection()
        return list_pessoas

    def get_one(self):
        self.conexao.connect_to_server()
        cursor = self.conexao.cursor()
        try:
            query = "SELECT * FROM Pessoa"
            cursor.execute(query)
            pessoa = Map.map_one(self.model, cursor.fetchone())

        except Exception as e:
            print(f"Ocorreu um erro na get_all: {e}")
            pessoa = None
        finally:
            cursor.close()
            self.conexao.close_connection()
        return pessoa
