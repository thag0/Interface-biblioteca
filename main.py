import tkinter as tk
from pessoa import Pessoa
from biblioteca import Biblioteca
from livro import Livro 


def acao_botao_menu():
    interacoes(0, ent_entrada_interacao, btn_acoes_interacao)
    indice = var_menu.get()
    texto_lb_saida.set('')
    
    if(indice == 0):
        texto_lb_log.set('Selecione uma opção')

    
    if(indice == 1):
        texto_lb_log.set('Digite o título')
        interacoes(1, ent_entrada_interacao, btn_acoes_interacao, 'Adicionar')
        
        
    if(indice == 2):
        texto_lb_log.set('Qual livro remover')
        bib.listarDisponiveis(biblioteca, texto_lb_saida)
        interacoes(1, ent_entrada_interacao, btn_acoes_interacao, 'Remover')

    
    if(indice == 3):
        texto_lb_log.set('Pegando livro')
        bib.listarDisponiveis(biblioteca, texto_lb_saida)
        interacoes(1, ent_entrada_interacao, btn_acoes_interacao, 'Emprestar')

    
    if(indice == 4):
        texto_lb_log.set('Devolvendo livro')
        bib.listarEmprestados(biblioteca, texto_lb_saida)
        interacoes(1, ent_entrada_interacao, btn_acoes_interacao, 'Devolver')
        

    if(indice == 5):
        texto_lb_log.set('Livros emprestados')
        bib.listarEmprestados(biblioteca, texto_lb_saida)


    if(indice == 6):
        texto_lb_log.set('Livros disponíveis')
        bib.listarDisponiveis(biblioteca, texto_lb_saida)


    if(indice == 7):
        texto_lb_log.set(f'Livros de {pessoa.nome}')
        pessoa.livrosPegos(texto_lb_saida)



def acao_botao_interacoes():
    indice_menu = var_menu.get()
    valor_entrada = 0

    global titulo
    global autor 

    global digitou_titulo
    global digitou_autor


    #A parte de adicionar ta bugada

    if((indice_menu == 1)&(digitou_titulo == False)):
        titulo = str(ent_entrada_interacao.get())
        digitou_titulo = True
        texto_lb_log.set('Digite o autor')
        var_ent_interacoes.set('')


    elif((indice_menu == 1)&(digitou_autor == False)):
        autor = str(ent_entrada_interacao.get())
        digitou_autor = True             


    if((indice_menu == 1)&(digitou_titulo == True)&(digitou_autor == True)):    
        bib.adicionarLivro(biblioteca, titulo, autor, texto_lb_saida)
        digitou_titulo = False
        digitou_autor = False
        interacoes(0, ent_entrada_interacao, btn_acoes_interacao)



    if(indice_menu == 2): 
        valor_entrada = int(ent_entrada_interacao.get())
        bib.removerLivro(biblioteca, valor_entrada, texto_lb_saida)
        interacoes(0, ent_entrada_interacao, btn_acoes_interacao)


    if(indice_menu == 3):
        valor_entrada = int(ent_entrada_interacao.get())
        bib.emprestarLivro(biblioteca, pessoa, valor_entrada, texto_lb_saida)
        interacoes(0, ent_entrada_interacao, btn_acoes_interacao)

    if(indice_menu == 4):
        valor_entrada = int(ent_entrada_interacao.get())
        bib.devolverLivro(biblioteca, pessoa, valor_entrada, texto_lb_saida)
        interacoes(0, ent_entrada_interacao, btn_acoes_interacao)



def interacoes(indice, entrada, botao, texto=None):
    if texto is None:
        texto = '\t'

    if(indice == 1):
        entrada['state'] = 'normal'
        entrada['bg'] = cor_apertar_botao
        botao['state'] = 'normal'
        botao['text'] = texto
        botao['relief'] = 'raised'

    if(indice == 0):
        entrada['state'] = 'disabled'
        botao['state'] = 'disabled'       
        botao['text'] = texto
        botao['relief'] = 'groove'
        var_ent_interacoes.set('')



#Main
pessoa = Pessoa('Thiago', 21)
bib = Biblioteca()
biblioteca = []

