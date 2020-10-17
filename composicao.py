class Cliente:
    def __init__(self, nome, documento):
        self.nome = nome
        self.documento = documento

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

class CarrinhoCompras:
    def __init__(self, cliente, produtos):
        self.num_pedido = '123' 
        self.produtos = produtos
        self.cliente = cliente

    @property
    def valor_carrinho(self):
        total = 0.0
        for produto in self.produtos:
            total += produto.preco

        return total

    def adicionar_produto(self, produto):
        self.produtos.append(produto)

    def remover_produto(self, produto):
        self.produtos.remove(produto)

    def fechar_carrinho(self):
        print(f"Fechando o pedido {self.num_pedido}")
        print(f"Valor do carrinho: {self.valor_carrinho}")
        print(f"Nome cliente: {self.cliente.nome}")
        print("Obrigado pela compra")

cliente = Cliente("Wodson", "1234567")

maquina_cafe = Produto("Maquina", 89.90)
maquina_cafe2 = Produto("Maquina2", 89.90)
maquina_cafe3 = Produto("Maquina3", 89.90)

produtosComprados = [maquina_cafe, maquina_cafe2]

carrinho = CarrinhoCompras(cliente, produtosComprados)
carrinho.adicionar_produto(maquina_cafe3)
carrinho.remover_produto(maquina_cafe2)

print(carrinho.valor_carrinho)

