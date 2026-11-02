
import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="SALAMA AI",
    page_icon="🛡️",
    layout="wide"
)

st.markdown("""
<style>
.block-container {
    padding-top: 2rem;
}
h1, h2, h3 {
    color: #17365D;
}
[data-testid="stMetric"] {
    background: #F0F5FB;
    padding: 16px;
    border-radius: 12px;
}
</style>
""", unsafe_allow_html=True)

st.title("🛡️ SALAMA AI")
st.subheader("Protection et bien-être psychosocial")
st.info(
    "Prototype de démonstration — "
    "données entièrement fictives."
)

st.sidebar.title("SALAMA AI")
page = st.sidebar.radio(
    "Navigation",
    [
        "Tableau de bord",
        "Simulation des besoins",
        "À propos"
    ]
)

donnees = [
    {"ville": "Kinshasa", "besoin": "Soutien psychosocial"},
    {"ville": "Kinshasa", "besoin": "Protection"},
    {"ville": "Bukavu", "besoin": "Protection"},
    {"ville": "Kolwezi", "besoin": "Soutien psychosocial"},
    {"ville": "Bandundu", "besoin": "Assistance juridique"}
]

df = pd.DataFrame(donnees)

if "simulations" not in st.session_state:
    st.session_state.simulations = []

if page == "Tableau de bord":
    st.header("Vue générale")

    villes = st.multiselect(
        "Filtrer par ville",
        sorted(df["ville"].unique()),
        default=sorted(df["ville"].unique())
    )

    filtre = df[df["ville"].isin(villes)]

    col1, col2, col3 = st.columns(3)

    col1.metric("Situations fictives", len(filtre))
    col2.metric("Villes sélectionnées", filtre["ville"].nunique())
    col3.metric("Catégories de besoins", filtre["besoin"].nunique())

    col4, col5 = st.columns(2)

    with col4:
        st.subheader("Répartition par ville")
        st.bar_chart(filtre["ville"].value_counts())

    with col5:
        st.subheader("Répartition par besoin")
        st.bar_chart(filtre["besoin"].value_counts())

    st.subheader("Données de démonstration")
    st.dataframe(filtre, use_container_width=True)

elif page == "Simulation des besoins":
    st.header("Simulation d'une demande")
    st.warning(
        "N'introduisez aucune donnée personnelle "
        "ou situation réelle dans ce prototype."
    )

    with st.form("simulation"):
        ville = st.selectbox(
            "Ville",
            ["Kinshasa", "Kolwezi", "Bukavu", "Bandundu"]
        )

        besoin = st.selectbox(
            "Type de besoin",
            [
                "Soutien psychosocial",
                "Protection",
                "Assistance juridique"
            ]
        )

        envoyer = st.form_submit_button("Simuler")

    if envoyer:
        orientation = {
            "Soutien psychosocial":
                "Orientation indicative vers un professionnel "
                "qualifié en soutien psychosocial.",
            "Protection":
                "Orientation indicative vers un service "
                "local de protection.",
            "Assistance juridique":
                "Orientation indicative vers un service "
                "d'assistance juridique."
        }

        st.session_state.simulations.append({
            "ville": ville,
            "besoin": besoin
        })

        st.success("Simulation enregistrée temporairement.")
        st.write(orientation[besoin])

    st.subheader("Historique de la session")
    st.dataframe(
        pd.DataFrame(
            st.session_state.simulations,
            columns=["ville", "besoin"]
        ),
        use_container_width=True
    )
    st.caption(
        "Ces simulations ne sont pas enregistrées "
        "dans une base de données permanente."
    )

else:
    st.header("À propos du projet")

    st.write("""
    SALAMA AI est un projet de plateforme numérique
    visant à améliorer l'accès à l'information,
    au soutien psychosocial et aux services de
    protection des femmes et des filles en RDC.
    """)

    st.subheader("Zones d'intervention envisagées")
    st.write("Kinshasa, Kolwezi, Bukavu et Bandundu.")

    st.subheader("État du développement")
    st.write("""
    Prototype expérimental utilisant Streamlit
    et Pandas. Les fonctionnalités avancées
    d'intelligence artificielle, la gestion
    sécurisée des dossiers et l'orientation
    réelle des bénéficiaires restent à développer
    et à valider.
    """)

st.divider()
st.caption(
    "SALAMA AI — Prototype expérimental | "
    "Aucune donnée réelle de bénéficiaire"
)
