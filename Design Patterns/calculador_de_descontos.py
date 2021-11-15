from descontos import *

class CalculadorDeDescontos(object):

    def calcula(self, orcamento):

        desconto = DescontoPorCincoItens(
            DescontoPorQuinhentosReais(
                SemDesconto()
            )
        )

        return desconto.calcula(orcamento)

if __name__ == "__main__":

    from orcamento import Orcamento, Item

    orcamento = Orcamento()
    orcamento.adiciona_itens(Item("Item 1", 100))
    orcamento.adiciona_itens(Item("Item 2", 50))
    orcamento.adiciona_itens(Item("Item 3", 400))

    print(orcamento.valor)

    calculador = CalculadorDeDescontos()
    desconto = calculador.calcula(orcamento)

    print(desconto)
