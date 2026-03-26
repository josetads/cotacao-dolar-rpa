import pandas as pd
import os

CAMINHO = "src/Database/dados_dolar.xlsx"

def salvar_dados(data, valor):
    novo = pd.DataFrame({
        "Data": [data],
        "Valor": [valor]
    })

    # Garante que a pasta existe
    os.makedirs("src/Database", exist_ok=True)

    try:
        # Se o arquivo existir, tenta ler
        if os.path.exists(CAMINHO):
            df = pd.read_excel(CAMINHO, engine="openpyxl")

            # Evitar duplicidade
            if data in df["Data"].values:
                print("Registro já existe.")
                return

            df = pd.concat([df, novo], ignore_index=True)
        else:
            df = novo

    except Exception as e:
        print("Arquivo corrompido ou inválido. Criando novo...")
        df = novo

    # Salva corretamente como Excel
    df.to_excel(CAMINHO, index=False, engine="openpyxl")

    print("Dados salvos com sucesso!")