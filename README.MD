#  Job Scraper RPA (Python + Selenium)

Automação desenvolvida em Python para **coleta de vagas de emprego** em múltiplos portais, com análise de aderência baseada em palavras-chave e geração automática de relatório em Excel.

---

##  Objetivo

Centralizar e automatizar a busca de vagas com foco em:

- Python
- RPA / Automação
- Backend / APIs
- Dados (ETL, Pandas)

Gerando um ranking das melhores oportunidades com base em um **score de aderência**.

---

##  Tecnologias utilizadas

- Python 3.x
- Selenium
- BeautifulSoup
- Pandas
- WebDriver Manager
- Logging

---

#  Job Scraper RPA (Python + Selenium)

Automação desenvolvida em Python para **coleta de vagas de emprego** em múltiplos portais, com análise de aderência baseada em palavras-chave e geração automática de relatório em Excel.

---

##  Objetivo

Centralizar e automatizar a busca de vagas com foco em:

- Python
- RPA / Automação
- Backend / APIs
- Dados (ETL, Pandas)

Gerando um ranking das melhores oportunidades com base em um **score de aderência**.

---

##  Tecnologias utilizadas

- Python 3.x
- Selenium
- BeautifulSoup
- Pandas
- WebDriver Manager
- Logging

---



##  Como funciona

### 1. Inicialização
- O script inicia o navegador automaticamente via Selenium.
- Configura logs para rastrear a execução.

### 2. Coleta de vagas

- LinkedIn  
- Indeed  
- Glassdoor  
- InfoJobs  
- Catho  

---

### 3. Cálculo de score

Baseado em palavras-chave como Python, RPA, Backend, APIs, etc.

---

### 4. Filtro

Apenas vagas com score >= 80 são consideradas.

---

### 5. Output

- Excel automático
- Ordenado por aderência
- Links clicáveis
- Abas separadas por site

---

## Como executar

```bash
python -m venv venv
source venv/bin/activate
pip install selenium webdriver-manager pandas beautifulsoup4
python main.py
```

---

---

##  Como funciona

### 1. Inicialização
- O script inicia o navegador automaticamente via Selenium.
- Configura logs para rastrear a execução.

### 2. Coleta de vagas

- LinkedIn  
- Indeed  
- Glassdoor  
- InfoJobs  
- Catho  

---

### 3. Cálculo de score

Baseado em palavras-chave como Python, RPA, Backend, APIs, etc.

---

### 4. Filtro

Apenas vagas com score >= 80 são consideradas.

---

##  Estrutura do projeto

```
projeto/
|-- scrapers/
|   |-- linkedin.py
|   |-- indeed.py
|   |-- glassdoor.py
|   |-- infojobs.py
|   `-- catho.py
|-- logs/
|-- output/
|-- config.py
|-- logger.py
|-- scorer.py
|-- utils.py
`-- main.py
```

### 5. Output

- Excel automático
- Ordenado por aderência
- Links clicáveis
- Abas separadas por site

---

## Como executar

```bash
python -m venv venv
source venv/bin/activate
pip install selenium webdriver-manager pandas beautifulsoup4
python main.py
```

---

