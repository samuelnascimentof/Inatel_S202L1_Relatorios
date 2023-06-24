from Voo import Voo
from typing import List

class Piloto:

    nome: str
    telefone: int
    cpf: int
    voos: Voo = []
    numVoos: int

    def __init__ (self, nome: str, telefone: int, cpf: int, voos: List[Voo]):
        self.nome = nome
        self.telefone = telefone
        self.cpf = cpf
        self.voos = voos
        self.numVoos = len(voos)

    def addVoo(self, voo: Voo):
        self.voos.append(voo)

