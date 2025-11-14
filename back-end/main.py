from fastapi import FastAPI
from funcoes import cadastrar_produto, listar_todos, atualizar_preco, deletar, valor_total

app = FastAPI()

@app.post("/produtos")
def rota_adicionar(nome: str, categoria: str, preco: float, quantidade:int):
    return cadastrar_produto(nome, categoria, preco, quantidade)

@app.get("/produtos")
def rota_listar():
    return listar_todos()

@app.put("/produtos/{id_produto}/preco")
def rota_atualizar_preco(id_produto:int, preco:float):
    return atualizar_preco(id_produto, preco)

@app.delete("/produtos/{id_produto}")
def rota_deletar(id_produto:int):
    return deletar(id_produto)

@app.get("/estoque/total")
def rota_valor_total():
    total = valor_total()
    return {"total": total}