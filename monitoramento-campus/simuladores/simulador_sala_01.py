import socket
import time
import json
from datetime import datetime
import random

SERVER_IP = '127.0.0.1'  # IP do gateway
SERVER_PORT = 5070      # Porta do gateway
AMBIENTE = 'Sala01'

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def gerar_dado_temperatura():
    return round(random.uniform(22.0, 30.0), 2)

while True:
    dado = {
        "ambiente": AMBIENTE,
        "tipo_sensor": "temperatura",
        "valor": gerar_dado_temperatura(),
        "timestamp": datetime.utcnow().isoformat()
    }

    mensagem = json.dumps(dado).encode('utf-8')
    sock.sendto(mensagem, (SERVER_IP, SERVER_PORT))
    print("Dado enviado:", dado)
    time.sleep(5)
