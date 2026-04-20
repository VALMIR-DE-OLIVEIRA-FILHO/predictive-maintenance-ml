# 🏭 Sistema de Manutenção Preditiva com IA

Aplicação interativa para simulação de falhas industriais utilizando **Machine Learning** e um  **Sistema Especialista** , desenvolvida com Python e Streamlit.

---

## 🚀 Visão Geral

Este projeto demonstra como técnicas de **Inteligência Artificial** podem ser aplicadas na **Indústria 4.0** para prever falhas em máquinas e apoiar decisões de manutenção.

A aplicação simula dados de sensores industriais em tempo real e utiliza um modelo de Machine Learning para calcular o risco de falha, além de fornecer um diagnóstico interpretável.

---

## 🧠 Tecnologias Utilizadas

* Python
* **Streamlit**
* **NumPy**
* **Pandas**
* **Scikit-learn**

---

## ⚙️ Funcionalidades

* 📊 Simulação de dados industriais
* 🤖 Treinamento de modelo de Machine Learning (Random Forest)
* 🔍 Predição de risco de falha em tempo real
* 🧠 Sistema especialista para explicação do diagnóstico
* 🔄 Simulação automática com múltiplos cenários
* 📈 Histórico de leituras com gráfico dinâmico
* 🎛️ Modo manual e automático

---

## 🏗️ Como Funciona

O sistema utiliza dados simulados com as seguintes variáveis:

* Temperatura
* Vibração
* Pressão
* Corrente

### 📌 Regra de falha simulada:

* Alta temperatura + alta vibração → maior risco de falha

---

## 🤖 Simulação Inteligente

O sistema gera três cenários de operação:

* 🟢 **Normal** — operação estável
* 🟠 **Moderado** — sinais de atenção
* 🔴 **Crítico** — alto risco de falha

Isso garante uma simulação mais realista e demonstra claramente o comportamento do modelo.

---

## 💻 Como Executar o Projeto

### 1. Clonar o repositório

<pre class="overflow-visible! px-0!" data-start="1907" data-end="2006"><div class="relative w-full mt-4 mb-1"><div class=""><div class="relative"><div class="h-full min-h-0 min-w-0"><div class="h-full min-h-0 min-w-0"><div class="border border-token-border-light border-radius-3xl corner-superellipse/1.1 rounded-3xl"><div class="h-full w-full border-radius-3xl bg-token-bg-elevated-secondary corner-superellipse/1.1 overflow-clip rounded-3xl lxnfua_clipPathFallback"><div class="pointer-events-none absolute inset-x-4 top-12 bottom-4"><div class="pointer-events-none sticky z-40 shrink-0 z-1!"><div class="sticky bg-token-border-light"></div></div></div><div class="relative"><div class=""><div class="relative z-0 flex max-w-full"><div id="code-block-viewer" dir="ltr" class="q9tKkq_viewer cm-editor z-10 light:cm-light dark:cm-light flex h-full w-full flex-col items-stretch ͼk ͼy"><div class="cm-scroller"><div class="cm-content q9tKkq_readonly"><span class="ͼs">git</span><span> clone https://github.com/VALMIR-DE-OLIVEIRA-FILHO/predictive-maintenance-ml</span><br/><span class="ͼs">cd</span><span> predictive-maintenance-ml</span></div></div></div></div></div></div></div></div></div></div><div class=""><div class=""></div></div></div></div></div></pre>

---

### 2. Criar ambiente virtual (recomendado)

<pre class="overflow-visible! px-0!" data-start="2058" data-end="2089"><div class="relative w-full mt-4 mb-1"><div class=""><div class="relative"><div class="h-full min-h-0 min-w-0"><div class="h-full min-h-0 min-w-0"><div class="border border-token-border-light border-radius-3xl corner-superellipse/1.1 rounded-3xl"><div class="h-full w-full border-radius-3xl bg-token-bg-elevated-secondary corner-superellipse/1.1 overflow-clip rounded-3xl lxnfua_clipPathFallback"><div class="pointer-events-none absolute inset-x-4 top-12 bottom-4"><div class="pointer-events-none sticky z-40 shrink-0 z-1!"><div class="sticky bg-token-border-light"></div></div></div><div class="relative"><div class=""><div class="relative z-0 flex max-w-full"><div id="code-block-viewer" dir="ltr" class="q9tKkq_viewer cm-editor z-10 light:cm-light dark:cm-light flex h-full w-full flex-col items-stretch ͼk ͼy"><div class="cm-scroller"><div class="cm-content q9tKkq_readonly"><span>python </span><span class="ͼu">-m</span><span> venv venv</span></div></div></div></div></div></div></div></div></div></div><div class=""><div class=""></div></div></div></div></div></pre>

Ativar:

**Windows**

<pre class="overflow-visible! px-0!" data-start="2112" data-end="2145"><div class="relative w-full mt-4 mb-1"><div class=""><div class="relative"><div class="h-full min-h-0 min-w-0"><div class="h-full min-h-0 min-w-0"><div class="border border-token-border-light border-radius-3xl corner-superellipse/1.1 rounded-3xl"><div class="h-full w-full border-radius-3xl bg-token-bg-elevated-secondary corner-superellipse/1.1 overflow-clip rounded-3xl lxnfua_clipPathFallback"><div class="pointer-events-none absolute inset-x-4 top-12 bottom-4"><div class="pointer-events-none sticky z-40 shrink-0 z-1!"><div class="sticky bg-token-border-light"></div></div></div><div class="relative"><div class=""><div class="relative z-0 flex max-w-full"><div id="code-block-viewer" dir="ltr" class="q9tKkq_viewer cm-editor z-10 light:cm-light dark:cm-light flex h-full w-full flex-col items-stretch ͼk ͼy"><div class="cm-scroller"><div class="cm-content q9tKkq_readonly"><span>venv\Scripts\activate</span></div></div></div></div></div></div></div></div></div></div><div class=""><div class=""></div></div></div></div></div></pre>

