from MotoristaDAO import MotoristaDAO
from Motorista import Motorista
from Corrida import Corrida
from Passageiro import Passageiro

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

class MotoristaCLI(SimpleCLI):
    def __init__ (self):
        super().__init__()
        self.motoristaDAO = MotoristaDAO()
        self.add_command("create", self.create_motorista)
        self.add_command("read", self.read_motorista)
        self.add_command("update", self.update_motorista)
        self.add_command("delete", self.delete_motorista)

    def create_motorista(self):
        corridas: Corrida = []

        nomePassageiro = input("Informe o nome do passageiro: ")
        documentoPassageiro = input("Informe o documento do passageiro: ")
        passageiro = Passageiro(nomePassageiro, documentoPassageiro)

        notaCorrida = int(input("Informe a nota da corrida: "))
        distanciaCorrida = float(input("Informe a distancia da corrida: "))
        valorCorrida = float(input("Informe o valor da corrida: "))
        corrida = Corrida(notaCorrida, distanciaCorrida, valorCorrida, passageiro)
        corridas.append(corrida)

        while input("Deseja adicionar mais uma corrida? (s/n): ") == "s":
            notaCorrida = int(input("Informe a nota da corrida: "))
            distanciaCorrida = float(input("Informe a distancia da corrida: "))
            valorCorrida = float(input("Informe o valor da corrida: "))
            corrida = Corrida(notaCorrida, distanciaCorrida, valorCorrida, passageiro)
            corridas.append(corrida)

        nota = input("Informe a nota do motorista: ")
        motorista = Motorista(corridas, nota)

        self.motoristaDAO.createMotorista(motorista)

    def read_motorista(self):
        id = input("Informe o ID: ")
        motorista = self.motoristaDAO.readMotoristaById(id)
        if motorista:
            print(motorista)

    def update_motorista(self):
        corridas: Corrida = []

        id = input("Informe o ID do motorista: ")
        nomePassageiro = input("Informe o nome do passageiro: ")
        documentoPassageiro = input("Informe o documento do passageiro: ")
        passageiro = Passageiro(nomePassageiro, documentoPassageiro)

        notaCorrida = int(input("Informe a nota da corrida: "))
        distanciaCorrida = float(input("Informe a distancia da corrida: "))
        valorCorrida = float(input("Informe o valor da corrida: "))
        corrida = Corrida(notaCorrida, distanciaCorrida, valorCorrida, passageiro)
        corridas.append(corrida)

        while input("Deseja adicionar mais uma corrida? (s/n): ") == "s":
            notaCorrida = int(input("Informe a nota da corrida: "))
            distanciaCorrida = float(input("Informe a distancia da corrida: "))
            valorCorrida = float(input("Informe o valor da corrida: "))
            corrida = Corrida(notaCorrida, distanciaCorrida, valorCorrida, passageiro)
            corridas.append(corrida)

        nota = input("Informe a nota do motorista: ")
        motorista = Motorista(corridas, nota)

        self.motoristaDAO.updateMotorista(id, motorista)

    def delete_motorista(self):
        id = input("Informe o ID: ")
        self.motoristaDAO.deleteMotorista(id)

    def run(self):
        print("Bem vindo ao CLI de Motoristas!")
        print("Comandos disponíveis: create, read, update, delete, quit")
        super().run()

