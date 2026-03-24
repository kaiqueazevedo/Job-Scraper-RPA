import time
from bs4 import BeautifulSoup
from scorer import calcular_score
from config import SCORE_MINIMO

def buscar(driver):
    vagas = []

    driver.get("https://www.catho.com.br/vagas/python/")
    time.sleep(5)

    soup = BeautifulSoup(driver.page_source, "html.parser")

    for card in soup.find_all("a"):
        titulo = card.text.strip()

        if "python" in titulo.lower():
            link = card.get("href", "")
            score = calcular_score(titulo)

            if score >= SCORE_MINIMO:
                vagas.append({
                    "site": "Catho",
                    "titulo": titulo,
                    "link": link,
                    "score": score
                })

    return vagas