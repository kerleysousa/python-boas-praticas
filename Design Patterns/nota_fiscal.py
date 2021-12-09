from datetime import date

class Item(object):
    
    def __init__(self, descricao, valor):
        self.__descricao = descricao
        self.__valor = valor

    @property
    def descricao(self):
        return self.__descricao

    @property
    def valor(self):
        return self.__valor

class Nota_Fiscal(object):

    def __init__(self, razao_social, cnpj, itens, data_emissao=date.today(), detalhes=""):
        self.__razao_social = razao_social
        self.__cnpj = cnpj
        self.__data_emissao = data_emissao
        if len(detalhes) > 20:
            raise Exception("Detalhes da nota não pode ter mais do que 20 caracteres")
        self.__detalhes = detalhes
        self.__itens = itens

        self.__imprime()
        self.__envia_email()
        self.__salva_banco()
    
    @property
    def razao_social(self):
        return self.__razao_social

    @property
    def cnpj(self):
        return self.__cnpj

    @property
    def data_emissao(self):
        return self.__data_emissao

    @property
    def detalhes(self):
        return self.__detalhes

    def __imprime(self):
        print(f"Imprimindo nota fiscal - CNPJ: {self.cnpj}")

    def __envia_email(self):
        print(f"Enviando por email nota fiscal - CNPJ: {self.cnpj}")

    def __salva_banco(self):
        print(f"Salvando no banco de dados nota fiscal - CNPJ: {self.cnpj}")

if __name__ == "__main__":

    from criador_nota_fiscal import CriadorNotaFiscal

    itens = [
        Item("Item A", 100),
        Item("Item B", 200)
    ]

    nota_fiscal_com_builder = (CriadorNotaFiscal()
        .com_razao_social("Loja da esquina")
        .com_cnpj("12345678901234")
        .com_itens(itens)
        .constroi()
    )

    print(nota_fiscal_com_builder.cnpj)