from tabulate import tabulate


class Tabela:
    def __init__(self):
        pass

    def render_table(self, header, list):
        data = [header]
        for i in list:
            data.append(i.__str__())
        return print(tabulate(data, headers='firstrow', tablefmt="grid", numalign="center", stralign='center'))