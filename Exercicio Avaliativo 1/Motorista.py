from Corrida import Corrida
from typing import List

class Motorista:

    corridas: Corrida = []
    nota: int = None

    def __init__ (self, corridas: List[Corrida], nota: int):
        self.corridas = corridas
        self.nota = nota

    def addCorrida(self, corrida: Corrida):
        self.corridas.append(corrida)

