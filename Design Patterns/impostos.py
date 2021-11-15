from abc import ABC, abstractmethod

class TemplateDeImpostoCondicional(ABC):
    
    def calcula(self, orcamento):
        if self.deve_usar_taxacao_maxima(orcamento):
            return self.maxima_taxacao(orcamento)
        else:
            return self.minima_taxacao(orcamento)
    
    @abstractmethod
    def deve_usar_taxacao_maxima(orcamento):
        pass
    
    @abstractmethod
    def taxacao_minima(orcamento):
        pass

    @abstractmethod
    def taxacao_maxima(orcamento):
        pass

class ISS(object):
    def calcula(self, orcamento):
        return orcamento.valor * 0.1

class ICMS(object):
    def calcula(self, orcamento):
        return orcamento.valor * 0.06

class ICPP(TemplateDeImpostoCondicional):
    def calcula(self, orcamento):
        if orcamento.valor > 500:
            return orcamento.valor * 0.07
        else:
            return orcamento.valor * 0.05

class IKCV(TemplateDeImpostoCondicional):
    def calcula(self, orcamento):
        if orcamento.valor > 500 and self.__tem_item_maior_que_100_reais(orcamento):
            return orcamento.valor * 0.1
        else:
            return orcamento.valor * 0.06

    def __tem_item_maior_que_100_reais(self, orcamento):
        for item in orcamento.obter_itens():
            if item.valor > 100:
                return True
        return False