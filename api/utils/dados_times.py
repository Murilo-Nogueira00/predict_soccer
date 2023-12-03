import pandas as pd


def retorna_dados_times():
    df = pd.read_csv('https://raw.githubusercontent.com/Murilo-Nogueira00/br2023_dataset/main/dataset_brasileirao.csv',
                     encoding='latin-1', delimiter=';')
    return df


def retorna_dados_do_jogo(sigla: str):
    df = pd.read_csv('https://raw.githubusercontent.com/Murilo-Nogueira00/br2023_dataset/main/dataset_brasileirao.csv',
                 encoding='latin-1', delimiter=';')
    dados = df[df['Sigla'] == sigla]
    return dados if not dados.empty else None

