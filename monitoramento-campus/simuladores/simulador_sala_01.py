import socket
import time
import json
from datetime import datetime
import random

SERVER_IP = '127.0.0.1'
SERVER_PORT = 5070
AMBIENTE = 'Sala101'

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def gerar_temperatura():
    return round(random.uniform(22.0, 32.0), 2)

def gerar_luminosidade():
    return random.randint(100, 900)  # em lux

def gerar_presenca():
    return random.choice([True, False])

while True:
    agora = datetime.utcnow().isoformat()

    sensores = [
        {"tipo_sensor": "temperatura", "valor": gerar_temperatura()},
        {"tipo_sensor": "luminosidade", "valor": gerar_luminosidade()},
        {"tipo_sensor": "presenca", "valor": gerar_presenca()},
    ]

    for sensor in sensores:
        dado = {
            "ambiente": AMBIENTE,
            "tipo_sensor": sensor["tipo_sensor"],
            "valor": sensor["valor"],
            "timestamp": agora
        }
        mensagem = json.dumps(dado).encode('utf-8')
        sock.sendto(mensagem, (SERVER_IP, SERVER_PORT))
        print("Dado enviado:", dado)
        time.sleep(1)  # intervalo entre sensores
