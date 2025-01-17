import json

def carregar_dados():
    try:
        with open('faturamento.json', 'r') as file:
            dados = json.load(file)
        return dados
    except FileNotFoundError:
        print("Erro: Arquivo 'faturamento.json' não encontrado.")
        return None
    except json.JSONDecodeError:
        print("Erro ao decodificar o arquivo JSON.")
        return None

def calcular_faturamento(dados):
    faturamento_diario = [registro['valor'] for registro in dados if registro['valor'] > 0]

    if not faturamento_diario:
        print("Não há faturamento válido para o cálculo.")
        return

    menor_faturamento = min(faturamento_diario)

    maior_faturamento = max(faturamento_diario)

    media_faturamento = sum(faturamento_diario) / len(faturamento_diario)

    dias_acima_media = len([valor for valor in faturamento_diario if valor > media_faturamento])

    print(f"Menor faturamento: R${menor_faturamento:.2f}")
    print(f"Maior faturamento: R${maior_faturamento:.2f}")
    print(f"Dias com faturamento acima da média: {dias_acima_media}")


def main():
    dados = carregar_dados()
    
    if dados:
        calcular_faturamento(dados)

if __name__ == "__main__":
    main()
