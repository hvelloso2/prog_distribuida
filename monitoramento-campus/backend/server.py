from flask import Flask, jsonify, request
from threading import Thread
from backend.state import get_leituras
from backend.kafka_consumer import iniciar_consumidor
from kafka import KafkaProducer
import json

app = Flask(__name__)

# Kafka Producer para comandos
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# Thread Kafka
def iniciar_kafka_em_thread():
    Thread(target=iniciar_consumidor, daemon=True).start()

# Rota GET: retorna todas as leituras
@app.route('/leituras', methods=['GET'])
def obter_leituras():
    return jsonify(get_leituras())

# Rota POST: envia comando para o Kafka
@app.route('/comando', methods=['POST'])
def enviar_comando():
    dados = request.get_json()
    if not dados or 'ambiente' not in dados or 'atuador' not in dados or 'comando' not in dados:
        return jsonify({"erro": "Formato inválido"}), 400

    producer.send('comandos.atuadores', dados)
    return jsonify({"status": "Comando enviado", "dados": dados})

if __name__ == '__main__':
    iniciar_kafka_em_thread()
    app.run(host='0.0.0.0', port=5000, debug=True)
