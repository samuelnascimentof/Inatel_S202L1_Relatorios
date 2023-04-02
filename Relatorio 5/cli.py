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
        
class BookCLI(SimpleCLI):
    def __init__(self, book_model):
        super().__init__()
        self.book_model = book_model
        self.add_command("create", self.create_book)
        self.add_command("read", self.read_book)
        self.add_command("update", self.update_book)
        self.add_command("delete", self.delete_book)

    def create_book(self):
        title = input("Enter the title: ")
        author = input("Enter the author: ")
        year = int(input("Enter the year: "))
        price = float(input("Enter the price: "))
        self.book_model.create_book(title, author, year, price)

    def read_book(self):
        id = input("Enter the id: ")
        book = self.book_model.read_book_by_id(id)
        if book:
            print(f"Title: {book['titulo']}")
            print(f"Author: {book['autor']}")
            print(f"Year: {book['ano']}")
            print(f"Price: {book['preco']}")

    def update_book(self):
        id = input("Enter the id: ")
        title = input("Enter the new title: ")
        author = input("Enter the new author: ")
        year = int(input("Enter the new year: "))
        price = float(input("Enter the new price: "))
        self.book_model.update_book(id, title, author, year, price)

    def delete_book(self):
        id = input("Enter the id: ")
        self.book_model.delete_book(id)
        
    def run(self):
        print("Welcome to book CLI!")
        print("Available commands: create, read, update, delete, quit")
        super().run()