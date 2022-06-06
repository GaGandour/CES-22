from abc import abstractmethod

class Bolo:
    def __init__(self, tipo = None, sabor = None):
        self.tipo = tipo
        self.sabor = sabor
   

class CakeBuilder:
    @abstractmethod
    def reset(self):
        pass

    @abstractmethod
    def sabor_builder(self):
        pass

    @abstractmethod
    def tipo_builder(self):
        pass


class BoloDeAniversarioBuilder(CakeBuilder):
    def reset(self):
        self.cake = Bolo()

    def sabor_builder(self, sabor):
        self.cake.sabor = sabor

    def tipo_builder(self):
        self.cake.tipo = "Aniversário"

    def get_bolo(self):
        return self.cake


class BoloDeCasamentoBuilder(CakeBuilder):
    def reset(self):
        self.cake = Bolo()

    def sabor_builder(self, sabor):
        self.cake.sabor = sabor

    def tipo_builder(self):
        self.cake.tipo = "Casamento"

    def get_bolo(self):
        return self.cake


class BoloDeFestaInformalBuilder(CakeBuilder):
    def reset(self):
        self.cake = Bolo()

    def sabor_builder(self, sabor):
        self.cake.sabor = sabor

    def tipo_builder(self):
        self.cake.tipo = "Festa Informal"

    def get_bolo(self):
        return self.cake


class CakeDirector:
    def __init__(self, builder):
        self.builder = builder

    def change_builder(self, builder):
        self.builder = builder

    def build_bolo(self, sabor):
        self.builder.reset()
        self.builder.tipo_builder()
        self.builder.sabor_builder(sabor)
        return self.builder.get_bolo()


b = BoloDeAniversarioBuilder()
d = CakeDirector(b)
d.build_bolo
p = b.get_bolo()