import pandas as pd
from datetime import datetime
import os

def salvar_excel(dolar, euro, real):

    pasta = "Database"
    arquivo = os.path.join(pasta, "dados_cotacoes.xlsx")

    os.makedirs(pasta, exist_ok=True)

    data = datetime.now().strftime("%Y-%m-%d %H:%M")

    nova_linha = pd.DataFrame({
        "Data": [data],
        "Dolar": [dolar],
        "Euro": [euro],
        "Real": [real]
    })

    if os.path.exists(arquivo):

        df = pd.read_excel(arquivo)
        df = pd.concat([df, nova_linha], ignore_index=True)

    else:

        df = nova_linha

    df.to_excel(arquivo, index=False)

    return arquivo