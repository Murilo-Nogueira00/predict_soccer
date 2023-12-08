from flask_openapi3 import OpenAPI, Info, Tag
from flask import jsonify, redirect

from model.modelo import Model
from schemas import *
from flask_cors import CORS


# Instanciando o objeto OpenAPI
info = Info(title="Minha API", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

# Definindo tags para agrupamento das rotas
home_tag = Tag(name="Documentação", description="Seleção de documentação: Swagger, Redoc ou RapiDoc")
partida_tag = Tag(name="Partida", description="Adição de times para simulação de uma partida e retorno de um vencedor")


# Rota home
@app.get('/', tags=[home_tag])
def home():
    """Redireciona para /openapi, tela que permite a escolha do estilo de documentação.
    """
    return redirect('/openapi')

# Rota de uma nova partida
@app.post('/partida', tags=[partida_tag],
          responses={"200": PartidaViewSchema, "400": ErrorSchema, "409": ErrorSchema})
def predict(form: PartidaSchema):
    """Escolhe dois times para realizar uma partida
    
    Args:
        sigla do time da casa (str): Informa a sigla do time que vai jogar
        sigla do time visitante (str): Informa a sigla do time que vai jogar
        
    Returns:
        dict: vencedor da partida e probabilidades do resultado
    """
    
    # Carregando modelo
    ml_path = 'ml_model/predict_soccer_svm.joblib'
    model = Model()
    modelo = model.carrega_modelo(ml_path)

    vencedor, probabilidades = Model.preditor(modelo, form)

    probabilidades_formatadas = [
        float(round(probabilidade*100, 2)) for probabilidade in probabilidades.flatten()
    ]

    return jsonify({"vencedor": vencedor, "probabilidades": probabilidades_formatadas})
