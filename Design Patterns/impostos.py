from abc import ABC, abstractmethod

class TemplateDeImpostoCondicional(ABC):
    
    def calcula(self, orcamento):
        if self.deve_usar_taxacao_maxima(orcamento):
            return self.taxacao_maxima(orcamento)
        else:
            return self.taxacao_minima(orcamento)
    
    @abstractmethod
    def deve_usar_taxacao_maxima(self, orcamento):
        pass
    
    @abstractmethod
    def taxacao_minima(self, orcamento):
        pass

    @abstractmethod
    def taxacao_maxima(self, orcamento):
        pass

class ISS(object):
    def calcula(self, orcamento):
        return orcamento.valor * 0.1

class ICMS(object):
    def calcula(self, orcamento):
        return orcamento.valor * 0.06

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