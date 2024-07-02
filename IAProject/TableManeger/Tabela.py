from tabulate import tabulate


class Tabela:
    def __init__(self):
        pass

    def render_table(self, header, obj):
        data = [header]
        if type(obj) is list:
            for i in obj:
                data.append(i.__str__())
        else:
            data.append(obj.__str__())
        return print(tabulate(data, headers='firstrow', tablefmt="grid", numalign="center", stralign='center'))

    def extractor(self,):
        pass
