from tabulate import tabulate
from sklearn.preprocessing import LabelEncoder
from numpy.core import ndarray


class Tabela:
    def __init__(self):
        pass

    def render_table(self, header, obj):
        data = [header]
        if type(obj) is list:
            if type(obj[1]) is ndarray:
                for i in obj:
                    data.append(i)
            else:
                for i in obj:
                    data.append(i.__str__())
        else:
            data.append(obj.__str__())
        return print(tabulate(data, headers='firstrow', tablefmt="grid", numalign="center", stralign='center'))

    def extractor_to_matriz(self, list, props, encoder=False):
        if encoder is True:
            matriz = []
            for obj in list:
                matriz.append(LabelEncoder().fit_transform([getattr(obj, attr) for attr in props]))
            return matriz
        else:
            return [[getattr(obj, attr) for attr in props] for obj in list]
