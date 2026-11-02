# 🌦️ Wheater ETL Pipeline

Pipeline de ETL (Extract, Transform, Load) em Python para coleta, processamento e armazenamento de dados meteorológicos, construído com foco em alta performance utilizando o ecossistema moderno do `uv`.

---

## 🛠️ Tecnologias Utilizadas

* **Python 3.14+**
* **[uv](https://github.com/astral-sh/uv)** (Gerenciador de pacotes e dependências ultrarrápido)
* **Pandas** (Transformação e manipulação de dados)
* **SQLAlchemy & Psycopg2** (Conexão e ORM com PostgreSQL)
* **Requests** (Consumo de APIs de clima)
* **Python-dotenv** (Gerenciamento de variáveis de ambiente)

---

## 📁 Estrutura do Projeto

```text
wheater/
├── .env                  # Variáveis de ambiente (credenciais do banco/API)
├── pyproject.toml        # Configuração do projeto e dependências
├── README.md             # Documentação do projeto
└── src/                  # Código-fonte do ETL
    └── __init__.py