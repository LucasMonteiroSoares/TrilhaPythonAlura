from POO3.modelos.Agencia import Agencia
from POO3.modelos.Banco import Banco


def main():
    banco1 = Banco('Itau', 'Mooca')
    agencia1 = Agencia('Itau', 'Mooca', '57')

    print(banco1)
    print(agencia1)

if __name__ == '__main__':
    main()