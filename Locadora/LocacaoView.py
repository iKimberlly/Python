from tkinter import Tk, Button, Label, Entry, messagebox
from LocacaoController import LocacaoController

class LocacaoView(Tk):
    def __init__(self):
        fonte = ('Arial', 18)
        super().__init__()

        Label(self, text='Locação de Filmes', font=('', 30)).pack()

        Label(self, text='ID DA LOCAÇÃO').pack()
        self.codigo = Entry(self, font=fonte)  
        self.codigo.pack()

        Label(self, text='Nome do cliente').pack()
        self.nome = Entry(self, font=fonte)
        self.nome.pack()

        Label(self, text='Matricula do filme:').pack()
        self.matricula = Entry(self, font=fonte)  
        self.matricula.pack()

        Label(self, text='Filme:').pack()
        self.filme = Entry(self, font=fonte)
        self.filme.pack()

        Label(self, text='Data da locação:').pack()
        self.data_locacao = Entry(self, font=fonte)
        self.data_locacao.pack()

        Label(self, text='Data de entrega:').pack()
        self.data_devolucao = Entry(self, font=fonte)
        self.data_devolucao.pack()

        Button(self, font=fonte, text='Salvar', command=self.salvar).pack()

    def salvar(self):
        controller = LocacaoController(self)

        if controller.inserir():
            messagebox.showinfo('Sucesso!', 'Salvo com sucesso!')
        else:
            messagebox.showerror('Erro!', 'Houve um erro ao salvar os dados!')

if __name__ == "__main__":
    jan = LocacaoView()
    jan.title('Locação de Filmes')
    jan.resizable(0, 0)
    jan.mainloop()
