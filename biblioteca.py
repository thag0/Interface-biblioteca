from tkinter import Label
from livro import Livro

class Biblioteca:
    # _abreCorAmarelo = '\033[1;33m'
    # _abreCorVerm= '\033[1;31m'
    # _abreCorAzul = '\033[1;34m'
    # _fechaCor = '\033[m'
    __capacidade = 10
    _total = 0


    def adicionarLivro(self, biblioteca:list, tituloLivro:str, autorLivro:str, label):
        if(self._total > self.__capacidade):
           label.set('A biblioteca está cheia')
           return

        l1 = Livro(tituloLivro, autorLivro)
        biblioteca.append(l1)
        self._total += 1
        label.set(f'Livro {l1.titulo} de {l1.autor} adicionado!\n')


    def removerLivro(self, biblioteca, indice, label):


        if(self._bibliotecaVazia(biblioteca)):
            label.set("A biblioteca está vazia")
            return

        if(self._verificarDisponibilidade(biblioteca, False) == False):
            label.set('Nenhum livro disponível para remoção')
            return
     
        texto = 'A biblioteca possui os seguintes livros:\n'
        contador = 0
        for contador in range (len(biblioteca)):
            if(biblioteca[contador].emprestado == False):
                texto += (f'{contador} - {biblioteca[contador].titulo}\n')


        if(indice > (len(biblioteca)-1)or(indice < 0)):
            label.set(f'Indice Inválido')
            return

        if(biblioteca[indice].emprestado == False):
            label.set(f'Livro {biblioteca[indice].titulo} removido!\n')
            biblioteca.pop(indice)
        else:
            label.set(f'Indice Inválido')
            return


    def emprestarLivro(self, biblioteca, pessoa, indice, label):
        
        #Verificar se a biblioteca possui livros e se os que tem estão disponiveis
        if(self._bibliotecaVazia(biblioteca)):
            label.set('\nA biblioteca está vazia')
            return

        if(self._verificarDisponibilidade(biblioteca, False) == False):
            label.set('\nNenhum livro disponível no momento')
            return

        textoDisplay = 'Livros disponíveis para emprestar\n'
        for c in range (len(biblioteca)):
            if(biblioteca[c].emprestado == False):
                textoDisplay += (f'{c} - {biblioteca[c].titulo}\n')
        label.set(textoDisplay)

        #Verificar se o indice é valido
        if((indice<0)or(indice>len(biblioteca)-1)):
            label.set(f'\nIndice Inválido')
            return
        
        if(biblioteca[indice].emprestado == False):
            biblioteca[indice].emprestado = True
            
            #Anotar quem pegou o livro
            self._quemPegouLivro(biblioteca[indice], pessoa)
            label.set(f'Livro {biblioteca[indice].titulo} foi emprestado por {pessoa.nome}')
        else:
            label.set(f'Indice Inválido')
            return


    def devolverLivro(self, biblioteca, pessoa, indice, label):
        
        #Verificar se a biblioteca possui livros e se os que tem estão disponiveis
        if(self._bibliotecaVazia(biblioteca)):
            label.set('A biblioteca está vazia')
            return

        if(self._verificarDisponibilidade(biblioteca, True) == False):
            label.set('Nenhum livro emprestado no momento')
            return

        texto = ''
        for c in range (len(biblioteca)):
            if(biblioteca[c].emprestado == True):
                texto += (f'{c} - {biblioteca[c].titulo}\n')


        #Verificar se o indice é valido
        if((indice<0)or(indice>len(biblioteca)-1)):
            label.set(f'Indice Inválido')
            return
        
        if(biblioteca[indice].emprestado == True):
            biblioteca[indice].emprestado = False
            #Verificar quem devolveu
            self._quemDevolveuLivro(biblioteca[indice], pessoa)
            label.set(f'{biblioteca[indice].titulo} foi devolvido por {pessoa.nome}')
        else:
            label.set(f'Indice Inválido')
            return
        
    #terminado 100%
    def listarEmprestados(self, biblioteca, textoDisplay):
        textoFinal = ''

        if(self._bibliotecaVazia(biblioteca)):
            textoDisplay.set('Biblioteca vazia')
            return

        if(self._verificarDisponibilidade(biblioteca, True) == False):
            textoDisplay.set('Sem livros emprestados')
            return

        textoDisplay.set('Livros emprestados foram') 
        contador = 0
        for contador in range (len(biblioteca)):
            if(biblioteca[contador].emprestado == True):
               textoFinal += (f'{contador} - {biblioteca[contador].titulo}\n')   
        textoDisplay.set(textoFinal)

    #terminado 100%
    def listarDisponiveis(self, biblioteca, textoDisplay):
        textoFinal = ''

        if(self._bibliotecaVazia(biblioteca)):
            textoDisplay.set('Biblioteca vazia')
            return
        
        if(self._verificarDisponibilidade(biblioteca, False) == False):
            textoDisplay.set('Sem livros disponiveis')
            return

        textoDisplay.set('Livros na biblioteca') 
        contador = 0
        for contador in range (len(biblioteca)):
            if(biblioteca[contador].emprestado == False):
               textoFinal += (f'{contador} - {biblioteca[contador].titulo}\n')

        textoDisplay.set(textoFinal)


    @classmethod
    def _bibliotecaVazia(cls, biblioteca)->bool:
        if(len(biblioteca) == 0):
            return True
        else:
            return False


    @classmethod
    def _verificarDisponibilidade(cls, biblioteca, estado)->bool:
        status = 0
        for contador in range (len(biblioteca)):
            if(biblioteca[contador].emprestado == estado):
                status += 1
        
        if(status == 0):
            return False
        else:
            return True


    @classmethod
    def _quemPegouLivro(cls, livro, pessoa):
        pessoa.pegarLivro(livro)

    
    @classmethod
    def _quemDevolveuLivro(cls, livro, pessoa):
        #pegar o indice do livro dentro da pessoa pra devolver
        indice = 0
        for indice in range(len(pessoa.livros)):
            if(pessoa.livros[indice] == livro):
                break

        pessoa.devolverLivro(livro)