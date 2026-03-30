import pandas as pd
from datetime import datetime
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

PASTA_DATABASE = os.path.join(BASE_DIR, "Database")

ARQUIVO_EXCEL = os.path.join(PASTA_DATABASE, "dados_dolar.xlsx")


def atualizar_excel(dolar, euro, real):

    os.makedirs(PASTA_DATABASE, exist_ok=True)

    data = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    novo_registro = pd.DataFrame({
        "Data": [data],
        "Dolar": [dolar],
        "Euro": [euro],
        "Real": [real]
    })

    if os.path.exists(ARQUIVO_EXCEL):

        df = pd.read_excel(ARQUIVO_EXCEL)
        df = pd.concat([df, novo_registro], ignore_index=True)

    else:

        df = novo_registro

    df.to_excel(ARQUIVO_EXCEL, index=False)

    print("Excel atualizado com sucesso.")