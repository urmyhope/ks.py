class Veiculo:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def ligar(self):
        print("Veiculo ligado")

    def desligar(self):
        print("Veiculo desligado")

class Carro(Veiculo):
    def __init__ (self,marca,modelo, ano, numerodePortas):
        super().__init__(marca,modelo,ano)
        self.numerodePortas = numerodePortas

class Moto(Veiculo):
    def __init__(self, marca, modelo, ano, cilindradas):
        super().__init__(marca, modelo, ano)
        self.cilindradas = cilindradas


Carro1 = Carro("Porsche", "Cayenne", 2021, 5)
print(Carro1.marca)

Moto1 = Moto("Honda","Hornet", 2001, 600)
print(Moto1.cilindradas)
