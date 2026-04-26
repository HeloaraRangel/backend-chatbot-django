def detectar_ambiguidade(resultado):

    confianca = resultado.get("confianca", 0)

    if confianca < 0.40:

        return {
            "ambigua": True,
            "mensagem": "Não entendi bem a pergunta."
        }

    if 0.40 <= confianca < 0.70:

        return {
            "ambigua": False,
            "precisa_confirmacao": True
        }

    return {
        "ambigua": False,
        "precisa_confirmacao": False
    }


def solicitar_confirmacao(resultado):

    if not resultado.get("encontrou"):

        return {
            "mensagem": "Pode reformular a pergunta?"
        }

    return {
        "mensagem":
            f"Você quis dizer: '{resultado['resposta']}'?"
    }


def formatar_resposta(resultado):

    if not resultado.get("encontrou"):

        return resultado["resposta"]

    return (
        f"{resultado['resposta']}\n\n"
        f" Origem: {resultado['origem']}\n"
        f" Confiança: {resultado['confianca']:.2%}"
    )