import os

# Endereço do servidor — 0.0.0.0 aceita conexões de qualquer interface
HOST = "10.24.105.135"

# Porta TCP padrão
PORT = 5000

# Tamanho máximo do buffer de recepção (bytes)
BUFFER_SIZE = 1024

# Diretório para salvar os arquivos de log
LOG_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "logs")

# Nome do arquivo de log
LOG_FILE = "sensor_log.txt"
