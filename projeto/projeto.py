import tkinter as tk
from tkinter import *
import tkinter.messagebox as messagebox

#def __init__(self,
#             screenName: str | None = None,
#             baseName: str | None = None,
#             className: str = "Tk",
#             useTk: bool = True,
#             sync: bool = False,
#             use: str | None = None) -> None:

def usuarioID():
    with open("id.txt", 'r') as file:
        pre_id = file.read()
    new_id = "USR" + str(int(pre_id[3:]) + 1)
    with open("id.txt", 'w') as file:
        file.write(new_id)
    return new_id

def salva():
    infoID = usuarioID()
    infoNome = campoNome.get()
    infoEmail = campoEmail.get()
    infoIdade = campoIdade.get()
    infoSexo = campoSexo.get()
    infoTelefone = campoTelefone.get()
    infoCidade = campoCidade.get()

    # Exibe os dados na tela do terminal
    print("ID: " + infoID + "\n")
    print("Nome: " + infoNome + "\n")
    print("Email: " + infoEmail + "\n")
    print("Idade: " + str(infoIdade) + "\n")
    print("Sexo: " + infoSexo)
    print("Telefone: " + infoTelefone + "\n")
    print("Cidade: " + infoCidade + "\n")
    print("Dados salvos com sucesso!")

    # Cria o arquivo de texto no PC
    arquivo = open("dados.txt", "a")
    arquivo.write("ID: " + infoID + "\n")
    arquivo.write("Nome: " + infoNome + "\n")
    arquivo.write("Email: " + infoEmail + "\n")
    arquivo.write("Idade: " + str(infoIdade) + "\n")
    arquivo.write("Sexo: " + infoSexo + "\n")
    arquivo.write("Telefone: " + infoTelefone + "\n")
    arquivo.write("Cidade: " + infoCidade + "\n")
    arquivo.write("Dados salvos com sucesso! \n")
    arquivo.write("-------------------------------------------------- \n")
    arquivo.close()

    # Exibe os dados que foram salvos no txt em uma caixa de diálogo
    tk.messagebox.showinfo(
        "Dados salvos com sucesso!")
    txtNome.delete(0, END)
    txtEmail.delete(0, END)
    txtIdade.delete(0, END)
    txtTelefone.delete(0, END)
    txtCidade.delete(0, END)
    txtSexo.opcoesSexo[0]
    
def cancela():
    janela.quit()

# Variáveis da janela
geometria = "300x300"
titulo = "FORMULÁRIO"

# Cria a janela principal
janela = Tk()
janela.geometry(geometria)
janela.title(titulo)

campoNome = StringVar()
campoEmail = StringVar()
campoIdade = IntVar()
opcoesSexo = ["-----", "Masculino", "Feminino", "Outros"]
campoSexo = StringVar()
campoTelefone = StringVar()
campoCidade = StringVar()

# Cria e posiciona os widgets da tela
texto = Label(janela, text="Cadastro de Usuário", font="Arial 20 bold", bg="green4", fg="azure", height="2", width="300")
texto.grid(row=0, column=0)
texto.pack()

nome = Label(janela, text="Nome:")
nome.place(x=15, y=80)
txtNome = Entry(janela, textvariable=campoNome, width=35)
txtNome.place(x=60, y=80)

email = Label(janela, text="Email:")
email.place(x=15, y=110)
txtEmail = Entry(janela, textvariable=campoEmail, width=35)
txtEmail.place(x=60, y=110)

idade = Label(janela, text="Idade:")
idade.place(x=15, y=140)
txtIdade = Entry(janela, textvariable=campoIdade, width=5)
txtIdade.place(x=60, y=140)

sexo = Label(janela, text="Sexo:")
sexo.place(x=145, y=140)
txtSexo = OptionMenu(janela, campoSexo, *opcoesSexo)
txtSexo.place(x=180, y=135)

telefone = Label(janela, text="Phone:")
telefone.place(x=15, y=170)
txtTelefone = Entry(janela, textvariable=campoTelefone, width=35)
txtTelefone.place(x=60, y=170)

cidade = Label(janela, text="Cidade:")
cidade.place(x=15, y=200)
txtCidade = Entry(janela, textvariable=campoCidade, width=35)
txtCidade.place(x=60, y=200)

ok = Button(janela, text="Salvar", width=15, height=2, command=salva)
ok.place(x=15, y=240)

cancelar = Button(janela, text="Cancelar", width=15, height=2, command=cancela)
cancelar.place(x=160, y=240)

# Inicia o loop principal da aplicação
janela.mainloop()
