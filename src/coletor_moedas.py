import requests


def obter_cotacoes():

    url_dolar = "https://api.bcb.gov.br/dados/serie/bcdata.sgs.1/dados/ultimos/1?formato=json"
    url_euro = "https://api.bcb.gov.br/dados/serie/bcdata.sgs.21619/dados/ultimos/1?formato=json"

    resposta_dolar = requests.get(url_dolar)
    resposta_euro = requests.get(url_euro)

    dolar = float(resposta_dolar.json()[0]["valor"])
    euro = float(resposta_euro.json()[0]["valor"])

    real = 1.0

    return dolar, euro, real