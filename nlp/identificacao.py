from nlp.nlp import analisar_texto

INTENCOES = {
    "CONSULTAR_DATA": ["quando", "data", "prazo", "dia"],
    "CONSULTAR_LOCAL": ["onde", "local", "campus"],
    "CONSULTAR_CUSTO": ["valor", "preço", "taxa"],
    "CONSULTAR_INSCRICAO": ["inscrição", "matrícula"],
    "CONSULTAR_VAGAS": ["vaga", "curso"],
    "LISTAR_DOCUMENTOS": ["documento", "rg", "cpf"],
}


def identificar_intencao(pergunta):

    pergunta = pergunta.lower()

    for intencao, palavras in INTENCOES.items():
        if any(p in pergunta for p in palavras):
            return {
                "intencao": intencao,
                "confianca": 0.8
            }

    return {
        "intencao": "GERAL",
        "confianca": 0.5
    }