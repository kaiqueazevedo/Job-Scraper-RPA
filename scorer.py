import re


# CARREGAR CURRÍCULO

def carregar_curriculo():
    with open("curriculo.txt", "r", encoding="utf-8") as f:
        return f.read().lower()

CURRICULO = carregar_curriculo()


# STOPWORDS (PALAVRAS IRRELEVANTES)


STOPWORDS = [
    "de", "da", "do", "e", "em", "para", "com",
    "uma", "um", "o", "a", "os", "as",
    "no", "na", "nos", "nas",
    "por", "ao", "aos", "das", "dos",
    "que", "se", "como", "mais", "ou"
]


# LIMPEZA DE TEXTO


def limpar_texto(texto):
    texto = texto.lower()
    texto = re.sub(r'[^a-zA-Z0-9\s]', ' ', texto)
    return texto


# EXTRAIR PALAVRAS RELEVANTES


def extrair_palavras(texto):
    palavras = limpar_texto(texto).split()

    palavras_filtradas = [
        p for p in palavras
        if p not in STOPWORDS and len(p) > 2
    ]

    return list(set(palavras_filtradas))


# CALCULAR SCORE (LÓGICA NOVA)


def calcular_score(texto_vaga, debug=False):
    palavras_vaga = extrair_palavras(texto_vaga)

    if not palavras_vaga:
        return 0

    correspondencias = []

    for palavra in palavras_vaga:
        if palavra in CURRICULO:
            correspondencias.append(palavra)

    score = (len(correspondencias) / len(palavras_vaga)) * 100

    if debug:
        print("\n==========================")
        print(f"VAGA: {texto_vaga}")
        print(f"PALAVRAS VAGA: {palavras_vaga}")
        print(f"MATCH: {correspondencias}")
        print(f"SCORE: {int(score)}%")
        print("==========================\n")

    return int(score)