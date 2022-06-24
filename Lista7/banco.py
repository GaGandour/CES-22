from tkinter import *
from tkinter import ttk
from banco_aux import Transacao

fields = ('Descrição', 'Valor')
extrato = [Transacao("Sorvete", 1), Transacao("Biscoito", 2)]

class MeuBotao:
    def __init__(self, master, text, command, row, column):
        self.botao = Button(master, text=text, command=command)
        self.botao.grid(row=row, column=column, sticky=W)

class QuitBotao:
    def __init__(self, master, row, column, root):
        self.botao = Button(master, text="Quit", command=root.quit)
        self.botao.grid(row=row, column=column, sticky=W)

class CriarTransacaoBotao:
    def __init__(self, master, row, column, entries, lista_de_transacoes):
        self.botao = Button(master, text="Criar Transação", command=(
            lambda e= entries: criar_transacao(e, lista_de_transacoes)))
        self.botao.grid(row=row, column=column, sticky=W)

class CalcularSaldoBotao:
    def __init__(self, master, row, column, extrato, saldo_label):
        self.botao = Button(master, text="Atualizar Saldo", command=(
            lambda : calcular_saldo(extrato, saldo_label)))
        self.botao.grid(row=row, column=column, sticky=W)



def make_form(content):
    entries = {}

    description = StringVar()
    value_string = StringVar()

    desc_label = Label(content, width=22, text="Descrição: ", anchor='w')
    desc_entry = Entry(content, textvariable=description)
    value_label = Label(content, width=22, text="Valor: ", anchor='w')
    value_entry = Entry(content, textvariable=value_string)

    desc_label.grid(row=0, column=0, sticky=E)
    desc_entry.grid(row=0, column=1)
    value_label.grid(row=1, column=0, sticky=E)
    value_entry.grid(row=1, column=1)

    # ent.insert(0,"")
    entries['Descrição'] = description
    entries['Valor'] = value_string
    return entries


def make_options(content, entries, l, extrato, saldo_label):
    frame = Frame(content, height=20)
    frame.grid(row=3, column=0)

    CriarTransacaoBotao(content, 4, 0, entries, l)
    CalcularSaldoBotao(content, 5, 0, extrato, saldo_label)
    QuitBotao(content, 6, 0, root)


def make_saldo(content, saldo):
    frame = Frame(content, height=20)
    frame.grid(row=7, column=0)

    saldo_label = Label(content, width=22, text="Saldo: ", anchor='w')
    saldo_label.grid(row=8, column=0, sticky=E)
    saldo_label.config(text="Saldo: {0}".format(saldo))
    return saldo_label


def criar_transacao(entries, lista_transacoes):
    descricao = entries['Descrição']
    valor = entries['Valor']
    descricao_value = descricao.get()
    valor_value = valor.get()
    if descricao_value and valor_value:
        valor_value = valor_value.replace(",", ".")
        valor_value = float(valor_value)

        transacao = Transacao(descricao_value, valor_value)
        extrato.append(transacao)
        lista_transacoes.insert('end', transacao.descricao +
                                " - R$ {0:0.2f}".format(transacao.valor))


def calcular_saldo(extrato, saldo_label):
    saldo = 0
    for transacao in extrato:
        saldo += transacao.valor
    saldo_string = "R$ {0:0.2f}".format(saldo)
    saldo_label.config(text="Saldo: " + saldo_string)


if __name__ == '__main__':
    root = Tk()
    root.title("Meu Banco")
    root.geometry("500x400")

    content = ttk.Frame(root, padding=(3, 3, 12, 12))
    content.grid(column=0, row=0, sticky=(N, W, E, S))

    ents = make_form(content)

    frame = Frame(content, width=40)
    frame.grid(row=0, rowspan=7, column=2, sticky=(N, W, E, S))

    l = Listbox(content, height=10)
    l.grid(column=4, row=0, rowspan=7, sticky=(N, W, E, S))
    s = ttk.Scrollbar(content, orient=VERTICAL, command=l.yview)
    s.grid(column=5, row=0, rowspan=7, sticky=(N, S))
    l['yscrollcommand'] = s.set

    for transacao in extrato:
        l.insert('end', transacao.descricao +
                 " - R$ {0:0.2f}".format(transacao.valor))


    root.bind('<Return>', (lambda e : criar_transacao(ents, l)))
    saldo_string = "?"
    saldo_label = make_saldo(content, saldo_string)

    make_options(content, ents, l, extrato, saldo_label)

    root.mainloop()
