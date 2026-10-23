# 
# Dois cuidados do COPY (para lembrar na hora de escrever)
# NaN precisa virar None, senão o Postgres recusa a cidade vazia.
# Esvazie a staging antes (TRUNCATE), para uma segunda execução não acumular linhas.
from dotenv import load_dotenv
import os
import psycopg
import pandas as pd

load_dotenv()

usuario = os.getenv("POSTGRES_USER")
senha = os.getenv("POSTGRES_PASSWORD")
nome_banco = os.getenv("POSTGRES_DB")

# formato sem with
# conexao = psycopg.connect(
#     dbname=nome_banco,
#     user=usuario,
#     password=senha,
#     host="127.0.0.1",
#     port= 5432,
# )
# cursor = conexao.cursor()
# cursor.execute("SELECT 1")
# print(cursor.fetchone())   # deve imprimir (1,)

with psycopg.connect(
    dbname=nome_banco, 
    user=usuario, 
    password=senha, 
    host="127.0.0.1", 
    port=5432) as conexao:
    with conexao.cursor() as cursor:
        cursor.execute("TRUNCATE pedidos_staging")
        df = pd.read_parquet("data/pedidos_zstd.parquet")
        df = df.astype(object).where(df.notna(), None) # transformando Nan para None
        with cursor.copy("COPY pedidos_staging FROM STDIN") as copy:
            for linha in df.itertuples(index=False, name=None):
                copy.write_row(linha)
        cursor.execute("SELECT COUNT(*) FROM pedidos_staging")
        linhas_staging = cursor.fetchone()[0] 
        cursor.execute("INSERT INTO pedidos SELECT * FROM pedidos_staging  ON CONFLICT (id_pedido) DO NOTHING")
        linhas_inseridas = cursor.rowcount
        descartadas = linhas_staging - linhas_inseridas
        print(f"Staging: {linhas_staging} | Inseridas: {linhas_inseridas} | Descartadas: {descartadas}")

                        
                       

        