from teacher_crud import TeacherCRUD

teacherCrud = TeacherCRUD()

# # Questão 3 - b)
# teacherCrud.create("Chris Lima", 1956, "189.052.396-66")

# # Questão 3 - c)
# result = teacherCrud.read("Chris Lima")
# print("\nProfessor Chris Lima:")
# print(result[0][0], " - ", result[0][1], " - ", result[0][2])

# # Questão 3 - d)
# teacherCrud.update("Chris Lima", "162.052.777-77")

# Questão 3 - e)
class CLI:
    def __init__(self):
        self.teacherCrud = TeacherCRUD()

    def initialize(self):
        while True:
            print("\nOpções disponíveis: ")
            print("1 - Cadastrar professor")
            print("2 - Consultar professor")
            print("3 - Atualizar professor")
            print("4 - Deletar professor")
            print("5 - Sair")

            option = int(input("\nDigite a opção desejada: "))

            if option == 1:
                self.create()
            elif option == 2:
                self.read()
            elif option == 3:
                self.update()
            elif option == 4:
                self.delete()
            elif option == 5:
                break
            else:
                print("Opção inválida!")
    
    def create(self):
        print("\n Cadastrar professor:")
        name = input("Digite o nome do professor: ")
        ano_nasc = int(input("Digite o ano de nascimento do professor: "))
        cpf = input("Digite o cpf do professor: ")
        self.teacherCrud.create(name, ano_nasc, cpf)
    
    def read(self):
        print("\n Consultar professor:")
        name = input("Digite o nome do professor: ")
        result = self.teacherCrud.read(name)
        print("\nProfessor", name, ":")
        print(result[0][0], " - ", result[0][1], " - ", result[0][2])

    def update(self):
        print("\n Atualizar professor:")
        name = input("Digite o nome do professor: ")
        cpf = input("Digite o novo cpf do professor: ")
        self.teacherCrud.update(name, cpf)
    
    def delete(self):
        print("\n Deletar professor:")
        name = input("Digite o nome do professor: ")
        self.teacherCrud.delete(name)

cli = CLI()
cli.initialize()
