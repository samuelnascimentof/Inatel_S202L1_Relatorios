from PilotoDAO import PilotoDAO
from Piloto import Piloto
from Voo import Voo
from Passageiro import Passageiro
import pprint

class SimpleCLI:
    def __init__(self):
        self.commands = {}

    def add_command(self, name, function):
        self.commands[name] = function

    def run(self):
        while True:
            command = input("Enter a command: ")
            if command == "quit":
                print("Goodbye!")
                break
            elif command in self.commands:
                self.commands[command]()
            else:
                print("Invalid command. Try again.")

class PilotoCLI(SimpleCLI):
    def __init__ (self):
        super().__init__()
        self.pilotoDAO = PilotoDAO()
        self.add_command("create", self.create_piloto)
        self.add_command("read", self.read_piloto)
        self.add_command("readAll", self.read_all_piloto)
        self.add_command("update", self.update_piloto)
        self.add_command("delete", self.delete_piloto)

    def create_piloto(self):
        voos: Voo = []

        nome = input("Informe o nome do piloto: ")
        telefone = int(input("Informe o telefone do piloto: "))
        cpf = int(input("Informe o CPF do piloto: "))

        nomePassageiro = input("Informe o nome do passageiro: ")
        telefonePassageiro = input("Informe o telefone do passageiro: ")
        cpfPassageiro = input("Informe o CPF do passageiro: ")
        passageiro = Passageiro(nomePassageiro, telefonePassageiro, cpfPassageiro)

        dataVoo = input("Informe a data do voo: ")
        duracaoVoo = int(input("Informe a duração do voo em minutos: "))
        altMaxVoo = int(input("Informe a altitude máxima atingida no voo em relação ao nível do mar: "))
        numFotosVoo = int(input("Informe o número de fotos tiradas durante o voo: "))
        equipamentoVoo = input("Informe o equipamento utilizado no voo: ")
        voo = Voo(dataVoo, duracaoVoo, altMaxVoo, numFotosVoo, equipamentoVoo, passageiro)
        voos.append(voo)

        while input("Deseja adicionar mais um voo? (s/n): ") == "s":
            nomePassageiro = input("Informe o nome do passageiro: ")
            telefonePassageiro = input("Informe o telefone do passageiro: ")
            cpfPassageiro = input("Informe o CPF do passageiro: ")
            passageiro = Passageiro(nomePassageiro, telefonePassageiro, cpfPassageiro)

            dataVoo = input("Informe a data do voo: ")
            duracaoVoo = int(input("Informe a duração do voo em minutos: "))
            altMaxVoo = int(input("Informe a altitude máxima atingida no voo em relação ao nível do mar: "))
            numFotosVoo = int(input("Informe o número de fotos tiradas durante o voo: "))
            equipamentoVoo = input("Informe o equipamento utilizado no voo: ")
            voo = Voo(dataVoo, duracaoVoo, altMaxVoo, numFotosVoo, equipamentoVoo, passageiro)
            voos.append(voo)

        piloto = Piloto(nome, telefone, cpf, voos)

        self.pilotoDAO.createPiloto(piloto)

    def read_piloto(self):
        id = input("Informe o ID: ")
        piloto = self.pilotoDAO.readPilotoById(id)
        if piloto:
            print(self.__pilotoToJSON(piloto))


    def read_all_piloto(self):
        pilotos = self.pilotoDAO.readAllPilotos()
        if pilotos:
            for piloto in pilotos:
                print(self.__pilotoToJSON(piloto))

    def update_piloto(self):
        voos: Voo = []

        nome = input("Informe o nome do piloto: ")
        telefone = int(input("Informe o telefone do piloto: "))
        cpf = int(input("Informe o CPF do piloto: "))

        nomePassageiro = input("Informe o nome do passageiro: ")
        telefonePassageiro = input("Informe o telefone do passageiro: ")
        cpfPassageiro = input("Informe o CPF do passageiro: ")
        passageiro = Passageiro(nomePassageiro, telefonePassageiro, cpfPassageiro)

        dataVoo = input("Informe a data do voo: ")
        duracaoVoo = int(input("Informe a duração do voo em minutos: "))
        altMaxVoo = int(input("Informe a altitude máxima atingida no voo em relação ao nível do mar: "))
        numFotosVoo = int(input("Informe o número de fotos tiradas durante o voo: "))
        equipamentoVoo = input("Informe o equipamento utilizado no voo: ")
        voo = Voo(dataVoo, duracaoVoo, altMaxVoo, numFotosVoo, equipamentoVoo, passageiro)
        voos.append(voo)

        while input("Deseja adicionar mais um voo? (s/n): ") == "s":
            nomePassageiro = input("Informe o nome do passageiro: ")
            telefonePassageiro = input("Informe o telefone do passageiro: ")
            cpfPassageiro = input("Informe o CPF do passageiro: ")
            passageiro = Passageiro(nomePassageiro, telefonePassageiro, cpfPassageiro)

            dataVoo = input("Informe a data do voo: ")
            duracaoVoo = int(input("Informe a duração do voo em minutos: "))
            altMaxVoo = int(input("Informe a altitude máxima atingida no voo em relação ao nível do mar: "))
            numFotosVoo = int(input("Informe o número de fotos tiradas durante o voo: "))
            equipamentoVoo = input("Informe o equipamento utilizado no voo: ")
            voo = Voo(dataVoo, duracaoVoo, altMaxVoo, numFotosVoo, equipamentoVoo, passageiro)
            voos.append(voo)

        piloto = Piloto(nome, telefone, cpf, voos)

        self.pilotoDAO.updatePiloto(id, piloto)

    def delete_piloto(self):
        id = input("Informe o ID: ")
        self.pilotoDAO.deletePiloto(id)

    def run(self):
        print("Clube Sul Mineiro de Voo Livre")
        print("Sistema de Gerenciamento de Voos Duplos")
        print("Comandos disponíveis: create, read, readAll, update, delete, quit")
        super().run()

    def __pilotoToJSON(self, piloto: Piloto):
        voos = [self.__getDadosVoo(voo) for voo in piloto.voos]
        return {"nome": piloto.nome, "telefone": piloto.telefone, "cpf": piloto.cpf, "numVoos": piloto.numVoos, "voos": voos}
    
    def __getDadosVoo(self, voo: Voo):
        dadosPassageiro = {"nome": voo.passageiro.nome, "telefone": voo.passageiro.telefone, "cpf": voo.passageiro.cpf}
        return {"data": voo.data, "duracao": voo.duracao, "altMax": voo.altMax, "numFotos": voo.numFotos, "equipamento": voo.equipamento, "passageiro": dadosPassageiro}