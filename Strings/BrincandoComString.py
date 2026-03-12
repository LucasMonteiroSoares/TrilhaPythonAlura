"""Estudo de String em Python"""

texto = "Céu azul e colorido chovendo no molhado e relampiando com furacão, ventos fortes e neblina."
# Entendo uma string como um array de caracteres

print (texto, '\n')
print (f'Tamanho do texto: {len(texto)}') # Função len para descobrir exatamente quantos caracteres possui
print (f'Primeira letra do texto: {texto[0]}') # Iteramos sobre uma string assim como um array
print (f'Último caractere do texto {texto[len(texto)-1]} \n') # Último elemento será o len - 1 pois começa no 0

# Slicing / Fatiamento
print(f'Assim se faz slicing: {texto[0:8]}') # Indice de start e stop (não pega o de stop)
print(f'Slicing sem stop parameter: {texto[50:]} \n')
print(f'Texto invertido: {texto[::-1]} \n')

# Limpeza, e transformação
texto2 = ' eu amo a isabelle! '
print(texto2)
texto2v2 = texto2.strip() # Elimina espaços em branco do começo e final da String
print(texto2v2)
print(texto2v2.capitalize()) # Deixa a primeira letra da String maiúscula
print(texto2v2.title()) # Primeiras letras das palavras todas as maiúsculas, como um título
print(texto2v2.upper(), '\n') # Todas as letras maiúsculas

# Divisão e junção
palavras = texto.split(' ') # Podemos passar como parâmetro o caracter separador
print(palavras)
print(' '.join(palavras), '\n') # O caracter que passarmos ali dentro do aspas vai tornar-se separador

# Busca e validação
posicaoColorido = texto.find('colorido')
print(f"Posição da palavra colorido no texto: {posicaoColorido}")
print(f'Quantidade de vezes que a palavra "e" aparece no texto: {palavras.count('e')}') # Usei a função na lista palavras, pois se não, ia contar quantos caracteres tinha no texto

arquivo = "relatorio.pdf"
if arquivo.endswith("o.pdf"): # Existe o endswith e o startswith
    print("É um arquivo PDF válido.")

codigo = "12345"
print(codigo.isdigit(), '\n') # Verifica se é tudo digito, isalpha (letra), isalnum (alfanumérico)

# Substituição
texto3 = 'O rato roeu a roupa do rei de roma'
newTexto3 = texto3.replace('r','l') # Essa função serve para trocar substring, ou seja, palavras tb
print(newTexto3)

# Arredondando numa F-String
preco = 19.985
print(f'O preço desse pastel é {preco:.2f}')

