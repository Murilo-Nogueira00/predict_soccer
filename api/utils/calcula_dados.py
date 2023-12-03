from model.time_casa import TimeCasa
from model.time_visitante import TimeVisitante
from model.times import Times
from .utilidades import retorna_media_coef_momento, media

def get_coeficiente_aproveitamento(time: Times):
    coef_ataque = ((time.get_ge()/time.get_jogos())/time.get_media_gf()) * \
        get_coeficiente_momento(time, time.get_coeficiente_momento())
    coef_defesa = (time.get_media_gs()/(time.get_gse()/time.get_jogos())) / \
        get_coeficiente_momento(time, time.get_coeficiente_momento())

    return coef_ataque, coef_defesa


def get_coeficiente_momento(time: Times, media_coeficiente_momento):
    momento = (time.get_r()/media_coeficiente_momento)*100
    return momento


def get_finalizacoes_feitas_jogo(time_1: TimeCasa, time_2: TimeVisitante):
    coef_ataque_1, coef_defesa_1 = get_coeficiente_aproveitamento(time_1)
    coef_ataque_2, coef_defesa_2 = get_coeficiente_aproveitamento(time_2)

    finalizacoes_1 = round(media(
        (time_1.get_media_cf() * coef_ataque_1), (time_2.get_media_cs() * coef_defesa_2)))
    finalizacoes_2 = round(media(
        (time_2.get_media_cf() * coef_ataque_2), (time_1.get_media_cs() * coef_defesa_1)))

    return finalizacoes_1, finalizacoes_2


def get_indicadores_gols(time_1: TimeCasa, time_2: TimeVisitante):
    coef_ataque_1, coef_defesa_1 = get_coeficiente_aproveitamento(time_1)
    coef_ataque_2, coef_defesa_2 = get_coeficiente_aproveitamento(time_2)

    indicador_gol_1 = media(
        (time_1.get_media_gf() * coef_ataque_1), (time_2.get_media_gs() * coef_defesa_2))
    indicador_gol_2 = media(
        (time_2.get_media_gf() * coef_ataque_2), (time_1.get_media_gs() * coef_defesa_1))

    return indicador_gol_1, indicador_gol_2


def get_prob_de_gol(indicador, finalizacoes):
    return indicador/finalizacoes

def registra_coeficiente_momentos(time_casa: TimeCasa, time_fora: TimeVisitante):
    media_coeficiente_momento = retorna_media_coef_momento()
    momento_casa = get_coeficiente_momento(
        time_casa, media_coeficiente_momento)
    time_casa.set_coeficiente_momento(momento_casa)
    momento_fora = get_coeficiente_momento(
        time_fora, media_coeficiente_momento)
    time_fora.set_coeficiente_momento(momento_fora)


def registra_finalizacoes_e_probabilidades(time_casa: TimeCasa, time_fora: TimeVisitante):
    registra_coeficiente_momentos(time_casa, time_fora)
    finalizacoes_casa, finalizacoes_fora = get_finalizacoes_feitas_jogo(
        time_casa, time_fora)
    indicador_gol_casa, indicador_gol_fora = get_indicadores_gols(
        time_casa, time_fora)
    probabilidade_casa = get_prob_de_gol(indicador_gol_casa, finalizacoes_casa)
    probabilidade_fora = get_prob_de_gol(indicador_gol_fora, finalizacoes_fora)
    time_casa.set_finalizacoes_feitas(finalizacoes_casa)
    time_casa.set_probabilidade_de_gol(probabilidade_casa)
    time_fora.set_finalizacoes_feitas(finalizacoes_fora)
    time_fora.set_probabilidade_de_gol(probabilidade_fora)

    return finalizacoes_casa, finalizacoes_fora
