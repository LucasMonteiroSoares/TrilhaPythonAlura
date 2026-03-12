'''Imagine que você recebeu uma string de texto contendo um lote de logs de operações da
bolsa de valores. Os dados vieram separados por ponto e vírgula (;), mas estão cheios de
espaços extras, letras maiúsculas/minúsculas misturadas e números com muitas casas decimais.'''

logs_brutos = """
  TRX001; CLIENTE: joão silva; OP: compra; ATIVO: PETR4; VALOR: 35.452 ; STATUS: sucesso 
TRX002; CLIENTE: maria oliveira; OP: venda; ATIVO: VALE3; VALOR: 68.90 ; STATUS: erro  
   TRX003; CLIENTE: carlos santos; OP: compra; ATIVO: ITUB4; VALOR: 34.1289; STATUS: sucesso
"""
# 1. Separar o texto em linhas
# O strip() inicial tira as quebras de linha vazias do começo e do fim do bloco inteiro
linhas = logs_brutos.strip().split('\n')

# 2. Iterar sobre cada linha da lista
for linha in linhas:

    # Prevenção: Pula a iteração atual se a linha for apenas um espaço em branco
    if not linha.strip():
        continue

    # 3. Filtrar apenas as transações com sucesso
    if "sucesso" in linha:

        # 4. Dividir a linha em pedaços usando o ponto e vírgula
        pedacos = linha.split(';')

        # 5. Limpar e extrair as informações (usando split no ':' para pegar o valor real)
        # Exemplo do pedacos[1]: " CLIENTE: joão silva".
        # split(':') transforma em [" CLIENTE", " joão silva"]. Pegamos o índice [1].

        cliente = pedacos[1].split(':')[1].strip().title() # Tira espaços e capitaliza
        operacao = pedacos[2].split(':')[1].strip().upper() # Tira espaços e deixa maiúsculo
        ativo = pedacos[3].split(':')[1].strip() # Apenas tira espaços
        valor_str = pedacos[4].split(':')[1].strip() # Extração do valor financeiro
        valor_float = float(valor_str) # Transforma o texto em um número decimal

        # 6. Formatação Final com F-String e arredondamento (.2f)
        mensagem = f"Transação Aprovada: {cliente} realizou uma {operacao} de {ativo} no valor de R$ {valor_float:.2f}."
        print(mensagem)