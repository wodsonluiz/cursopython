class Impressora:

    #metodos de classe não tem acesso aos objetos que está no escopo da classe [self.a = 10]
    def __init__(self):
        self.a = 10

    @classmethod
    def imprimir_folha(cls):
        print("folha impressa")
    
    @classmethod
    def imprimir_livro(cls, paginas):
        for i in range(paginas):
            cls.imprimir_folha()

Impressora.imprimir_folha()

Impressora.imprimir_livro(5)

impressora = Impressora()

impressora.imprimir_folha()
