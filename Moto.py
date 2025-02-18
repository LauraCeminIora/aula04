from Veiculo import Veiculo

class Moto(Veiculo):
    def __init__(self, marca, modelo, placa, ano, cilindradas):
        super().__init__(marca, modelo, placa,ano) #super = invocar o metodo init da super classe
        self.__cilindradas = cilindradas
    #Sobrescrita do método __str__
    def __str__(self):
    #invoco o metodo __str__() da SUPERCLASSE veículo
    #armazeno o retorno na variável "retorno"
      retorno = super().__str__()
    #retorno com a concatenaçãi do valor da variável
    #"retorno" com as "__cilindradas"
      return f'''{retorno}
- Cilindradas: {self.__cilindradas}'''

