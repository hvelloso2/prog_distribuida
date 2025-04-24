from kafka import KafkaConsumer
import json

TOPICO = 'sensores.temperatura'

consumer = KafkaConsumer(
    TOPICO,
    bootstrap_servers='localhost:9092',
    value_deserializer=lambda m: json.loads(m.decode('utf-8')),
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='grupo-temperatura'
)

print(f"[CONSUMIDOR] Aguardando dados no tópico '{TOPICO}'...")

for mensagem in consumer:
    dado = mensagem.value
    ambiente = dado['ambiente']
    valor = dado['valor']
    timestamp = dado['timestamp']

    print(f"[{ambiente}] Temperatura: {valor}°C em {timestamp}")

    if valor > 28:
        print(f"  ALERTA: Temperatura elevada em {ambiente} ({valor}°C)")
