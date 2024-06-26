from Connections.MySQLConnective import ConnectionToServer


class Requests:

    def __init__(self):
        self.conexao = ConnectionToServer(host='localhost', user='root', password='Gbriel988!', database='iabase')

    def get_all(self, table):
        self.conexao.connect_to_server()
        cursor = self.conexao.cursor()
        query = "SELECT * FROM %s"
        cursor.execute(query, table)
        pessoas = cursor
        cursor.close()
        self.conexao.my_connection.close_connection()
        return pessoas
