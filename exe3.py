import json

with open("dados.json", "r", encoding="utf-8") as file:
    dados = json.load(file)

# for item in dados:
#     print(f"Dia {item['dia']}: {item['valor']}")

faturamento_diario = {item["dia"]: item["valor"] for item in dados}
print(faturamento_diario)

dia_menor, menor_faturamento = min(faturamento_diario.items(), key=lambda item: item[1])
print(f"Menor faturamento foi de {menor_faturamento} no dia {dia_menor}")

dia_maior, maior_faturamento = max(faturamento_diario.items(), key=lambda item: item[1])
print(f"Maior faturamento foi de {maior_faturamento} no dia {dia_maior}")
