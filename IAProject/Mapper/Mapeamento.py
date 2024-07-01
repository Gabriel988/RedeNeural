
class Map:

    def map_one(self, model=object, cursor=tuple):
        try:
            keys = model().__dict__.keys()
            obj_dict = dict(zip(keys, cursor))
            return model(**obj_dict)
        except Exception as e:
            print('Erro ao mapear entidade')

    def map_all(self, model=object, list_cursor=list):
        try:
            list_model = []
            for i in list_cursor:
                keys = model().__dict__.keys()
                obj_dict = dict(zip(keys, i))
                list_model.append(model(**obj_dict))
            return list_model
        except Exception as e:
            print('Erro ao mapear todas as entidades')
