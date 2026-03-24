import os
from datetime import datetime

from server.config import LOG_DIR, LOG_FILE


def setup_log_dir():
    """Cria o diretório de logs caso não exista."""
    if not os.path.exists(LOG_DIR):
        os.makedirs(LOG_DIR)
        print(f"[LOG] Diretório de logs criado: {LOG_DIR}")


def save_log(data: dict):
    """
    Salva uma entrada de log no arquivo sensor_log.txt.

    Formato:
        [2026-03-24 10:55:00] Bateria: 85% | Lat: -23.5505 | Lon: -46.6333

    Args:
        data: Dicionário com chaves 'bateria', 'lat', 'lon'.
    """
    setup_log_dir()

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    bateria = data.get("bateria", "N/A")
    lat = data.get("lat", "N/A")
    lon = data.get("lon", "N/A")

    log_entry = f"[{timestamp}] Bateria: {bateria}% | Lat: {lat} | Lon: {lon}\n"

    log_path = os.path.join(LOG_DIR, LOG_FILE)

    with open(log_path, "a", encoding="utf-8") as f:
        f.write(log_entry)

    print(f"[LOG] Entrada salva em {log_path}")
