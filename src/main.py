from coletor_moedas import obter_cotacoes
from excel_manager import atualizar_excel


def main():

    dolar, euro, real = obter_cotacoes()

    print("Cotação atual:")
    print("Dólar:", dolar)
    print("Euro:", euro)
    print("Real:", real)

    atualizar_excel(dolar, euro, real)


if __name__ == "__main__":
    main()