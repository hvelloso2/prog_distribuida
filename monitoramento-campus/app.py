import streamlit as st
import requests

API_URL = "http://localhost:5000"

st.set_page_config(page_title="Painel de Monitoramento", layout="wide")
st.title("🌐 Painel para controle de ambiente)")

# --- Função que busca os dados da API com cache de 5 segundos ---
@st.cache_data(ttl=5)
def fetch_dados():
    res = requests.get(f"{API_URL}/leituras")
    return res.json()

# --- Buscar dados ---
try:
    dados = fetch_dados()
except Exception as e:
    st.error(f"Erro ao conectar com a API Flask: {e}")
    st.stop()

st.markdown("### 🟢 Backend Flask conectado")

# --- Exibir os dados por ambiente ---
for ambiente, sensores in dados.items():
    st.markdown(f"### 🏷️ {ambiente}")
    col1, col2, col3 = st.columns(3)

    temp = sensores.get("temperatura", "N/A")
    lum = sensores.get("luminosidade", "N/A")
    pres = sensores.get("presenca", "N/A")

    col1.metric(" Temperatura", f"{temp}°C" if temp != "N/A" else temp,
                delta="🔥" if isinstance(temp, (int, float)) and temp > 28 else "OK")
    col2.metric(" Luminosidade", f"{lum} lux" if lum != "N/A" else lum)
    col3.metric(" Presença", "✅ Sim" if pres is True else "❌ Não" if pres is False else pres)

    # --- Botões de comando ---
    with st.expander(f" Controles de {ambiente}"):
        if st.button(" Ligar Ar", key=f"ar-{ambiente}"):
            comando = {"ambiente": ambiente, "atuador": "ar_condicionado", "comando": "ligar"}
            requests.post(f"{API_URL}/comando", json=comando)
            st.success("Comando enviado")

        if st.button(" Acender Luz", key=f"luz-{ambiente}"):
            comando = {"ambiente": ambiente, "atuador": "luz", "comando": "ligar"}
            requests.post(f"{API_URL}/comando", json=comando)
            st.success("Comando enviado")

        if st.button(" Ativar Alarme", key=f"alarme-{ambiente}"):
            comando = {"ambiente": ambiente, "atuador": "alarme", "comando": "ativar"}
            requests.post(f"{API_URL}/comando", json=comando)
            st.success("Comando enviado")
