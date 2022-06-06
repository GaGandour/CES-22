from abc import abstractmethod


class CakeFactory:
    @abstractmethod
    def create_bolo_de_chocolate(self):
        pass

    @abstractmethod
    def create_bolo_de_mandioca(self):
        pass

    @abstractmethod
    def create_bolo_de_cenoura(self):
        pass


class BoloDeAniversarioFactory(CakeFactory):
    def create_bolo_de_chocolate(self):
        return Bolo("Aniversário", "Chocolate")
    
    def create_bolo_de_mandioca(self):
        return Bolo("Aniversário", "Mandioca")

    def create_bolo_de_cenoura(self):
        return Bolo("Aniversário", "Cenoura")


class BoloDeCasamentoFactory(CakeFactory):
    def create_bolo_de_chocolate(self):
        return Bolo("Casamento", "Chocolate")

    def create_bolo_de_mandioca(self):
        return Bolo("Casamento", "Mandioca")

    def create_bolo_de_cenoura(self):
        return Bolo("Casamento", "Cenoura")


class BoloDeFestaInformalFactory(CakeFactory):
    def create_bolo_de_chocolate(self):
        return Bolo("Festa Informal", "Chocolate")

    def create_bolo_de_mandioca(self):
        return Bolo("Festa Informal", "Mandioca")

    def create_bolo_de_cenoura(self):
        return Bolo("Festa Informal", "Cenoura")


class Bolo:
    def __init__(self, tipo, sabor):
        self.tipo = tipo
        self.sabor = sabor
        