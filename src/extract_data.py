import os
import json
import logging
import requests
from pathlib import Path
from dotenv import load_dotenv

# Carrega as variáveis do ficheiro .env
load_dotenv()

# Configuração do logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

API_KEY = os.getenv("API_KEY")

lat = -8.8383  # Coordenadas de Luanda
lon = 13.2344

# Endpoint correto para a API 2.5 gratuita do OpenWeather
url = f"https://api.openweathermap.org/data/2.5/weather?q=Luanda&appid={API_KEY}&units=metric"


def extract_weather_data(url: str) -> dict:
    if not API_KEY:
        logging.error("A variável API_KEY não está definida no ficheiro .env!")
        return {}

    response = requests.get(url)
    data = response.json()

    if response.status_code != 200:
        logging.error(f"Falha na requisição. Código de status: {response.status_code}")
        logging.error(f"Detalhes do erro: {data}")
        return {}

    if not data:
        logging.warning("Nenhum dado retornado pela API.")
        return {}

    # Definindo o caminho do ficheiro (.data/weather_data.json)
    output_path = Path(".data/weather_data.json")

    # Criando o diretório caso não exista
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

    logging.info(f"Dados salvos com sucesso em {output_path}")
    return data


extract_weather_data(url)
