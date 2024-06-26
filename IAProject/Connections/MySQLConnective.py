from mysql import connector


class ConnectionToServer:

    def __init__(self, user, password, host, database):
        self.user = user
        self.password = password
        self.host = host
        self.database = database

    def connect_to_server(self):
        try:
            connection = connector.connect(user=self.user, password=self.password, host=self.host,
                                           database=self.database)
            print(f'Conexão com a base de dados [{connection.database}] estabelecida')
            return connection
        except connector.Error as e:
            print(f'Erro ao tentar realizar uma conexão com o servidor {e}')


    def close_connection(self, connection=connector.MySQLConnection()):
        try:
            if connection is not None and connection.is_connected():
                print(f'Conexão com a base de dados [{connection.database}] Encerrada')
                return connection.close()
        except connector.Error as e:
            print(f'Erro ao tentar fechar uma conexão com o servidor {e}')
