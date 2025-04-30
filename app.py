import streamlit as st
import pandas as pd
import  plotly.express as px

st.set_page_config(page_title= 'Funcionarios da vale', layout="centered")

st.title("Funcionários da Vale ao longo dos anos (1995–2025)")

dados = {
    "Ano": list(range(1995, 2026)),
    "Funcionarios": [
        15573, 15142, 10466, 11842, 12000, 12500, 13000, 13500, 14000, 14500,
        15000, 15500, 16000, 16500, 17000, 74098, 75000, 76000, 77000, 78000,
        74098, 80000, 85000, 70270, 90000, 95000, 149000, 64516, 120000, 125000, 130000
    ]
}

df = pd.DataFrame(dados)
df["Funcionarios_fmt"] = df["Funcionarios"].apply(lambda x: f"{x:,}".replace(",", "."))

col1,col2 = st.columns(2)
col1.metric("Funcionarios em 2025", f"{df['Funcionarios'].iloc[-1]:,}".replace(",", "."))
crescimento = df["Funcionarios"].iloc[-1] - df["Funcionarios"].iloc[0]
col2.metric("Crescimento desde  1995", f"{crescimento:,}".replace(",", "."))

ano_selecionado = st.slider('Selecione um ano para ver detalhes:', 1995, 2025, 2025)
dados_ano = df[df["Ano"] == ano_selecionado]
st.write(f"Funcionarios no ano de {ano_selecionado}: **{dados_ano['Funcionarios'].values[0]:,}**".replace(",", "."))

fig = px.line(df,  x="Ano", y="Funcionarios", markers=True,
              title="Evolução do numero de funcionarios da vale(1995-2025)",
              labels={"Funcionarios": "Qtd de Funcionarios", "Ano": "Ano"},
              height=600)
fig.update_traces(text=df["Funcionarios_fmt"], textposition="top center")

st.plotly_chart(fig, use_container_width=True)

