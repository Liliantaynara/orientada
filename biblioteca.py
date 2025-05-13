from encodings.punycode import selective_find
from traceback import print_tb


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

        preco = ingresso6
    print(f"{preco} do ingresso normal no {ingressovip} fica por {v}")

class formas():
    def __init__(self):
        self.area = 0
        self.perimetro = 0

class retangulo(formas):
    def _init_(self, base, altura):
        super().__init__
        self.base = base
        self.altura = altura

    def calculaArea(self):
        self.area = self.base * self.altura
        print(f"{self.area}")

    def calculaPeri(self):
        self.perimetro = 2 * (self.base + self.altura)
        print(f"{self.perimetro}")

class triangulo(formas):
    def _init_(self, base, altura, lado1, lado2):
        super()._init_()
        self.base = base
        self.altura = altura
        self.lado1 = lado1
        self.lado2 = lado2

    def calculArea(self):
        self.area = (self.base * self.altura) / 2
        print (f"{self.area}")

    def calculaPeri(self):
        self.perimetro = self.base + self.lado1 + self.lado2
        print(f"{self.perimetro}")






