class Mamifero:
    def __init__(self, nome, idade, peso, especie):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.especie = especie
        print("O mamifero {} foi criado\n".format(self.nome))

    def __str__(self):
        return f'{self.nome} é um mamifero da especie {self.especie} de {self.idade} anos e pesa {self.peso} kg.'


class Estimacao:
    def __init__(self, nome, dono, especie):
        self.nome = nome
        self.dono = dono
        self.especie = especie
        print("O animal de estimação {} foi criado\n".format(self.nome))

    def __str__(self):
        return f'{self.nome} é um {self.especie} do {self.dono}.'


class Cachorro(Mamifero, Estimacao):
    def __init__(self, nome, idade, peso, dono):
        super().__init__(nome, idade, peso, "canis familiaris")
        self.dono = dono

    def __str__(self):
        return super().__str__() + f'\n{self.nome} é um cachorro do {self.dono}.'

rex = Cachorro("Rex", 5, 10, "João")