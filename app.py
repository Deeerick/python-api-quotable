import streamlit as st
import requests


def obter_frase():
    url = "https://api.quotable.io/random"
    response = requests.get(url)

    if response.status_code == 200:
        frase = response.json()["content"]
        autor = response.json()["author"]
        return frase, autor
    else:
        print("Erro ao obter a frase.")
        return None, None


def exibir_frase():
    frase_motivacional, autor = obter_frase()
    if frase_motivacional and autor:
        st.header(frase_motivacional)
        st.subheader(f"- {autor}")
    else:
        st.header("Erro ao obter a frase.")


if st.button("Nova Frase"):
    exibir_frase()
else:
    exibir_frase()