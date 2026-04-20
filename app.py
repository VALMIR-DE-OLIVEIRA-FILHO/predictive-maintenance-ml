import streamlit as st
import numpy as np
import pandas as pd
import time
from sklearn.ensemble import RandomForestClassifier

# =========================
# CONFIG
# =========================
st.set_page_config(page_title="Manutenção Preditiva", layout="centered")

# =========================
# SIMULAÇÃO DE DADOS
# =========================
np.random.seed(42)

def gerar_dados(n=500):
    data = pd.DataFrame({
        "temperatura": np.random.normal(70, 10, n),
        "vibracao": np.random.normal(5, 2, n),
        "pressao": np.random.normal(30, 5, n),
        "corrente": np.random.normal(10, 3, n)
    })

    data["falha"] = ((data["temperatura"] > 85) & (data["vibracao"] > 7)).astype(int)
    return data

data = gerar_dados()

# =========================
# TREINAMENTO DO MODELO
# =========================
X = data.drop("falha", axis=1)
y = data["falha"]

model = RandomForestClassifier()
model.fit(X, y)

# =========================
# SISTEMA ESPECIALISTA
# =========================
def explicacao(temp, vib):
    if temp > 85 and vib > 7:
        return "🔴 Alto risco: superaquecimento + vibração excessiva"
    elif temp > 85:
        return "🟠 Risco moderado: temperatura elevada"
    elif vib > 7:
        return "🟠 Risco moderado: vibração alta"
    else:
        return "🟢 Operação normal"

# =========================
# FUNÇÃO DE SIMULAÇÃO REALISTA
# =========================
def gerar_leitura():
    cenario = np.random.choice(
        ["normal", "moderado", "critico"],
        p=[0.5, 0.3, 0.2]
    )

    if cenario == "normal":
        temperatura = np.random.normal(65, 5)
        vibracao = np.random.normal(4, 1)
        pressao = np.random.normal(28, 3)
        corrente = np.random.normal(9, 2)

    elif cenario == "moderado":
        temperatura = np.random.normal(85, 5)
        vibracao = np.random.normal(6.5, 1)
        pressao = np.random.normal(35, 4)
        corrente = np.random.normal(12, 2)

    else:  # crítico
        temperatura = np.random.normal(100, 5)
        vibracao = np.random.normal(9, 2)
        pressao = np.random.normal(45, 5)
        corrente = np.random.normal(15, 3)

    # limites
    temperatura = np.clip(temperatura, 40, 120)
    vibracao = np.clip(vibracao, 0, 15)
    pressao = np.clip(pressao, 10, 60)
    corrente = np.clip(corrente, 1, 20)

    return temperatura, vibracao, pressao, corrente, cenario

# =========================
# UI
# =========================
st.title("🏭 Sistema de Manutenção Preditiva com IA")
st.markdown("Simulação de falhas industriais usando Machine Learning + Sistema Especialista")

modo = st.radio("Modo de operação", ["Manual", "Automático"])

st.subheader("🔧 Dados da Máquina")

# =========================
# MODO MANUAL
# =========================
if modo == "Manual":
    temperatura = st.slider("Temperatura (°C)", 40, 120, 70)
    vibracao = st.slider("Vibração (mm/s)", 0.0, 15.0, 5.0)
    pressao = st.slider("Pressão (bar)", 10, 60, 30)
    corrente = st.slider("Corrente (A)", 1, 20, 10)

    if st.button("🔍 Analisar Máquina"):
        entrada = np.array([[temperatura, vibracao, pressao, corrente]])
        prob = model.predict_proba(entrada)[0][1]
        risco = prob * 100

        st.subheader("📊 Resultado")

        if risco > 70:
            st.error(f"🔴 Risco ALTO: {risco:.2f}%")
        elif risco > 40:
            st.warning(f"🟠 Risco MODERADO: {risco:.2f}%")
        else:
            st.success(f"🟢 Risco BAIXO: {risco:.2f}%")

        st.subheader("🧠 Diagnóstico")
        st.info(explicacao(temperatura, vibracao))

# =========================
# MODO AUTOMÁTICO
# =========================
else:
    if "historico" not in st.session_state:
        st.session_state.historico = pd.DataFrame(
            columns=["temperatura", "vibracao", "pressao", "corrente", "risco"]
        )

    velocidade = st.slider("⏱️ Intervalo (segundos)", 0.5, 3.0, 1.0)

    if st.button("▶️ Iniciar Simulação"):
        placeholder = st.empty()

        for i in range(50):  # mais ciclos
            temperatura, vibracao, pressao, corrente, cenario = gerar_leitura()

            entrada = np.array([[temperatura, vibracao, pressao, corrente]])
            prob = model.predict_proba(entrada)[0][1]
            risco = prob * 100

            novo = pd.DataFrame([{
                "temperatura": temperatura,
                "vibracao": vibracao,
                "pressao": pressao,
                "corrente": corrente,
                "risco": risco
            }])

            st.session_state.historico = pd.concat(
                [st.session_state.historico, novo],
                ignore_index=True
            )

            # limitar histórico
            st.session_state.historico = st.session_state.historico.tail(100)

            with placeholder.container():
                st.subheader(f"📡 Leitura {i+1}")
                st.write(f"📌 Cenário: **{cenario.upper()}**")

                col1, col2 = st.columns(2)

                with col1:
                    st.metric("🌡️ Temperatura", f"{temperatura:.2f} °C")
                    st.metric("⚙️ Vibração", f"{vibracao:.2f}")

                with col2:
                    st.metric("📊 Pressão", f"{pressao:.2f}")
                    st.metric("⚡ Corrente", f"{corrente:.2f}")

                if risco > 70:
                    st.error(f"🔴 Risco ALTO: {risco:.2f}%")
                elif risco > 40:
                    st.warning(f"🟠 Risco MODERADO: {risco:.2f}%")
                else:
                    st.success(f"🟢 Risco BAIXO: {risco:.2f}%")

                st.info(explicacao(temperatura, vibracao))

                st.subheader("📈 Histórico")
                st.line_chart(st.session_state.historico[["temperatura", "vibracao", "risco"]])

            time.sleep(velocidade)