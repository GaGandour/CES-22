import abc

class Materia(abc.ABC):
    __metaclass__ = abc.ABCMeta
    
    def __init__(self, professor, turma):
        super().__init__()
        self.professor = professor
        self.turma = turma

    @classmethod
    def caracteristicas(cls):
        print("Nome: {}\nSigla: {}\nCarga Horeria: {}".format(cls.nome, cls.sigla, cls.carga_horaria))

    @abc.abstractmethod
    def descricao(self):
        """ Metodo abstrato """

    @staticmethod
    def apresenta():
        print("Sou uma materia do ITA!\n")

    def muda_professor(self, novo_professor):
        self.professor = novo_professor
        

class CES22(Materia):
    nome = "Programação Orientada a Objetos"
    sigla = "CES22"
    carga_horaria = "4 creditos"

    def __init__(self, professor, turma):
        super().__init__(professor, turma)

    def descricao(self):
        print("Em {}, voce vai aprender a programar em Python com o professor {}!\n".format(self.sigla, self.professor))


class CES12(Materia):
    nome = "Algoritmos e Estruturas de Dados"
    sigla = "CES12"
    carga_horaria = "5 creditos"

    def __init__(self, professor, turma):
        super().__init__(professor, turma)

    def descricao(self):
        print("Em {}, voce vai aprender a implementar ervores rubro-negras com o professor {}!\n".format(self.sigla, self.professor))


class CES10(Materia):
    nome = "Introdução a Computação"
    sigla = "CES10"
    carga_horaria = "3 creditos"

    def __init__(self, professor, turma):
        super().__init__(professor, turma)

    """ Aqui, não iremos implementar a função descrição. Esperamos um erro. """
    
    

ces12 = CES12("Alonso", "24")
ces22 = CES22("Yano", "24")

CES12.apresenta()
CES12.caracteristicas()
ces12.descricao()
ces22.descricao()
ces22.muda_professor("Karla")
ces22.descricao()

"""Aqui, esperamos um erro porque não implementamos a função descrição."""
ces10 = CES10("Armando", "24")