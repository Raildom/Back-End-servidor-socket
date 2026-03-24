"""
Modulo do servidor TCP socket -- escuta conexoes e orquestra o processamento.
"""

import sys
import socket

from server.config import HOST, PORT, BUFFER_SIZE
from server.handler import parse_message, display_data
from server.logger import save_log


def _print(text=""):
    """Print seguro para Windows (evita erros de encoding)."""
    try:
        print(text)
    except UnicodeEncodeError:
        print(text.encode("ascii", errors="replace").decode("ascii"))


def start_server():
    """
    Inicia o servidor TCP socket.

    Fluxo:
        1. Cria o socket e faz bind em HOST:PORT
        2. Aguarda conexoes em loop continuo
        3. Para cada conexao:
           a. Recebe os dados
           b. Decodifica a mensagem (handler)
           c. Exibe no console (handler)
           d. Salva no log (logger)
    """
    # Cores ANSI
    CYAN = "\033[96m"
    GREEN = "\033[92m"
    RED = "\033[91m"
    YELLOW = "\033[93m"
    RESET = "\033[0m"
    BOLD = "\033[1m"

    # Cria socket TCP (IPv4)
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Permite reutilizar a porta imediatamente apos fechar o servidor
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    try:
        server_socket.bind((HOST, PORT))
        server_socket.listen(5)

        _print()
        _print(f"{CYAN}{'=' * 55}{RESET}")
        _print(f"{BOLD}{GREEN}  [SERVIDOR] MONITORAMENTO PERVASIVO{RESET}")
        _print(f"{CYAN}{'=' * 55}{RESET}")
        _print(f"  {YELLOW}Host:{RESET} {HOST}")
        _print(f"  {YELLOW}Porta:{RESET} {PORT}")
        _print(f"{CYAN}{'=' * 55}{RESET}")
        _print()
        _print(f"{BOLD}{YELLOW}  Aguardando dados dos sensores...{RESET}")
        _print()

        while True:
            # Aceita uma nova conexao
            client_socket, addr = server_socket.accept()
            _print(f"{GREEN}[CONEXAO]{RESET} Cliente conectado: {addr[0]}:{addr[1]}")

            try:
                # Recebe os dados do cliente
                raw_data = client_socket.recv(BUFFER_SIZE)

                if raw_data:
                    # Decodifica bytes para string
                    message = raw_data.decode("utf-8")

                    # Processa a mensagem
                    data = parse_message(message)

                    if data:
                        # Exibe no console
                        display_data(data, addr)

                        # Salva no log
                        save_log(data)

                        # Envia confirmacao ao cliente
                        client_socket.send("OK: Dados recebidos com sucesso!".encode("utf-8"))
                    else:
                        _print(f"{RED}[ERRO]{RESET} Mensagem invalida recebida de {addr}")
                        client_socket.send("ERRO: Formato de mensagem invalido.".encode("utf-8"))
                else:
                    _print(f"{YELLOW}[AVISO]{RESET} Conexao vazia de {addr}")

            except Exception as e:
                _print(f"{RED}[ERRO]{RESET} Erro ao processar dados de {addr}: {e}")

            finally:
                client_socket.close()
                _print(f"{YELLOW}[DESCONEXAO]{RESET} Cliente {addr[0]}:{addr[1]} desconectado")
                _print()

    except KeyboardInterrupt:
        _print(f"\n{YELLOW}[INFO]{RESET} Servidor encerrado pelo usuario.")

    except Exception as e:
        _print(f"{RED}[ERRO FATAL]{RESET} {e}")

    finally:
        server_socket.close()
        _print(f"{CYAN}[INFO]{RESET} Socket do servidor fechado.")
