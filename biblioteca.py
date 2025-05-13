class animal():
    def __init__(self,nome,cor):
        self.nome= nome
        self.cor= cor

    def comer(self):
        print(f"o{self.nome} foi comer...")

class gato(animal):
    def __init__(self,nome,cor):
        super().__init__(nome,cor)

    def miar(self):
        print (f"{self.nome} foi miando...")

class vaca(animal):
    def __init__(self,nome,cor):
        print(f"{self.vaca} foi comer capim")

class coelho(animal):
    def __init__(self,nome,cor):
        print("comendo")
class cachorro(animal):
    def __init__(self,nome,cor):
        print(f"comendo")


class ingresso:
     def __init__(self, preco):

        self.preco = preco

     def imprimeValor(self):
        print(f"custa {self.preco}")

class ingressovip:
    def __init__(self,nome, preco):
        super

        preco = ingresso

    print(f"{preco} do ingresso normal no {ingressovip} fica por {v}")

class forma():
    







