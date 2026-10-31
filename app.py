
import streamlit as st
import pandas as pd

from analyse_donnees import analyser_besoins

st.set_page_config(
    page_title="SALAMA AI",
    page_icon="🛡️",
    layout="wide"
)

st.title("🛡️ SALAMA AI")
st.subheader("Protection et bien-être psychosocial")
st.info("Prototype de démonstration — données fictives uniquement")

donnees = [
    {"ville": "Kinshasa", "besoin": "Soutien psychosocial"},
    {"ville": "Kinshasa", "besoin": "Protection"},
    {"ville": "Bukavu", "besoin": "Protection"},
    {"ville": "Kolwezi", "besoin": "Soutien psychosocial"},
    {"ville": "Bandundu", "besoin": "Assistance juridique"}
]

resultats = analyser_besoins(donnees)

st.metric("Situations fictives analysées", resultats["total"])

col1, col2 = st.columns(2)

with col1:
    st.subheader("Répartition par ville")
    villes = pd.Series(resultats["par_ville"])
    st.bar_chart(villes)

with col2:
    st.subheader("Répartition par besoin")
    besoins = pd.Series(resultats["par_besoin"])
    st.bar_chart(besoins)

st.subheader("Données de démonstration")
st.dataframe(pd.DataFrame(donnees), hide_index=True)

st.warning(
    "Aucune donnée réelle de survivantes n'est utilisée. "
    "Ce prototype ne fournit ni diagnostic ni décision automatisée."
)

st.caption("SALAMA AI — Prototype expérimental en RDC")
