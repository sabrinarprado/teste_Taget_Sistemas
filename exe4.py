import json

with open("dados.json", "r", encoding="utf-8") as file:
    dados = json.load(file)

# for item in dados:
#     print(f"Dia {item['dia']}: {item['valor']}")

faturamento_diario = {item["dia"]: item["valor"] for item in dados}
print(faturamento_diario)

faturamento_estado = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53,
}

valor_total_mensal = sum(faturamento_diario.values())

percentual_estado = {estado: (faturamento / valor_total_mensal)*100 for estado, faturamento in faturamento_estado.items()}

print("\nPercentual de Representação de Cada Estado:")
for estado, percentual in percentual_estado.items():
    print(f"{estado}: {percentual:.2f}%")