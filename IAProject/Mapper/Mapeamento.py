from mysql.connector.cursor import MySQLCursor


class Map:
    def __init__(self):
        self.entity = None,
        self.model = None

    def map_one(self, model, cursor=MySQLCursor):
        try:
            teste = model(**cursor)

        except Exception as e:
            print('Erro ao mapear entidade')
