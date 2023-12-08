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
           'JOGADORES_EXPULSOS_TIME_CASA', 'JOGADORES_EXPULSOS_TIME_FORA', 'VENCEDOR']

# Carga dos dados
dataset = carregador.carregar_dados(url_dados)

# Separando em dados de entrada e saída
X = dataset.iloc[:, 0:-1]
Y = dataset.iloc[:, -1]
    
# Método para testar o modelo de Regressão Logística a partir do arquivo correspondente
def test_modelo_svm():
    # Importando o modelo de regressão logística
    svm_path = 'ml_model/predict_soccer_svm.joblib'
    modelo_svm = modelo.carrega_modelo(svm_path)

    # Obtendo as métricas da Regressão Logística
    acuracia_svm, recall_svm, precisao_svm, f1_svm = avaliador.avaliar(modelo_svm, X, Y)
    
    # Testando as métricas da Regressão Logística 
    # Modifique as métricas de acordo com seus requisitos
    assert acuracia_svm >= 0.485
    assert recall_svm >= 0.33
    assert precisao_svm >= 0.27
    assert f1_svm >= 0.23
 
# # Método para testar modelo KNN a partir do arquivo correspondente
def test_modelo_knn():
    # Importando modelo de KNN
    knn_path = 'ml_model/predict_soccer_knn.joblib'
    modelo_knn = modelo.carrega_modelo(knn_path)

    # Obtendo as métricas do KNN
    acuracia_knn, recall_knn, precisao_knn, f1_knn = avaliador.avaliar(modelo_knn, X, Y)
    
    # Testando as métricas do KNN
    # Modifique as métricas de acordo com seus requisitos

    assert acuracia_knn >= 0.45
    assert recall_knn >= 0.3
    assert precisao_knn >= 0.25
    assert f1_knn >= 0.2
    

