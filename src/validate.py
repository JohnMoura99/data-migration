from dotenv import load_dotenv
import os
import psycopg
import pandas as pd
import sys

load_dotenv()

usuario = os.getenv("POSTGRES_USER")
senha = os.getenv("POSTGRES_PASSWORD")
nome_banco = os.getenv("POSTGRES_DB")

resultados = []

def checar(nome, obtido, esperado, tolerancia=0):
    passou = abs(obtido - esperado) <= tolerancia
    status = "OK" if passou else "FALHA"
    print(f"[{status}] {nome}: obtido={obtido} | esperado={esperado}")
    resultados.append(passou)


def consultar(cursor, sql):
    cursor.execute(sql)
    return cursor.fetchone()[0]

df = pd.read_parquet("data/pedidos_zstd.parquet", columns=["id_pedido", "cidade", "valor_total"])
df = df.drop_duplicates(subset="id_pedido")
linhas_esperadas = len(df)
soma_esperada = df["valor_total"].sum()
nulos_cidade_esperados = df["cidade"].isna().sum()

with psycopg.connect(
    dbname=nome_banco, 
    user=usuario, 
    password=senha, 
    host="127.0.0.1", 
    port=5432) as conexao:
    with conexao.cursor() as cursor:
        checar("Total de linhas", consultar(cursor, "SELECT COUNT(*) FROM pedidos"), linhas_esperadas)
        checar("Pedidos duplicados", consultar(cursor, "SELECT COUNT(*) - COUNT(DISTINCT id_pedido) FROM pedidos"), 0)#duplicados
        checar("Soma de valor_total", float(consultar(cursor, "SELECT SUM(valor_total) FROM pedidos")), soma_esperada ,tolerancia=0.01)#soma de valor_total
        checar("Nulos em cidade", consultar(cursor, "SELECT COUNT(*) FROM pedidos WHERE cidade IS NULL"), nulos_cidade_esperados)#qtt de nulos em cidades
        checar("Nulos em colunas obrigatórias", consultar(cursor, "SELECT COUNT(*) FROM pedidos WHERE id_pedido IS NULL OR id_cliente IS NULL OR valor_total IS NULL"), 0)#nulos obrigatorios
        checar("Linhas com valor_total incorreto", consultar(cursor, "SELECT COUNT(*) FROM pedidos WHERE ABS(valor_total - quantidade * valor_unitario) > 0.01"), 0)#regra de negocio
        checar("Linhas com status inválido", consultar(cursor, "SELECT COUNT(*) FROM pedidos WHERE status NOT IN ('ENTREGUE','CANCELADO','EM TRANSPORTE','DEVOLVIDO')"),0)#status inválido
        checar("Linhas com quantidade inválida", consultar(cursor, "SELECT COUNT(*) FROM pedidos WHERE quantidade NOT BETWEEN 1 AND 3"), 0)


print(f"{sum(resultados)} de {len(resultados)} checagens passaram")
if not all(resultados):
    sys.exit(1)