import requests
import json

url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'
meuRequest = requests.get(url) # Faz um request de get no endpoint
print(meuRequest) # Printa a response com status code
print(meuRequest.status_code) # Acessando atributo status code do meu request

if meuRequest.status_code == 200:
    dados_json = meuRequest.json()
else:
    print(f'Erro identificado: {meuRequest.status_code}')


