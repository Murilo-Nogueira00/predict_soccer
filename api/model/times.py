from abc import ABC, abstractmethod


class Times(ABC):
    def __init__(self, nome, sigla, media_gf, media_gs, media_cf, media_cs, jogos, ge, gse, r):
        self.nome = nome
        self.sigla = sigla
        self.media_gf = media_gf
        self.media_gs = media_gs
        self.media_cf = media_cf
        self.media_cs = media_cs
        self.jogos = jogos
        self.ge = ge
        self.gse = gse
        self.r = r
        self.coeficiente_momento = None
        self.finalizacoes_feitas = None
        self.probabilidade_de_gol = None
        self.pontuacao = 0
        self.jogos_totais = 0
        self.vitorias = 0
        self.empates = 0
        self.derrotas = 0
        self.gols_feitos = 0
        self.gols_sofridos = 0

    # Getters para os atributos
    def get_nome(self):
        return self.nome

    def get_sigla(self):
        return self.sigla

    def get_media_gf(self):
        return self.media_gf

    def get_media_gs(self):
        return self.media_gs

    def get_media_cf(self):
        return self.media_cf

    def get_media_cs(self):
        return self.media_cs

    def get_jogos(self):
        return self.jogos

    def get_ge(self):
        return self.ge

    def get_gse(self):
        return self.gse

    def get_r(self):
        return self.r

    def get_coeficiente_momento(self):
        return self.coeficiente_momento

    def get_finalizacoes_feitas(self):
        return self.finalizacoes_feitas

    def get_probabilidade_de_gol(self):
        return self.probabilidade_de_gol

    def get_pontuacao(self):
        return self.pontuacao

    def get_vitorias(self):
        return self.vitorias

    def get_empates(self):
        return self.empates

    def get_derrotas(self):
        return self.derrotas

    def get_gols_feitos(self):
        return self.gols_feitos

    def get_gols_sofridos(self):
        return self.gols_sofridos

    def get_jogos_totais(self):
        return self.jogos_totais

    # Setters
    def set_coeficiente_momento(self, coeficiente):
        self.coeficiente_momento = coeficiente

    def set_finalizacoes_feitas(self, finalizacoes):
        self.finalizacoes_feitas = finalizacoes

    def set_probabilidade_de_gol(self, probabilidade):
        self.probabilidade_de_gol = probabilidade

    def get_coeficiente_momento(self):
        return self.coeficiente_momento

    def set_coeficiente_momento(self, coeficiente):
        self.coeficiente_momento = coeficiente

    def set_pontuacao(self, valor):
        self.pontuacao += valor

    def set_jogos_totais(self):
        self.jogos_totais += 1

    def set_vitorias(self):
        self.vitorias += 1

    def set_empates(self):
        self.empates += 1

    def set_derrotas(self):
        self.derrotas += 1

    def set_gols_feitos(self, valor):
        self.gols_feitos += valor

    def set_gols_sofridos(self, valor):
        self.gols_sofridos += valor
