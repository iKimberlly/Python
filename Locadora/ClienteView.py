
from tkinter import Tk, Button, Label, Entry, Frame, messagebox
from ClienteController import ClienteController


class ClienteView(Tk):
    def __init__(self):
        fonte = ('Arial', 18)
        super().__init__()

        Label(self, text='Cadastro de Cliente', font=('', 30)).pack()

        Label(self, text='Matricula').pack()
        self.matricula = Entry(self, font=fonte)
        self.matricula.pack()

        Label(self, text='Nome').pack()
        self.nome = Entry(self, font=fonte)
        self.nome.pack()

        Label(self, text='Contato').pack()
        self.contato = Entry(self, font=fonte)
        self.contato.pack()

        Button(self, font=fonte, text='Salvar', command=self.salvar).pack()

    def salvar(self):
        controller = ClienteController(self)

        if controller.inserir():
            messagebox.showinfo('Sucesso!', 'Salvo com sucesso!')
        else:
            messagebox.showerror('Erro!', 'Houve um erro ao salvar os dados!')


if __name__ == "__main__":
    jan = ClienteView()
    jan.title('Cadastro de Cliente')
    jan.resizable(0, 0)
    jan.mainloop()
