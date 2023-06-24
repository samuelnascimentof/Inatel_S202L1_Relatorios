from Passageiro import Passageiro

class Voo:

    data: str
    duracao: int
    altMax: int
    numFotos: int
    equipamento: str
    passageiro: Passageiro

    def __init__ (self, data: str, duracao: int, altMax: int, numFotos: int, equipamento: str, passageiro: Passageiro):
        self.data = data
        self.duracao = duracao
        self.altMax = altMax
        self.numFotos = numFotos
        self.equipamento = equipamento
        self.passageiro = passageiro
        
    

