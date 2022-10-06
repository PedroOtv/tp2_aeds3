#from entidade import Entidade
from Produto import Produto

class VetorProduto(Produto):
    def__init__(self):
        self.Produtos = []

    def addProduto(self, Produto):
        self.Produtos.append(Produto)
    
    def buscarProdutoNome(self, nome)
        for p in self.Produtos:
            if nome == p.nome:
                print("Produto encontrado\n")
                p.indentificacao()
                return p
        print("Produto não encontrado\n")
        return NONE

    def listaProdutos(self):
        for p in self.Produtos:
            p.indentificacao()


    def removerProduto(self, Produto, quantidadeVendida):
        p = buscarProdutoNome(Produto)
        p.quantidade = p.quantidade - quantidadeVendida

    