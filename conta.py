
class Conta:
    def __int__(self, numero, titular, saldo, limite):
        print("Construindo objeto... {}".format(self))
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

    def extrato(self):
        print("Saldo de R${} do titular {}".format(self.saldo, self.titular))

    def deposita(self, valor):
        self.saldo += valor

    def saca(selfself, valor):
        self.saldo -= valor