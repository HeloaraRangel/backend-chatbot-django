"""
Arquivo responsável pelo pré-processamento do texto.

Agora integrado com spaCy:
- Normalização
- Tokenização
- Lemmatização
"""

import re
import unicodedata

from nlp.nlp import analisar_texto


def normalizar_texto(texto):
    """
    Normaliza texto:

    - minúsculas
    - remove acentos
    - remove caracteres inválidos
    """

    # Minúsculas
    texto = texto.lower()

    # Remove acentos
    texto = unicodedata.normalize('NFKD', texto)
    texto = texto.encode('ascii', 'ignore').decode('utf-8')

    # Remove caracteres especiais
    texto = re.sub(r'[^a-zA-Z0-9\s]', '', texto)

    return texto


def preprocessar(texto):
    """
    Pré-processamento principal.

    Usa spaCy para gerar tokens lematizados.
    """

    # Processamento com spaCy
    resultado = analisar_texto(texto)

    # Normalização básica
    texto_normalizado = normalizar_texto(texto)

    return {
        "texto_normalizado": texto_normalizado,
        "tokens": resultado["tokens"],
        "doc": resultado["doc"]
    }


def preprocessar_para_api(texto):
    """
    Função usada pela API.

    Retorna estrutura padronizada.
    """

    resultado = preprocessar(texto)

    return {
        "texto_original": texto,
        "texto_normalizado": resultado["texto_normalizado"],
        "tokens": resultado["tokens"],
        "num_tokens": len(resultado["tokens"]),
        "sucesso": len(resultado["tokens"]) > 0
    }


def preprocessar_passo_a_passo(texto):
    """
    Versão detalhada para debug.

    Mostra cada etapa.
    """

    print("\nENTRADA:")
    print(texto)

    texto_normalizado = normalizar_texto(texto)

    print("\nTEXTO NORMALIZADO:")
    print(texto_normalizado)

    resultado = analisar_texto(texto_normalizado)

    print("\nTOKENS:")
    print(resultado["tokens"])

    print("\nENTIDADES:")
    print(resultado["entidades"])

    return {
        "texto_original": texto,
        "texto_normalizado": texto_normalizado,
        "tokens_finais": resultado["tokens"],
        "entidades": resultado["entidades"]
    }