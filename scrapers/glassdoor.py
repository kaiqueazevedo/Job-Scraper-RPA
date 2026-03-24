import time
from bs4 import BeautifulSoup
from scorer import calcular_score
from config import SCORE_MINIMO

def buscar(driver):
    vagas = []

    driver.get("https://www.glassdoor.com.br/Vaga/python-vagas-SRCH_KO0,6.htm")
    time.sleep(5)

    soup = BeautifulSoup(driver.page_source, "html.parser")

    for card in soup.find_all("a"):
        titulo = card.text.strip()

        if "python" in titulo.lower():
            link = "https://www.glassdoor.com.br" + card.get("href", "")
            score = calcular_score(titulo)

            if score >= SCORE_MINIMO:
                vagas.append({
                    "site": "Glassdoor",
                    "titulo": titulo,
                    "link": link,
                    "score": score
                })

    return vagas