from abc import ABC, abstractclassmethod

class EstadoDeUmOrcamento(ABC):
    
    @abstractclassmethod
    def aplica_desconto_extra(self, orcamento):
        pass
    
    @abstractclassmethod
    def aprova(self, orcamento):
        pass

    @abstractclassmethod
    def reprova(self, orcamento):
        pass

    @abstractclassmethod
    def finaliza(self, orcamento):
        pass

class EmAprovacao(EstadoDeUmOrcamento):
    def aplica_desconto_extra(self, orcamento):
        orcamento.adiciona_desconto_extra(orcamento.valor * 0.02)

    def aprova(self, orcamento):
        orcamento.estado_atual = Aprovado()

    def reprova(self, orcamento):
        orcamento.estado_atual = Reprovado()

    def finaliza(self, orcamento):
        raise Exception("Estado em aprovação não pode ir para finalizado.")

class Aprovado(EstadoDeUmOrcamento):
    def aplica_desconto_extra(self, orcamento):
        orcamento.adiciona_desconto_extra(orcamento.valor * 0.05)

    def aprova(self, orcamento):
        raise Exception("Orcamento aprovado não pode ser aprovado novamente.")

    def reprova(self, orcamento):
        raise Exception("Não é possível reprovar um orçamento aprovado")

    def finaliza(self, orcamento):
        orcamento.estado_atual = Finalizado()
    
class Reprovado(EstadoDeUmOrcamento):
    def aplica_desconto_extra(self, orcamento):
        raise Exception("Orçamentos reprovados não recebem desconto extra.")

    def aprova(self, orcamento):
        raise Exception("Não é possível aprovar um orçamento reprovado")

    def reprova(self, orcamento):
        raise Exception("Orcamento reprovado não pode ser reprovado novamento.")

    def finaliza(self, orcamento):
        orcamento.estado_atual = Finalizado()

class Finalizado(EstadoDeUmOrcamento):
    def aplica_desconto_extra(self, orcamento):
        raise Exception("Orçamentos reprovados não recebem desconto extra.")

    def aprova(self, orcamento):
        raise Exception("Orcamento está finalizado.")

    def reprova(self, orcamento):
        raise Exception("Orcamento está finalizado.")

    def finaliza(self, orcamento):
        raise Exception("Orcamento finalizado não pode ser finalizado novamente.")

class Orcamento(object):

    def __init__(self):
        self.__itens = []
        self.estado_atual = EmAprovacao()
        self.__desconto_extra = 0

    def aprova(self):
        self.estado_atual.aprova(orcamento)

    def reprova(self):
        self.estado_atual.reprova(orcamento)

    def finaliza(self):
        self.estado_atual.finaliza(orcamento)

    def aplica_desconto_extra(self):
        self.estado_atual.aplica_desconto_extra(self)

    def adiciona_desconto_extra(self, desconto):
        self.__desconto_extra += desconto

    @property
    def valor(self):
        total = 0.0
        for item in self.__itens:
            total += item.valor
        return total - self.__desconto_extra
    
    def obter_itens(self):
        return tuple(self.__itens)

    @property
    def total_itens(self):
        return len(self.__itens)

    def adiciona_itens(self, item):
        self.__itens.append(item)

class Item(object):

    def __init__(self, nome, valor):
        self.__nome = nome
        self.__valor = valor
    
    @property
    def nome(self):
        return self.__nome

    @property
    def valor(self):
        return self.__valor
    

if __name__ == "__main__":

    orcamento = Orcamento()
    orcamento.adiciona_itens(Item("Item 1", 100))
    orcamento.adiciona_itens(Item("Item 2", 200))
    orcamento.adiciona_itens(Item("Item 3", 300))

    print(orcamento.valor)
    orcamento.aprova()
    orcamento.reprova()