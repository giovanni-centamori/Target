import json

with open('faturamento.json', 'r') as file:
    data = json.load(file)

faturamento_diario = data["faturamento_diario"]

faturamento_diario = [valor for valor in faturamento_diario if valor > 0]

menor_faturamento = min(faturamento_diario)
maior_faturamento = max(faturamento_diario)

media_faturamento = sum(faturamento_diario) / len(faturamento_diario)

dias_acima_media = len([valor for valor in faturamento_diario if valor > media_faturamento])

print(f"Menor faturamento: R${menor_faturamento}")
print(f"Maior faturamento: R${maior_faturamento}")
print(f"Dias com faturamento acima da média: {dias_acima_media}")