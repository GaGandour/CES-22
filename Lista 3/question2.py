def meu_decorador(funcao):
    def explica_funcao(lista, dicionario):
        print("A funcao {} foi chamada:\n".format(funcao.__name__))
        funcao(lista, dicionario)
        print ("\nA funcao {} foi finalizada".format(funcao.__name__))

    return explica_funcao

@meu_decorador
def listar_palavras(lista, dicionario):
    for palavra in lista:
        print(palavra)
    print("")
    for chave, valor in dicionario.items():
        print(chave, ": ", valor)


minha_lista = [
    "hello",
    "world",
    "python",
    "is",
    "awesome"
    ]

meu_dicionario = {
    "Melhor linguagem" : "Python",
    "Melhor curso": "Engenharia de Computação",
    "Melhor turma": "T-24"}

listar_palavras(minha_lista, meu_dicionario)