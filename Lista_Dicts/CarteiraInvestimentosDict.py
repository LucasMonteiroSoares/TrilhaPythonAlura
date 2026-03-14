resposta_api = {
    "cliente_id": "8842-X",
    "nome": "Lucas",
    "perfil": "Arrojado",
    "carteira": [
        {"ativo": "PETR4", "quantidade": 200},
        {"ativo": "VALE3", "quantidade": 50},
        {"ativo": "ITUB4", "quantidade": 100}
    ]
}

precos_mercado = {
    "PETR4": 36.50,
    "VALE3": 69.20,
    "ITUB4": 34.80,
    "WEGE3": 40.10
}

print(f'Boas vindas {resposta_api['nome']}! \n'
      f'Seu perfil de investidor é {resposta_api['perfil']}')

patrimonio_total = 0

for linha in resposta_api['carteira']:
    ativo_atual = linha['ativo']
    quantidade_atual = linha['quantidade']
    if ativo_atual in precos_mercado:
        patrimonio_total += quantidade_atual*precos_mercado[ativo_atual]


print(patrimonio_total)