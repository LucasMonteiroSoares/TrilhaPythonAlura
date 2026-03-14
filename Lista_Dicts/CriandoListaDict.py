dados_brutos = """
sensor_id,data,consumo_kwh,status
S1,2026-03-01,150.5,normal
S2,2026-03-01,0.0,inativo
S1,2026-03-02,165.2,normal
S3,2026-03-02,450.0,anomalia
S2,2026-03-02,0.0,inativo
S3,2026-03-03,480.5,anomalia
"""

listaPorLinhas = dados_brutos.strip().split('\n')
dadosProcessados = []

for linha in listaPorLinhas[1:]:
    valores = linha.split(',')

    registro = {
        "sensor_id": valores[0],
        "data": valores[1],
        "consumo_kwh": valores[2],
        "status": valores[3]
    }

    dadosProcessados.append(registro)

consumoTotal = 0
maiorConsumo = 0

for linha in dadosProcessados:
    if linha["status"] != 'inativo':
        consumoTotal += float(linha['consumo_kwh'])
        if maiorConsumo < float(linha['consumo_kwh']):
            maiorConsumo = float(linha['consumo_kwh'])
            indice = linha




