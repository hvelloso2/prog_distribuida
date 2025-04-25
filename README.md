# Plataforma de Monitoramento de Ambientes Inteligentes (Simulada)

Este projeto simula uma plataforma distribuída para **monitoramento e controle de ambientes inteligentes** em um campus universitário, utilizando sensores virtuais e comandos remotos. Foi desenvolvido como parte de uma atividade prática de sistemas distribuídos.

---

## 🧠 Tecnologias Utilizadas

- **Flask** — backend que centraliza os dados dos sensores e recebe comandos
- **Streamlit** — frontend leve para visualização dos ambientes e controle
- **Kafka + UDP Sockets** — simulação de comunicação assíncrona entre sensores e gateway
- **Python + Threading** — gerenciamento de tarefas simultâneas

---


## ▶️ Como Executar

 1.Instale as dependências:
 
pip install streamlit flask kafka-python requests

 2.Inicie os servidores
 
docker compose up -d   # (para rodar o Kafka e Zookeeper)

# Backend Flask
python -m backend.server

# Simulador
python simuladores/simulador_sala101.py

# Gateway UDP
python gateway/gateway_udp.py

# Painel de visualização
streamlit run app.py
