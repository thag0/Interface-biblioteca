class Livro:
    def __init__(self, titulo, autor, emprestado=None):
        self.titulo = titulo
        self.autor = autor

        if emprestado == None:
            self.emprestado = False
        else:
            self.emprestado = emprestado