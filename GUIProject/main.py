from tkinter import *
from users import Participante


fields = ('Nome', 'Login', 'Senha', 'Email', 'Endereco', 'Telefone')


def makeform(root, fields):
    entries = {}
    for field in fields:
        row = Frame(root)
        lab = Label(row, width=22, text=field+": ", anchor='w')
        ent = Entry(row)
        # ent.insert(0,"")
        row.pack(side = TOP, fill = X, padx = 5 , pady = 5)
        lab.pack(side = LEFT)
        ent.pack(side = RIGHT, expand = YES, fill = X)
        entries[field] = ent
    return entries


participantes = []


def createParticipante(entries):
    nome = entries['Nome']
    login = entries['Login']
    senha = entries['Senha']
    email = entries['Email']
    endereco = entries['Endereco']
    telefone = entries['Telefone']

    participante = Participante(nome, login, senha, email, endereco, telefone)
    participantes.append(participante)
    root.update()
    root.update_idletasks()


def deleteParticipante(participante):
    participantes.remove(participante)
    root.update()
    root.update_idletasks()
    pass



if __name__ == '__main__':
    root = Tk()
    ents = makeform(root, fields)
    # root.bind('<Return>', (lambda event, e = ents: fetch(e)))
    
    row = Frame(root)
    criar_button = Button(row, text = 'Criar Usuário',
        command=(lambda e = ents: createParticipante(e)))
    criar_button.pack(side = LEFT, padx = 5, pady = 5)
    quit_button = Button(row, text = 'Quit', command = root.quit)
    quit_button.pack(side = LEFT, padx = 5, pady = 5)
    row.pack(side = TOP, fill = X, padx = 5 , pady = 5)

    for participante in participantes:
        row = Frame(root)
        info = Label(row ,text = participante.nome)
        info.pack(side = LEFT, fill = X, padx = 5 , pady = 5)
        delete_button = Button(row, text = 'Delete', command = (lambda p = participante: deleteParticipante(p)))
        delete_button.pack(side = LEFT, padx = 5, pady = 5)
        row.pack(side = TOP, fill = X, padx = 5 , pady = 5)

    root.mainloop()