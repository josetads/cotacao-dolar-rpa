from botcity.web import WebBot
from coletor_moedas import coletar_cotacoes
from excel_manager import salvar_excel
from email_sender import enviar_email

def main():

    print("Iniciando robô de monitoramento de moedas")

    bot = WebBot()
    bot.headless = True

    dolar, euro, real = coletar_cotacoes()

    print("Cotação atual:")
    print("Dolar:", dolar)
    print("Euro:", euro)
    print("Real:", real)

    arquivo = salvar_excel(dolar, euro, real)

    print("Excel atualizado")

    enviar_email(arquivo)

    print("Processo finalizado")

if __name__ == "__main__":
    main()