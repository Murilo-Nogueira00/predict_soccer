from model.time_casa import TimeCasa
from model.time_visitante import TimeVisitante
from .dados_times import retorna_dados_do_jogo

def instancia_times(sigla_casa: str, sigla_fora: str):
    dados_casa = retorna_dados_do_jogo(sigla_casa)
    dados_fora = retorna_dados_do_jogo(sigla_fora)

    # Cria as instâncias dos times que vão jogar
    instancia_casa = TimeCasa(
        dados_casa['Team'].values[0],
        dados_casa['Sigla'].values[0],
        float(dados_casa['GF'].values[0]),
        float(dados_casa['GS'].values[0]),
        float(dados_casa['CF'].values[0]),
        float(dados_casa['CS'].values[0]),
        float(dados_casa['JC'].values[0]),
        float(dados_casa['GEC'].values[0]),
        float(dados_casa['GSEC'].values[0]),
        float(dados_casa['R'].values[0])
    )

    instancia_fora = TimeVisitante(
        dados_fora['Team'].values[0],
        dados_fora['Sigla'].values[0],
        float(dados_fora['GF'].values[0]),
        float(dados_fora['GS'].values[0]),
        float(dados_fora['CF'].values[0]),
        float(dados_fora['CS'].values[0]),
        float(dados_fora['JF'].values[0]),
        float(dados_fora['GEF'].values[0]),
        float(dados_fora['GSEF'].values[0]),
        float(dados_fora['R'].values[0])
    )

    # Retorna instância
    return instancia_casa, instancia_fora
