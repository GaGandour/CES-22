from abc import abstractmethod


class Veiculo:
    def __init__(self, tipo):
        self.tipo = tipo

    def __str__(self):
        return str(self.tipo)


class TipoDeVeiculo:
    def __init__(self, tipo, motorizacao):
        self.tipo = tipo
        self.motorizacao = motorizacao

    def __str__(self):
        return self.tipo + " - " + self.motorizacao.tipo


class Motorizacao:
    def __init__(self, tipo):
        self.tipo = tipo


class VeiculoFactory:
    @abstractmethod
    def criar_veiculo(self, motorizacao):
        pass


class CaminhaoFactory(VeiculoFactory):
    def criar_veiculo(self, motorizacao):
        tipo = TipoDeVeiculo("Caminhao", Motorizacao(motorizacao))
        return Veiculo(tipo)


class AutomovelFactory(VeiculoFactory):
    def criar_veiculo(self, motorizacao):
        tipo = TipoDeVeiculo("Automovel", Motorizacao(motorizacao))
        return Veiculo(tipo)


print("Criando Veiculo - Caminhao Eletrico:")

meu_caminhao = CaminhaoFactory().criar_veiculo("Eletrico")

print("Meu veiculo e:", str(meu_caminhao), "\n\n")

print("Criando Veiculo - Automovel Combustao:")

meu_caminhao = AutomovelFactory().criar_veiculo("Combustao")

print("Meu veiculo e:", str(meu_caminhao))