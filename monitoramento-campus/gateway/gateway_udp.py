import socket
import json
from kafka import KafkaProducer

IP = "0.0.0.0"
PORT = 5070
BUFFER_SIZE = 1024

# Configura o produtor Kafka
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

TOPICO_KAFKA = 'sensores.temperatura'

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((IP, PORT))

print(f"[GATEWAY] Enviando dados para Kafka no tópico: {TOPICO_KAFKA}")

while True:
    try:
        data, addr = sock.recvfrom(BUFFER_SIZE)
        mensagem = json.loads(data.decode("utf-8"))

        # Publica no Kafka
        producer.send(TOPICO_KAFKA, mensagem)
        print(f"[Kafka] Publicado: {mensagem}")

    except Exception as e:
        print(f"[ERRO] {e}")
