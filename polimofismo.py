class Mamifero:
    def emitir_som(self):
        pass

class Cachorro(Mamifero):
    def emitir_som(self):
        print("Latiu")

class Gato(Mamifero):
    def emitir_som(self):
        print("miou")

class Rato(Mamifero):
    def emitir_som(self):
        print("não sei o som do rato")

cachorro = Cachorro()
gato = Gato()
rato = Rato()

mamiferos = [cachorro, gato, rato]

for mamifero in mamiferos:
    mamifero.emitir_som()