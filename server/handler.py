"""
Módulo de processamento — decodifica e exibe os dados recebidos do app Android.
"""

from datetime import datetime


def parse_message(raw: str) -> dict:
    """
    Decodifica a string recebida do app Android.

    Formato esperado:
        "bateria:85;lat:-23.5505;lon:-46.6333"

    Args:
        raw: String bruta recebida via socket.

    Returns:
        Dicionário com os dados extraídos.
        Ex: {"bateria": "85", "lat": "-23.5505", "lon": "-46.6333"}
    """
    data = {}

    try:
        # Remove espaços em branco e quebras de linha
        raw = raw.strip()

        # Separa os pares chave:valor por ";"
        pairs = raw.split(";")

        for pair in pairs:
            if ":" in pair:
                # Divide apenas na primeira ocorrência de ":"
                key, value = pair.split(":", 1)
                data[key.strip().lower()] = value.strip()

    except Exception as e:
        print(f"[ERRO] Falha ao decodificar mensagem: {e}")
        print(f"[ERRO] Mensagem recebida: {raw}")

    return data


def display_data(data: dict, addr: tuple):
    """
    Exibe os dados recebidos no console de forma formatada e colorida.

    Args:
        data: Dicionário com os dados do sensor.
        addr: Tupla (IP, Porta) do cliente conectado.
    """
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    bateria = data.get("bateria", "N/A")
    lat = data.get("lat", "N/A")
    lon = data.get("lon", "N/A")

    # Cores ANSI para o terminal
    CYAN = "\033[96m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    MAGENTA = "\033[95m"
    RESET = "\033[0m"
    BOLD = "\033[1m"

    print()
    print(f"{CYAN}{'=' * 55}{RESET}")
    print(f"{BOLD}{GREEN}  [SENSOR] DADOS RECEBIDOS{RESET}")
    print(f"{CYAN}{'=' * 55}{RESET}")
    print(f"  {YELLOW}Timestamp :{RESET} {timestamp}")
    print(f"  {YELLOW}Cliente   :{RESET} {addr[0]}:{addr[1]}")
    print(f"  {MAGENTA}Bateria   :{RESET} {bateria}%")
    print(f"  {MAGENTA}Latitude  :{RESET} {lat}")
    print(f"  {MAGENTA}Longitude :{RESET} {lon}")
    print(f"{CYAN}{'=' * 55}{RESET}")
    print()
