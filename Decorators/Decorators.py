def meu_primeiro_decorator(funcao_original):
    def wrapper():
        print("1. Isso acontece ANTES da função rodar.")

        funcao_original()  # Aqui chamamos a função de verdade

        print("3. Isso acontece DEPOIS da função rodar.")

    return wrapper  # Retornamos o "embrulho"

@meu_primeiro_decorator
def dizer_ola():
    print("2. Olá! Eu sou a função original.")

dizer_ola()

@property # Decorator para criar métodos getters
def saldo(self):
    # Agora você pode acessar como 'usuario.saldo' em vez de 'usuario.saldo()'
    return f"R$ {self._saldo:.2f}"

@dataclass # Decorator para criar uma classe, não precisa criar o __init__ nem sobresvrever o __repr__
class AtivoFinanceiro:
    ticker: str
    preco: float
    quantidade: int