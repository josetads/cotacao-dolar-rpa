import requests

def coletar_cotacoes():

    url = "https://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL"

    resposta = requests.get(url)

    dados = resposta.json()

    dolar = float(dados['USDBRL']['bid'])
    euro = float(dados['EURBRL']['bid'])

    # valor base do real
    real = 1.0

    return dolar, euro, real