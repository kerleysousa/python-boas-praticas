from abc import ABC, abstractmethod

class Imposto(ABC):

    def __init__(self, outro_imposto = None):
        self.__outro_imposto = outro_imposto

    def calcula_outro_imposto(self, orcamento):
        if self.__outro_imposto is None:
            return 0
        else:
            return self.__outro_imposto.calcula(orcamento)

    @abstractmethod
    def calcula(self, orcamento):
        pass

class TemplateDeImpostoCondicional(Imposto):
    
    def calcula(self, orcamento):
        if self.deve_usar_taxacao_maxima(orcamento):
            return self.taxacao_maxima(orcamento) + self.calcula_outro_imposto(orcamento)
        else:
            return self.taxacao_minima(orcamento) + self.calcula_outro_imposto(orcamento)
    
    @abstractmethod
    def deve_usar_taxacao_maxima(self, orcamento):
        pass
    
    @abstractmethod
    def taxacao_minima(self, orcamento):
        pass

    @abstractmethod
    def taxacao_maxima(self, orcamento):
        pass


def MAIS50(outra_funcao):
    def wrapper(self, orcamento):
        return outra_funcao(self, orcamento) + 50
    return wrapper


class ISS(Imposto):
    
    @MAIS50
    def calcula(self, orcamento):
        return orcamento.valor * 0.1 + self.calcula_outro_imposto(orcamento)

class ICMS(Imposto):
    def calcula(self, orcamento):
        return orcamento.valor * 0.06 + self.calcula_outro_imposto(orcamento)

class ICPP(TemplateDeImpostoCondicional):

    def deve_usar_taxacao_maxima(self, orcamento):
        return orcamento.valor > 500
    
    def taxacao_minima(self, orcamento):
        return orcamento.valor * 0.05

    def taxacao_maxima(self, orcamento):
        return orcamento.valor * 0.07

class IKCV(TemplateDeImpostoCondicional):

    def deve_usar_taxacao_maxima(self, orcamento):
        return orcamento.valor > 500 and self.__tem_item_maior_que_100_reais(orcamento)
    
    def taxacao_minima(self, orcamento):
        return orcamento.valor * 0.06

    def taxacao_maxima(self, orcamento):
        return orcamento.valor * 0.1

    def __tem_item_maior_que_100_reais(self, orcamento):
        for item in orcamento.obter_itens():
            if item.valor > 100:
                return True
        return False