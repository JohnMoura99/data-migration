import pandas as pd
import time as tm
import os as os

#estrutura do scripts
#imports → caminhos dos arquivos → ler CSV (medindo tempo) → salvar 3 Parquets (medindo #tempo) → comparar tamanhos → comparar leitura de 1 coluna → imprimir tabela

CAMINHO_CSV = "data/pedidos3.csv"

def medir_tempo(funcao,*args, **kwargs):
    inicio = tm.perf_counter()
    resultado = funcao(*args, **kwargs)
    duracao = tm.perf_counter() - inicio
    return resultado, duracao

df, t_leitura = medir_tempo( pd.read_csv,CAMINHO_CSV, parse_dates=["data_pedido"])
print(f"Leitura do CSV: {t_leitura:.2f} s") # aqui tem duas variaveis pq a função retorna dois resultados

# df.to_parquet("data/pedidos_sem_compressao.parquet", compression=None) -antes a linha que trasformava o arquivo em parquet era escrito dessa forma, porem para usar a função para medir o tempo vamo se escrever da maneira que estar agora sem parentese para entregar a função para medir_tempo executar 

_, t_none = medir_tempo(df.to_parquet, "data/pedidos_sem_compressao.parquet", compression=None)
print(f"Escrita None: {t_none:.2f} s")

_, t_snapy = medir_tempo(df.to_parquet, "data/pedidos_snappy.parquet", compression="snappy")
print(f"Escrita snapy: {t_snapy:.2f} s")

_, t_zstd = medir_tempo(df.to_parquet, "data/pedidos_zstd.parquet", compression="zstd")
print(f"Escrita zstd: {t_zstd:.2f} s")
# df.to_parquet("data/pedidos_zstd.parquet", compression="zstd")
# print(df)

tamanho_csv = os.path.getsize(CAMINHO_CSV)
tamanho_none = os.path.getsize("data/pedidos_sem_compressao.parquet")
tamanho_snappy = os.path.getsize("data/pedidos_snappy.parquet")
tamanho_zstd = os.path.getsize("data/pedidos_zstd.parquet")

#medir tempo de leitura dos arquivos
#csv, none, snappy, zstd

_,t_leitura_csv = medir_tempo(pd.read_csv,CAMINHO_CSV ,parse_dates=["data_pedido"]) #resultado do tempo de leitura para comparação
_,t_leitura_none = medir_tempo(pd.read_parquet,"data/pedidos_sem_compressao.parquet")
_,t_leitura_snapy = medir_tempo(pd.read_parquet,"data/pedidos_snappy.parquet")
_,t_leitura_zstd =  medir_tempo(pd.read_parquet,"data/pedidos_zstd.parquet")

#teste da coluna única - leitura da coluna valor total

_ ,leitura_coluna_csv = medir_tempo(pd.read_csv,CAMINHO_CSV , usecols=["valor_total"])
_ ,leitura_coluna_none = medir_tempo(pd.read_parquet,"data/pedidos_sem_compressao.parquet",columns=["valor_total"])
_ ,leitura_coluna_snapy = medir_tempo(pd.read_parquet,"data/pedidos_snappy.parquet",columns=["valor_total"])
_ ,leitura_coluna_zstd =  medir_tempo(pd.read_parquet,"data/pedidos_zstd.parquet",columns=["valor_total"])




tamanho_dic = [
    {"arquivo":"CSV" ,"tamanho_mb":round(tamanho_csv / (1024*1024),2) ,"tempo_escrita_s":None, "tempo_leitura_arquivo_s":round(t_leitura_csv,2),"tempo_col_valor_total_s":round(leitura_coluna_csv,3)},
    {"arquivo":"parquet_none" ,"tamanho_mb": round(tamanho_none / (1024*1024),2) ,"tempo_escrita_s": round(t_none, 2), "tempo_leitura_arquivo_s":round(t_leitura_none,2),"tempo_col_valor_total_s":round(leitura_coluna_none,3)},
    {"arquivo":"parquet_snapy" ,"tamanho_mb": round(tamanho_snappy / (1024*1024),2) ,"tempo_escrita_s": round(t_snapy, 2), "tempo_leitura_arquivo_s":round(t_leitura_snapy,2),"tempo_col_valor_total_s":round(leitura_coluna_snapy,3)},
    {"arquivo":"parquet_zstd" ,"tamanho_mb": round(tamanho_zstd / (1024*1024),2) ,"tempo_escrita_s": round(t_zstd, 2), "tempo_leitura_arquivo_s":round(t_leitura_zstd,2),"tempo_col_valor_total_s":round(leitura_coluna_zstd,3)},
    ]

dtfm = pd.DataFrame(tamanho_dic)

print(dtfm)
dtfm.to_csv('docs/comparacao.csv', index=False)