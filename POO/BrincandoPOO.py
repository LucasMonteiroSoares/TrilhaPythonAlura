class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'{self.nome} | {self.categoria}'

    def listar_restaurantes():
        for restaurante in Restaurante.restaurantes:
            print(f'{restaurante.nome} | {restaurante.categoria} | {restaurante.ativo}')

#r1 = Restaurante('BK', 'Hamburguer')
#r2 = Restaurante('Mac', 'Fast Food')
#Restaurante.listar_restaurantes()

class ContaBancaria:
    def __init__(self, titular, saldo):
        self._titular = titular
        self._saldo = saldo
        self._ativo = False

    def __str__(self):
        return f'{self._titular} | {self._saldo} | {self._ativo}'

    @classmethod
    def ativar_conta(cls):
        cls.ativo = True
        return "Conta ativada"

c1 = ContaBancaria("Pedro", 0)
c2 = ContaBancaria("Paulo", 5000)
c3 = ContaBancaria("Douglas", 1000)
c3.ativar_conta()
print(c1)
print(c2)
print(c3)