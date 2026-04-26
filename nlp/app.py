from flask import Flask, request, jsonify
import logging
import os

from flasgger import Swagger
from flask import redirect

from nlp import analisar_texto
from identificacao import identificar_intencao
from base_conhecimento import base_manager
from busca import formatar_resposta

app = Flask(__name__)

swagger = Swagger(app)

logging.basicConfig(level=logging.INFO)

# Carregar base
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CAMINHO_BASE = os.path.join(BASE_DIR, "dados", "edital.txt")

base_manager.carregar(CAMINHO_BASE)

print("Base carregada com sucesso!")
print("Arquivo usado:", CAMINHO_BASE)


@app.route('/processar', methods=['POST'])
def processar():
    """
    Processa pergunta do usuário
    ---
    tags:
      - Chatbot
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          properties:
            mensagem:
              type: string
              example: Quando começam as inscrições?
    responses:
      200:
        description: Resposta do chatbot
    """

    dados = request.get_json()
    mensagem = dados.get("mensagem")

    if not mensagem:
        return jsonify({"erro": "Mensagem obrigatória"}), 400

    # NLP
    resultado_nlp = analisar_texto(mensagem)

    # Intenção
    intencao = identificar_intencao(mensagem)

    # Busca
    busca = base_manager.buscar(
        resultado_nlp["doc"],
    )

    resposta = formatar_resposta(busca)

    return jsonify({
        "entrada": mensagem,
        "resposta": resposta
    })


@app.route('/status', methods=['GET'])
def status():
    """
    Verifica status do sistema
    ---
    tags:
      - Sistema
    responses:
      200:
        description: Sistema online
    """
    return jsonify({
        "status": "online"
    })

@app.route("/")
def home():
    return redirect("/apidocs/")


if __name__ == "__main__":
    print("\n" + "="*60)
    print("🤖 CHATBOT IFES - API")
    print("="*60)
    print("🔗 API: http://localhost:5000")
    print("📖 Swagger: http://localhost:5000/apidocs/")
    print("="*60 + "\n")

    app.run(debug=True, port=5000)