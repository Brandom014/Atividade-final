from conexao import conectar_banco

#Função de adicionar produtos
def cadastrar_produto(nome, preco, quantidade):
    conexao = conectar_banco()
    if conexao:
        try:
            cursor = conexao.cursor()
            cursor.execute("""
                INSERT INTO produtos(nome, preco, quantidade) VALUES (%s, %s, %s)
                           """, (nome, preco, quantidade))
            conexao.commit()
            print(f"Produto '{nome}' cadastrado com sucesso!")
            cursor.close()
        except Exception as erro:
            print(f"Erro ao cadastrar o produto {erro}")
        finally:
            conexao.close()

