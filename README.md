# Servidor de Monitoramento Pervasivo (TCP Socket)

Servidor TCP Socket para receber dados de sensores (bateria e localização) de dispositivos móveis.

## Estrutura do Projeto

```
Back-End-servidor-socket/
├── server/
│   ├── config.py            # Configurações (host, porta, log)
│   ├── handler.py           # Decodificação e exibição dos dados
│   ├── logger.py            # Salva leituras com timestamp
│   └── socket_server.py     # Servidor TCP socket
├── logs/
│   └── sensor_log.txt       # Arquivo de gravações
├── main.py                  # Ponto de entrada do servidor
├── test_client.py           # Cliente de teste para o servidor
└── README.md
```

## Como Rodar

### Pré-requisitos

- Python 3.x instalado
- Apenas bibliotecas nativas são utilizadas

### Executar o Servidor

```bash
python main.py
```

O terminal exibirá a inicialização do servidor e aguardará conexões na porta **5000**.

### Executar o Cliente de Teste

Em outro terminal:

```bash
python test_client.py
```

O cliente de teste obtém automaticamente a bateria do sistema (Linux) e a localização via IP.

## Exemplo de Log (`logs/sensor_log.txt`)

```
[2026-03-24 10:55:00] Bateria: 85% | Lat: -23.5505 | Lon: -46.6333
```

## Configuração

OBS.: O ip do servidor deve ser o mesmo do cliente para que a conexão seja estabelecida.

OBS.: O ip do servidor deve se adequar ao ambiente de rede onde o servidor está rodando.
Edite `server/config.py` para alterar:

| Variável    | Descrição                              | Padrão           |
|-------------|----------------------------------------|------------------|
| HOST        | Endereço IP do servidor (EXEMPLO:)               | `10.24.105.135`  |
| PORT        | Porta TCP                              | `5000`           |
| BUFFER_SIZE | Tamanho máximo do buffer de recepção   | `1024`           |
| LOG_DIR     | Diretório para arquivos de log         | `logs/`          |
| LOG_FILE    | Nome do arquivo de log                 | `sensor_log.txt` |
