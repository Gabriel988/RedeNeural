class Pessoa:
    def __init__(self, **kwargs):
        self.id = kwargs.get('id')
        self.nome = kwargs.get('nome')
        self.idade = kwargs.get('idade')
        self.sexo = kwargs.get('sexo')
        self.documento = kwargs.get('documento')