l1 = Livro('Livro1', 'autor')
l2 = Livro('Livro2', 'autor', True)
l3 = Livro('Livro3', 'autor')
biblioteca.append(l1)
biblioteca.append(l2)
biblioteca.append(l3)
pessoa.pegarLivro(l2)
bib._total = 3

#Criando a interface grafica
janela = tk.Tk()
janela.title('Biblioteca')
janela.iconbitmap('icones/livros_icon.ico')
janela.resizable(width=0, height=0)
janela.config(padx=5, pady=5)


#personalizacao
cor_fundo = '#846547' #'#69422B'
cor_apertar_botao = '#CC9965'
cor_fonte = 'white'
rbtn_cor = cor_fundo
cor_menu = 'grey25'
janela['bg'] = cor_fundo

var_menu = tk.IntVar()
texto_lb_saida = tk.StringVar()
texto_lb_log = tk.StringVar()

var_ent_interacoes = tk.StringVar()

digitou_titulo = False
digitou_autor = False
titulo = ''
autor = ''

menu_1 = tk.Radiobutton(janela, variable=var_menu, bg=cor_fundo, fg=cor_fonte, selectcolor=cor_menu, text='Adicionar livro', value=1, activebackground=rbtn_cor)
menu_2 = tk.Radiobutton(janela, variable=var_menu, bg=cor_fundo, fg=cor_fonte, selectcolor=cor_menu, text='Remover livro', value=2, activebackground=rbtn_cor)
menu_3 = tk.Radiobutton(janela, variable=var_menu, bg=cor_fundo, fg=cor_fonte, selectcolor=cor_menu, text='Emprestar Livro', value=3, activebackground=rbtn_cor)
menu_4 = tk.Radiobutton(janela, variable=var_menu, bg=cor_fundo, fg=cor_fonte, selectcolor=cor_menu, text='Devolver Livro', value=4, activebackground=rbtn_cor)
menu_5 = tk.Radiobutton(janela, variable=var_menu, bg=cor_fundo, fg=cor_fonte, selectcolor=cor_menu, text='Lista de emprestados', value=5, activebackground=rbtn_cor)
menu_6 = tk.Radiobutton(janela, variable=var_menu, bg=cor_fundo, fg=cor_fonte, selectcolor=cor_menu, text='Lista de disponíveis', value=6, activebackground=rbtn_cor)
menu_7 = tk.Radiobutton(janela, variable=var_menu, bg=cor_fundo, fg=cor_fonte, selectcolor=cor_menu, text='Meus Livros', value=7, activebackground=rbtn_cor)

btn_confirmar = tk.Button(janela, text='Confirmar', bg=cor_fundo, fg=cor_fonte, command=acao_botao_menu, activebackground=cor_apertar_botao)
lb_log = tk.Label(janela, textvariable=texto_lb_log, bg=cor_fundo, fg=cor_fonte,)

#area de interação
ent_entrada_interacao = tk.Entry(janela, textvariable=var_ent_interacoes, state='disabled', justify='center', relief='raised')
btn_acoes_interacao = tk.Button(janela, text='\t', command=acao_botao_interacoes, state='disabled', bg=cor_fundo, fg=cor_fonte, activebackground=cor_apertar_botao, relief='groove')

lb_saida = tk.Label(janela, textvariable=texto_lb_saida, bg=cor_fundo, fg=cor_fonte)

#Adicionando os widgtes no canto direito
menu_1.grid(row=0, column=0, sticky='w')
menu_2.grid(row=1, column=0, sticky='w')
menu_3.grid(row=2, column=0, sticky='w')
menu_4.grid(row=3, column=0, sticky='w')
menu_5.grid(row=4, column=0, sticky='w')
menu_6.grid(row=5, column=0, sticky='w')
menu_7.grid(row=6, column=0, sticky='w')

btn_confirmar.grid(row=7, column=0, pady=10, sticky='news')
lb_log.grid(row=8, column=0,sticky='news')

ent_entrada_interacao.grid(row=9, column=0, sticky='news')
btn_acoes_interacao.grid(row=9, column=1, padx=5,sticky='news')


lb_saida.grid(row=0, column=2, rowspan=14, padx=5, pady=5, sticky='news')
lb_saida.config(wraplength=150)


janela.mainloop()