import streamlit as st
from kafka import KafkaConsumer
import json
import time
from collections import deque

# --- Kafka Consumer Config ---
consumer = KafkaConsumer(
    'sensores.temperatura',
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='latest',
    enable_auto_commit=True,
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

# --- Dados Temporários em Memória ---
ultimas_mensagens = deque(maxlen=10)
ultima_temp_por_ambiente = {}

# --- Interface ---
st.set_page_config(page_title="Painel de Monitoramento", layout="wide")
st.title("📊 Painel de Monitoramento de Temperatura em Tempo Real")

# --- Placeholder da Interface ---
placeholder = st.empty()

# --- Loop contínuo de atualização ---
for mensagem in consumer:
    dados = mensagem.value
    ambiente = dados.get("ambiente", "Desconhecido")
    temperatura = dados.get("valor") or dados.get("temperatura")
    timestamp = dados.get("timestamp", "")

    # Atualiza as estruturas
    if temperatura is not None:
        ultima_temp_por_ambiente[ambiente] = temperatura
    ultimas_mensagens.append({
        "ambiente": ambiente,
        "temperatura": temperatura,
        "timestamp": timestamp
    })

    with placeholder.container():
        # Status do sistema
        st.markdown("### 🟢 Sistema Ativo – Kafka conectado")

        # Layout: cards por ambiente
        st.subheader("🌡️ Últimas Leituras por Ambiente")
        colunas = st.columns(len(ultima_temp_por_ambiente) or 1)

        for i, (amb, temp) in enumerate(ultima_temp_por_ambiente.items()):
            status = "🔥" if temp > 28 else "✅"
            colunas[i].metric(
                label=f"{amb}",
                value=f"{temp}°C",
                delta="ALTA" if temp > 28 else "Normal"
            )

        # Histórico dobrável
        with st.expander("📋 Ver últimas 10 mensagens recebidas"):
            for msg in reversed(ultimas_mensagens):
                st.json(msg)

        st.info("Atualizando em 2 segundos...")
        time.sleep(2)
