class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.livros = []

    def identificar(self):
        print(f'Sou {self.nome} e tenho {self.idade} anos')

    def pegarLivro(self, livro):
        self.livros.append(livro)


    def devolverLivro(self, livro):
        indice = 0
        for indice in range(len(self.livros)):
            if (self.livros[indice] == livro):
                break

        self.livros.pop(indice)


    def livrosPegos(self, label):
        labelLivros = ''
        if(len(self.livros)==0):
            label.set(f'\n{self.nome} não possui nenhum livro')
            return

        cont = 0
        for cont in range (len(self.livros)):
            labelLivros += (f'{cont}-{self.livros[cont].titulo}\n')
        label.set(labelLivros)