**Linux / Mac**

<pre class="overflow-visible! px-0!" data-start="2163" data-end="2199"><div class="relative w-full mt-4 mb-1"><div class=""><div class="relative"><div class="h-full min-h-0 min-w-0"><div class="h-full min-h-0 min-w-0"><div class="border border-token-border-light border-radius-3xl corner-superellipse/1.1 rounded-3xl"><div class="h-full w-full border-radius-3xl bg-token-bg-elevated-secondary corner-superellipse/1.1 overflow-clip rounded-3xl lxnfua_clipPathFallback"><div class="pointer-events-none absolute inset-x-4 top-12 bottom-4"><div class="pointer-events-none sticky z-40 shrink-0 z-1!"><div class="sticky bg-token-border-light"></div></div></div><div class="relative"><div class=""><div class="relative z-0 flex max-w-full"><div id="code-block-viewer" dir="ltr" class="q9tKkq_viewer cm-editor z-10 light:cm-light dark:cm-light flex h-full w-full flex-col items-stretch ͼk ͼy"><div class="cm-scroller"><div class="cm-content q9tKkq_readonly"><span class="ͼs">source</span><span> venv/bin/activate</span></div></div></div></div></div></div></div></div></div></div><div class=""><div class=""></div></div></div></div></div></pre>

---

### 3. Instalar dependências

<pre class="overflow-visible! px-0!" data-start="2235" data-end="2294"><div class="relative w-full mt-4 mb-1"><div class=""><div class="relative"><div class="h-full min-h-0 min-w-0"><div class="h-full min-h-0 min-w-0"><div class="border border-token-border-light border-radius-3xl corner-superellipse/1.1 rounded-3xl"><div class="h-full w-full border-radius-3xl bg-token-bg-elevated-secondary corner-superellipse/1.1 overflow-clip rounded-3xl lxnfua_clipPathFallback"><div class="pointer-events-none absolute inset-x-4 top-12 bottom-4"><div class="pointer-events-none sticky z-40 shrink-0 z-1!"><div class="sticky bg-token-border-light"></div></div></div><div class="relative"><div class=""><div class="relative z-0 flex max-w-full"><div id="code-block-viewer" dir="ltr" class="q9tKkq_viewer cm-editor z-10 light:cm-light dark:cm-light flex h-full w-full flex-col items-stretch ͼk ͼy"><div class="cm-scroller"><div class="cm-content q9tKkq_readonly"><span>pip install streamlit numpy pandas scikit-learn</span></div></div></div></div></div></div></div></div></div></div><div class=""><div class=""></div></div></div></div></div></pre>

---

### 4. Executar a aplicação

<pre class="overflow-visible! px-0!" data-start="2329" data-end="2361"><div class="relative w-full mt-4 mb-1"><div class=""><div class="relative"><div class="h-full min-h-0 min-w-0"><div class="h-full min-h-0 min-w-0"><div class="border border-token-border-light border-radius-3xl corner-superellipse/1.1 rounded-3xl"><div class="h-full w-full border-radius-3xl bg-token-bg-elevated-secondary corner-superellipse/1.1 overflow-clip rounded-3xl lxnfua_clipPathFallback"><div class="pointer-events-none absolute inset-x-4 top-12 bottom-4"><div class="pointer-events-none sticky z-40 shrink-0 z-1!"><div class="sticky bg-token-border-light"></div></div></div><div class="relative"><div class=""><div class="relative z-0 flex max-w-full"><div id="code-block-viewer" dir="ltr" class="q9tKkq_viewer cm-editor z-10 light:cm-light dark:cm-light flex h-full w-full flex-col items-stretch ͼk ͼy"><div class="cm-scroller"><div class="cm-content q9tKkq_readonly"><span>streamlit run app.py</span></div></div></div></div></div></div></div></div></div></div><div class=""><div class=""></div></div></div></div></div></pre>

---

## 📊 Exemplo de Saída

O sistema apresenta:

* 🔴 Risco alto / 🟠 moderado / 🟢 baixo
* 📈 Probabilidade de falha (%)
* 🧠 Diagnóstico explicativo
* 📌 Cenário da simulação
* 📊 Gráfico de histórico em tempo real

---

## 🎯 Objetivo do Projeto

Demonstrar na prática:

* Aplicação de Machine Learning em problemas industriais
* Integração entre IA e sistemas interpretáveis
* Simulação de dados em tempo real
* Construção de dashboards interativos

---

## 🚀 Possíveis Melhorias

* Integração com dados reais (IoT / sensores)
* Deploy em nuvem (Streamlit Cloud, AWS, etc.)
* Uso de modelos mais avançados (XGBoost, LSTM)
* Persistência de dados (MySQL/PostgreSQL)
* Sistema de alertas (email, webhook)

---

## 🤝 Contribuição

Sinta-se à vontade para abrir issues ou enviar pull requests!

---

## 📄 Licença

Este projeto está sob a licença MIT.

