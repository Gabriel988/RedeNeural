import mysql.connector
from mysql import connector


class ConnectionToServer(mysql.connector.MySQLConnection):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.obj_connect = {
            "host": "localhost",
            "user": "root",
            "password": "Gbriel988!",
            "database": "iabase",
        }

    def connect_to_server(self):
        try:
            self.connect(**self.obj_connect)
            if self.is_connected():
                print(f'Conexão com a base de dados [{self.database}] estabelecida')
            else:
                print('Conexão com a base de dados não estabelecida')
        except connector.Error as e:
            print(f'Erro ao tentar realizar uma conexão com o servidor {e}')

    def close_connection(self, connection=connector.MySQLConnection()):
        try:
            if connection is not None and connection.is_connected():
                print(f'Conexão com a base de dados [{connection.database}] Encerrada')
                return connection.close()
        except connector.Error as e:
            print(f'Erro ao tentar fechar uma conexão com o servidor {e}')
