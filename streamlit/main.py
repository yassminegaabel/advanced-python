import streamlit as st
import requests

st.title(" Gestion d'articles")

#afficher les articles
st.header("Liste des articles")
response = requests.get("http://localhost:8000/items")
if response.status_code == 200:
    items = response.json()
    if items:
        for item in items:
            st.write(f"**{item['name']}** — {item['price']}€ — En stock : {item['in_stock']}")
    else:
        st.info("Aucun article pour l'instant.")

# ajouter un article
st.header("Ajouter un article")
with st.form("add_item"):
    name = st.text_input("Nom de l'article")
    price = st.number_input("Prix", min_value=0.0)
    in_stock = st.checkbox("En stock", value=True)
    submitted = st.form_submit_button("Ajouter")

    if submitted:
        new_item = {"name": name, "price": price, "in_stock": in_stock}
        r = requests.post("http://localhost:8000/items", json=new_item)
        if r.status_code == 200:
            st.success(f"Article '{name}' ajouté !")
            st.rerun()
        else:
            st.error("Erreur lors de l'ajout.")