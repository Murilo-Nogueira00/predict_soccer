from model.avaliador import Avaliador
from model.carregador import Carregador
from model.modelo import Model

# To run: pytest -v test_modelos.py

# Instanciação das Classes
carregador = Carregador()
modelo = Model()
avaliador = Avaliador()

# Parâmetros    
url_dados = "https://raw.githubusercontent.com/Murilo-Nogueira00/br2023_dataset/main/dados_times.csv"
colunas = ['TIME_CASA', 'TIME_FORA', 'CHUTES_NO_GOL_TIME_CASA', 'CHUTES_NO_GOL_TIME_FORA',
           'JOGADORES_EXPULSOS_TIME_CASA', 'JOGADORES_EXPULSOS_TIME_FORA', 'pedi', 'age', 'class']

# Carga dos dados
dataset = carregador.carregar_dados(url_dados, colunas)

# Separando em dados de entrada e saída
X = dataset.iloc[:, 0:-1]
Y = dataset.iloc[:, -1]
    
# Método para testar o modelo de Regressão Logística a partir do arquivo correspondente
# O nome do método a ser testado necessita começar com "test_"
def test_modelo_lr():  
    # Importando o modelo de regressão logística
    lr_path = 'ml_model/predict_soccer.joblib'
    modelo_lr = modelo.carrega_modelo(lr_path)

    # Obtendo as métricas da Regressão Logística
    acuracia_lr, recall_lr, precisao_lr, f1_lr = avaliador.avaliar(modelo_lr, X, Y)
    
    # Testando as métricas da Regressão Logística 
    # Modifique as métricas de acordo com seus requisitos
    assert acuracia_lr >= 0.01 
    assert recall_lr >= 0.01 
    assert precisao_lr >= 0.01 
    assert f1_lr >= 0.01 
 
# Método para testar modelo KNN a partir do arquivo correspondente
# def test_modelo_knn():
#     # Importando modelo de KNN
#     knn_path = 'ml_model/diabetes_knn.pkl'
#     modelo_knn = modelo.carrega_modelo(knn_path)

#     # Obtendo as métricas do KNN
#     acuracia_knn, recall_knn, precisao_knn, f1_knn = avaliador.avaliar(modelo_knn, X, Y)
    
#     # Testando as métricas do KNN
#     # Modifique as métricas de acordo com seus requisitos
#     assert acuracia_knn >= 0.75
#     assert recall_knn >= 0.5 
#     assert precisao_knn >= 0.5 
#     assert f1_knn >= 0.5 
    

