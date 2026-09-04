class Pessoa:

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentacao(self):
        print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos.")


class Estudante(Pessoa):

    def __init__(self, nome, idade, serie):
        super().__init__(nome, idade)
        self.serie = serie

    def grade(self):
        print(f"Olá, meu nome é {self.nome}, tenho {self.idade} anos e estou na {self.serie} série.")


pessoa1 = Pessoa("Adiel", 17)
pessoa1.apresentacao()

estudante1 = Estudante("Adiel", 17, "2º")
estudante1.apresentacao()
estudante1.grade()
estudante2 = Estudante("João", 16, "1º")

