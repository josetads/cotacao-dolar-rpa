import requests

URL = "https://api.bcb.gov.br/dados/serie/bcdata.sgs.1/dados/ultimos/1?formato=json"

def obter_dolar():
    try:
        response = requests.get(URL)
        response.raise_for_status()

        dados = response.json()

        valor = float(dados[0]['valor'])
        data = dados[0]['data']

        return data, valor

    except Exception as e:
        print(f"Erro ao coletar dados: {e}")
        return None, None