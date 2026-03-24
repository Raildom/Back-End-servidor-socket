# Servidor de Monitoramento Pervasivo (Socket + FastAPI)

1. Um servidor TCP Socket puro na porta 5000 (para receber os dados dos sensores do Android).
2. Uma API Web em FastAPI na porta 8000 (para facilitar a descoberta do IP pelo React Native).

## Estrutura do Projeto

```
Back-End-servidor-socket/
├── server/
│   ├── __init__.py          
│   ├── app.py               # API Web FastAPI (rotas)
│   ├── config.py            # Configuracoes (host, porta, log)
│   ├── handler.py           # Decodificacao e exibicao
│   ├── logger.py            # Salva leituras com timestamp
│   ├── socket_server.py     # Servidor TCP socket (raw TCP)
│   └── utils.py             # Descoberta do IP local
├── logs/
│   └── sensor_log.txt       # Arquivo de gravacoes
├── main.py                  # Ponto original de chamada
└── README.md
```

## Como Rodar o Servidor

### 1. Instalar as dependencias
### 1. Pre-requisitos
- Python instalado. Apenas bibliotecas nativas sao utilizadas (nao precisa de pip install).

### 2. Executar
```bash
python main.py
```

O terminal exibira a inicializacao do servidor e aguardara conexoes na porta **5000**.

## Integracao com Front-End (React Native)

Para conectar do seu app React Native a porta 5000 do TCP Socket, utilize uma biblioteca nativa como `react-native-tcp-socket` e conecte-se diretamente no IP local (IPv4) da sua maquina roteadora/PC.

## Formato da Mensagem via TCP Socket

O app deve enviar via RAW TCP uma string com o seguinte conteudo:

```
bateria:85;lat:-23.5505;lon:-46.6333
```


## Exemplo de Log (`logs/sensor_log.txt`)

```
[2026-03-24 10:55:00] Bateria: 85% | Lat: -23.5505 | Lon: -46.6333
```

## Configuracao

Edite `server/config.py` para alterar a porta TCP e outras configuracoes.
