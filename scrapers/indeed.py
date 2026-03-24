import time
from bs4 import BeautifulSoup
from scorer import calcular_score
from config import SCORE_MINIMO

def buscar(driver):
    vagas = []

    driver.get("https://br.indeed.com/jobs?q=python+rpa")
    time.sleep(5)

    soup = BeautifulSoup(driver.page_source, "html.parser")
    cards = soup.find_all("a")

    for card in cards:
        titulo = card.text.strip()

        if "python" in titulo.lower():
            link = "https://br.indeed.com" + card.get("href", "")
            score = calcular_score(titulo)

            if score >= SCORE_MINIMO:
                vagas.append({
                    "site": "Indeed",
                    "titulo": titulo,
                    "link": link,
                    "score": score
                })

    return vagas