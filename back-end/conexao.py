import psycopg2
import os
from dotenv import load_dotenv

#Carrega as variaveis do .env
load_dotenv()

#Conexão com o banco
def conectar_banco():
    try:
        conexao = psycopg2.connect(
            host=os.getenv("DB_HOST"),
            database=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            port=os.getenv("DB_PORT")
        )
        print("Conexão estabelecida com sucesso!")
        return conexao
    except Exception as erro:
        print(f"A conexão falhou: {erro}")
        return None

#Função de criar a tabela 
def criar_tabela():
    conexao = conectar_banco()
    if conexao:
        try:
            cursor = conexao.cursor()
            cursor.execute("""CREATE TABLE IF NOT EXISTS produtos(
                                id SERIAL PRIMARY KEY,
                                nome TEXT NOT NULL,
                                preco REAL NOT NULL,
                                quantidade INTEGER
                           )""")
            conexao.commit()
            print("Tabela criada com sucesso!")
            cursor.close()
        except Exception as erro:
            print(f"Erro ao criar a tabela:{erro}")
        finally:
            conexao.close()
            print("Conexão fechada")
    else:
        print("Não foi possivel criar a tabela porque a conexão falhou.")

if __name__ == "__main__":
    criar_tabela()