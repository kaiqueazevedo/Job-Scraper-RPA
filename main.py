import os
import pandas as pd
from datetime import datetime

from utils import iniciar_driver
from scrapers import linkedin, indeed, glassdoor, infojobs, catho
from logger import setup_logger

logger = setup_logger()

def main():
    logger.info(" Iniciando execução do robô")

    driver = iniciar_driver()
    todas_vagas = []

    try:
        logger.info(" Buscando vagas no LinkedIn")
        todas_vagas += linkedin.buscar(driver)

        logger.info(" Buscando vagas no Indeed")
        todas_vagas += indeed.buscar(driver)

        logger.info(" Buscando vagas no Glassdoor")
        todas_vagas += glassdoor.buscar(driver)

        logger.info(" Buscando vagas no InfoJobs")
        todas_vagas += infojobs.buscar(driver)

        logger.info("Buscando vagas no Catho")
        todas_vagas += catho.buscar(driver)

    except Exception as e:
        logger.error(f" Erro durante execução: {str(e)}")

    finally:
        driver.quit()
        logger.info("Navegador fechado")

    df = pd.DataFrame(todas_vagas)

    #  GARANTE QUE A PASTA EXISTE
    os.makedirs("output", exist_ok=True)

    if not df.empty:
        logger.info(f"Total de vagas encontradas: {len(df)}")

        #  Renomeia colunas
        df = df.rename(columns={
            "titulo": "Título",
            "score": "% Aderência",
            "link": "Link",
            "site": "Portal"
        })

        #  Ordena
        df = df.sort_values(by="% Aderência", ascending=False)

        #  Link clicável no Excel
        df["Link"] = df["Link"].apply(lambda x: f'=HYPERLINK("{x}", "Abrir vaga")')

        #  Nome com timestamp
        nome_arquivo = f"output/vagas_{datetime.now().strftime('%Y%m%d_%H%M')}.xlsx"

        #  Salvar com abas
        with pd.ExcelWriter(nome_arquivo) as writer:
            # Aba geral
            df.to_excel(writer, sheet_name="Todas", index=False)

            # Abas por portal
            for portal in df["Portal"].unique():
                df_portal = df[df["Portal"] == portal]
                df_portal.to_excel(writer, sheet_name=portal, index=False)

        logger.info(f" Planilha gerada: {nome_arquivo}")
        print(f" Planilha gerada: {nome_arquivo}")

    else:
        logger.warning(" Nenhuma vaga encontrada.")
        print(" Nenhuma vaga encontrada.")

    logger.info(" Execução finalizada")


if __name__ == "__main__":
    main()