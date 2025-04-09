
from tkinter import Tk, Button, Label, Entry, Frame, messagebox
from FilmeController import FilmeController


class FilmeView(Tk):
    def __init__(self):
        fonte = ('Arial', 18)
        super().__init__()

        Label(self, text='Cadastro de Filmes', font=('', 30)).pack()

        Label(self, text='Código').pack()
        self.codigo = Entry(self, font=fonte)
        self.codigo.pack()

        Label(self, text='Nome').pack()
        self.nome = Entry(self, font=fonte)
        self.nome.pack()

        Label(self, text='Quantidade Disponivel').pack()
        self.disponivel = Entry(self, font=fonte)
        self.disponivel.pack()

        Button(self, font=fonte, text='Salvar', command=self.salvar).pack()

    def salvar(self):
        controller = FilmeController(self)

        if controller.inserir():
            messagebox.showinfo('Sucesso!', 'Salvo com sucesso!')
        else:
            messagebox.showerror('Erro!', 'Houve um erro ao salvar os dados!')


if __name__ == "__main__":
    jan = FilmeView()
    jan.title('Cadastro de Filmes')
    jan.resizable(0, 0)
    jan.mainloop()
