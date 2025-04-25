from kafka import KafkaConsumer
import json
from backend.state import atualizar_leitura

def iniciar_consumidor():
    consumer = KafkaConsumer(
        'sensores.temperatura',
        bootstrap_servers='localhost:9092',
        auto_offset_reset='latest',
        enable_auto_commit=True,
        value_deserializer=lambda m: json.loads(m.decode('utf-8'))
    )

    for msg in consumer:
        dado = msg.value
        ambiente = dado.get("ambiente", "Desconhecido")
        tipo = dado.get("tipo_sensor", "temperatura")
        valor = dado.get("valor")
        atualizar_leitura(ambiente, tipo, valor)
