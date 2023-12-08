import random
import numpy as np
import pickle
import joblib
from utils.instancia_times import instancia_times
from utils.calcula_dados import registra_finalizacoes_e_probabilidades

class Model:
    
    def carrega_modelo(self, path):
        """Dependendo se o final for .pkl ou .joblib, carregamos de uma forma ou de outra
        """
        
        if path.endswith('.pkl'):
            model = pickle.load(open(path, 'rb'))
        elif path.endswith('.joblib'):
            model = joblib.load(path)
        else:
            raise Exception('Formato de arquivo não suportado')
        return model
    
    def preditor(model, form):
        """Realiza a predição de uma partida com base no modelo treinado
        """

        time_casa, time_fora = instancia_times(form.sigla_casa, form.sigla_fora)
        finalizacoes_casa, finalizacoes_fora = registra_finalizacoes_e_probabilidades(time_casa, time_fora)
        expulsoes_casa = min(max(random.betavariate(100, 1), 0), 1)
        expulsoes_fora = min(max(random.betavariate(1, 100), 0), 1)
        print(finalizacoes_casa, finalizacoes_fora)
        print(expulsoes_casa, expulsoes_fora)
        X_input = np.array([0, 
                            1, 
                            finalizacoes_casa,
                            finalizacoes_fora,
                            expulsoes_casa,
                            expulsoes_fora
                        ])
        # Faremos o reshape para que o modelo entenda que estamos passando
        diagnosis = model.predict(X_input.reshape(1, -1))
        probabilidades = model.predict_proba(X_input.reshape(1, -1))

        mapeamento_vencedor = {
            0: time_casa.get_sigla(), 1: time_fora.get_sigla(), 2: 'empate'}
        vencedor = mapeamento_vencedor.get(int(diagnosis[0]), 'resultado inválido')

        return vencedor, probabilidades