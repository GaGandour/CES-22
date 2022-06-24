import abc

class Pai(abc.ABC):

    @abc.abstractmethod
    def imprimir(self):
        print("pai")

class Filho(Pai):
    def imprimir(self):
        super().imprimir()
        print("filho")

    def imprimir2(self):
        print("filho2")

filho = Filho()

a = "2,,,1"
a = a.replace(",",".")
print(a)