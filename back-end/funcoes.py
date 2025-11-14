from conexao import conectar_banco

#Função de adicionar produtos
def cadastrar_produto(nome, categoria, preco, quantidade):
    conexao = conectar_banco()
    if conexao:
        try:
            cursor = conexao.cursor()
            cursor.execute("""
                INSERT INTO produtos(nome, categoria, preco, quantidade) VALUES (%s, %s, %s, %s)
                           """, (nome, categoria, preco, quantidade))
            conexao.commit()
            print(f"Produto '{nome}' cadastrado com sucesso!")
            cursor.close()
        except Exception as erro:
            print(f"Erro ao cadastrar o produto {erro}")
        finally:
            conexao.close()

#cadastrar_produto("Bomba Nuclear", "Destruição em massa", 1996.50, 1)

#Função de listar tudo
def listar_todos():
    conexao = conectar_banco()
    if conexao:
        try:
            cursor = conexao.cursor()
            cursor.execute(
                """SELECT * FROM produtos"""
            )
            resultado = cursor.fetchall()
            return resultado
        except Exception as erro:
            print(f"Erro ao listar {erro}")
        finally:
            conexao.close()

#dados = listar_todos()
#print(dados)

#Função de atualizar o preço
def atualizar_preco(id_produto, novo_preco):
    conexao = conectar_banco()
    if conexao:
        try:
            cursor = conexao.cursor()
            cursor.execute(
                "UPDATE produtos SET preco = %s WHERE id = %s",
                (novo_preco, id_produto)
            )
            conexao.commit()
            return "Preço atualizado com sucesso!"
        except Exception as erro:
            return f"Erro ao tentar atualizar: {erro}"
        finally:
            conexao.close()


#atualizar_preco(1, 1973.50)