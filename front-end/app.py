import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"

st.title("Sistema de Estoque")

menu = st.sidebar.radio("Menu",[
    "Adicionar Produto",
    "Listar Produtos",
    "Atualizar Produto",
    "Deletar Produto",
    "Valor Total do Estoque"
])

#Cadastrar
if menu == "Adicionar Produto":
    st.header("Adicionar Produto")
    nome = st.text_input("Nome")
    categoria = st.text_input("Categoria")
    preco = st.number_input("Preço", min_value= 0.0, step= 0.50)
    quantidade = st.number_input("Quantidade", min_value= 0, step=1)
    
    if st.button("Adicionar"):
        response = requests.post(f"{API_URL}/produtos", json={
            "nome": nome,
            "categoria": categoria,
            "preco": preco,
            "quantidade": quantidade
        })

        st.success("Produto cadastrado com sucesso!")

#Listar
elif menu == "Listar Produtos":
    st.header("Lista de Produtos")
    response = requests.get(f"{API_URL}/produtos")

    if response.status_code == 200:
        produtos = response.json()
        st.table(produtos)
    else:
        st.error("Erro ao carregar lista")

#Atualizar preço
# Atualizar preço
elif menu == "Atualizar Produto":
    st.header("Atualizar Preço")
    id_produto = st.number_input("ID do Produto", min_value=1)
    novo_preco = st.number_input("Novo Preço", min_value=0.0, step=0.50)

    if st.button("Atualizar"):
        # Enviando JSON no corpo da requisição
        response = requests.put(
            f"{API_URL}/produtos/{id_produto}/preco",
            json={"preco": novo_preco}
        )

        # Verifica se a atualização deu certo
        if response.status_code == 200:
            st.success("Produto atualizado com sucesso!")
        else:
            st.error(f"Erro ao atualizar produto: {response.text}")

#Deletar
elif menu == "Deletar Produto":
    st.header("Deletar Produto")
    id_produto = st.number_input("ID do Produto para deletar", min_value=1)

    if st.button("Deletar"):
        response = requests.delete(f"{API_URL}/produtos/{id_produto}")
        st.success("Produto deletado com sucesso!")

#Total
elif menu == "Valor Total do Estoque":
    st.header("Valor Total do Estoque")
    response = requests.get(f"{API_URL}/estoque/total")

    if response.status_code == 200:
        total = response.json()["total"]
        st.metric("Total em estoque:", f"R$ {total:.2f}")
    else:
        st.error("Erro ao carregar total")
