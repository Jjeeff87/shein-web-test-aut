import os
import random
import time

import requests
from dotenv import load_dotenv

load_dotenv()


def get_env(key, default=None):
    """Lê uma variável de ambiente (definida no .env ou no sistema), com fallback para um default."""
    return os.getenv(key, default)


def is_url_reachable(url, timeout=10):
    """Verifica se uma URL está acessível (usada para checar se o site está no ar)."""
    try:
        response = requests.get(url, timeout=timeout)
        return response.status_code < 500
    except requests.RequestException:
        return False


def human_type(element, text, min_delay=0.06, max_delay=0.18):
    """Digita um texto caractere por caractere com pequenas pausas aleatórias,
    imitando digitação humana em vez de preencher o campo instantaneamente
    (send_keys(text) de uma vez só). Reduz a chance de o comportamento do
    teste parecer obviamente automatizado.
    """
    for character in text:
        element.send_keys(character)
        time.sleep(random.uniform(min_delay, max_delay))


def human_pause(min_delay=0.4, max_delay=1.2):
    """Pequena pausa aleatória entre ações (ex: depois de um clique, antes do próximo passo),
    simulando o tempo de reação de uma pessoa real."""
    time.sleep(random.uniform(min_delay, max_delay))
