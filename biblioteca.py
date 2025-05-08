class conta () :

    def __init__ (self ,num,saldo,nome, tipo, limite):

        self.num = num
        self.saldo = saldo
        self.nome = nome
        self.tipo = tipo
        self.status = False
        self.limite = limite

    def status (self):
        if self.status == True:
            print("Esta ativo!")

        else:
            print ("esta inativo!")



