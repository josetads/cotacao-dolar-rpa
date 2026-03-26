from coletor_dolar import obter_dolar
from excel_manager import salvar_dados

def main():
    print("=== ROBÔ DE MONITORAMENTO DO DÓLAR ===")

    data, valor = obter_dolar()

    if data and valor:
        print(f"Cotação do dólar em {data}: R$ {valor}")
        salvar_dados(data, valor)
    else:
        print("Erro na execução do robô.")

if __name__ == "__main__":
    main()