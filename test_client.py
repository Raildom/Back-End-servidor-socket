import socket
import urllib.request
import json
import os

def get_battery_linux():
    try:
        with open('/sys/class/power_supply/BAT0/capacity', 'r') as f:
            return f.read().strip()
    except Exception:
        try:
            with open('/sys/class/power_supply/BAT1/capacity', 'r') as f:
                return f.read().strip()
        except Exception:
            return "100" # Retorna 100 como padrão caso falhe

def get_location_by_ip():
    # Usa um serviço público de geolocalização via IP
    try:
        with urllib.request.urlopen("https://ipinfo.io/json", timeout=5) as response:
            data = json.loads(response.read().decode('utf-8'))
            loc = data.get("loc", "0,0")
            lat, lon = loc.split(',')
            return lat.strip(), lon.strip()
    except Exception as e:
        print(f"Erro ao obter localização: {e}")
        return "-23.5505", "-46.6333" # Fallback para o valor antigo (SP)

def send_test_request():
    host = "127.0.0.1"
    port = 5000
    
    bateria = get_battery_linux()
    lat, lon = get_location_by_ip()
    
    message = f"bateria:{bateria};lat:{lat};lon:{lon}"

    print(f"Conectando ao servidor em {host}:{port}...")
    try:
        # Cria o socket TCP
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((host, port))
            print(f"Enviando: {message}")
            
            # Envia a mensagem codificada em bytes
            s.sendall(message.encode('utf-8'))
            
            # Aguarda e exibe a resposta do servidor
            data = s.recv(1024)
            print(f"Resposta do servidor: {data.decode('utf-8')}")
            
    except ConnectionRefusedError:
        print("Erro: Não foi possível conectar. Verifique se o servidor está rodando (python main.py).")
    except Exception as e:
        print(f"Erro inesperado: {e}")

if __name__ == "__main__":
    send_test_request()