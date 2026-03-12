from POO3.modelos.Banco import Banco

class Agencia(Banco):
    def __init__(self, nome, endereco, numero):
        super().__init__(nome, endereco)
        self._numero = numero

    def __str__(self):
        return f'{super().__str__()} / Numero: {self._numero}'