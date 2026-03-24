import time
from bs4 import BeautifulSoup
from scorer import calcular_score
from config import SCORE_MINIMO, MAX_VAGAS_POR_SITE

def buscar(driver):
    vagas = []

    url = "https://www.linkedin.com/jobs/search/?keywords=python%20rpa"
    driver.get(url)
    time.sleep(5)

    soup = BeautifulSoup(driver.page_source, "html.parser")
    cards = soup.find_all("a", class_="base-card__full-link")

    for card in cards[:MAX_VAGAS_POR_SITE]:
        titulo = card.text.strip()
        link = card.get("href")

        score = calcular_score(titulo)

        if score >= SCORE_MINIMO:
            vagas.append({
                "site": "LinkedIn",
                "titulo": titulo,
                "link": link,
                "score": score
            })

    return vagas