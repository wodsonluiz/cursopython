class Impressora:
    
    @staticmethod
    def ligar_para_suporte():
        print("liguei para o suporte")

    @classmethod
    def deu_problema_na_impressora(cls):
        print("analisando o problema")
        cls.ligar_para_suporte()

    #meto de instancia chamando um metodo estatico
    def imprimir(self):
        print("imprimindo pagina 1")
        self.ligar_para_suporte()

Impressora.ligar_para_suporte()

Impressora.deu_problema_na_impressora()

impressora = Impressora()
impressora.imprimir()