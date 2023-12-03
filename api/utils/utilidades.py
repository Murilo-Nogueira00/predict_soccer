from .dados_times import retorna_dados_times

def media(valor_1, valor_2):
    return (valor_1 + valor_2)/2

def retorna_media_coef_momento():
    df = retorna_dados_times()
    return df['R'].mean()
