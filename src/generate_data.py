from faker import Faker
import pandas as pd
import numpy as np

#passo 2 - definindo o tamanho 
N_PEDIDOS = 2000000
N_CLIENTES = 200000

fake = Faker("pt_BR")

#passo 3 - criando tabela de clientes
cliente = [{"id_cliente": i,"nome": fake.name(),"cidade": fake.city(), "estado":fake.state_abbr()} for i in range(1,N_CLIENTES+1)]

# passo 4 - criando um catalogo de produtos 
produtos = [
    {"produto": "Fone Bluetooth", "categoria": "Eletrônicos", "valor_unitario": 149.90},
    {"produto": "Camiseta Básica", "categoria": "Moda", "valor_unitario": 59.90},
    {"produto": "Panela de Pressão", "categoria": "Casa", "valor_unitario": 129.90},
    {"produto": "Mouse sem Fio", "categoria": "Eletrônicos", "valor_unitario": 79.90},
    {"produto": "Teclado Mecânico", "categoria": "Eletrônicos", "valor_unitario": 249.90},
    {"produto": "Garrafa Térmica", "categoria": "Casa", "valor_unitario": 49.90},
    {"produto": "Tênis Esportivo", "categoria": "Calçados", "valor_unitario": 219.90},
    {"produto": "Mochila Executiva", "categoria": "Acessórios", "valor_unitario": 179.90},
    {"produto": "Relógio Digital", "categoria": "Acessórios", "valor_unitario": 99.90},
    {"produto": "Liquidificador", "categoria": "Eletrodomésticos", "valor_unitario": 159.90},
    {"produto": "Cafeteira Elétrica", "categoria": "Eletrodomésticos", "valor_unitario": 189.90},
    {"produto": "Ventilador de Mesa", "categoria": "Eletrodomésticos", "valor_unitario": 119.90},
    {"produto": "Luminária de Mesa", "categoria": "Casa", "valor_unitario": 69.90},
    {"produto": "Cadeira de Escritório", "categoria": "Móveis", "valor_unitario": 599.90},
    {"produto": "Mesa para Computador", "categoria": "Móveis", "valor_unitario": 449.90},
    {"produto": "Monitor LED 24 Polegadas", "categoria": "Informática", "valor_unitario": 799.90},
    {"produto": "Webcam Full HD", "categoria": "Informática", "valor_unitario": 189.90},
    {"produto": "Impressora Multifuncional", "categoria": "Informática", "valor_unitario": 699.90},
    {"produto": "Carregador USB-C", "categoria": "Acessórios para Celular", "valor_unitario": 49.90},
    {"produto": "Capa para Celular", "categoria": "Acessórios para Celular", "valor_unitario": 29.90},
    {"produto": "Power Bank", "categoria": "Acessórios para Celular", "valor_unitario": 89.90},
    {"produto": "Livro de Python", "categoria": "Livros", "valor_unitario": 89.90},
    {"produto": "Caderno Universitário", "categoria": "Papelaria", "valor_unitario": 24.90},
    {"produto": "Caneta Esferográfica", "categoria": "Papelaria", "valor_unitario": 3.50},
    {"produto": "Mochila Escolar", "categoria": "Papelaria", "valor_unitario": 119.90},
    {"produto": "Perfume Masculino", "categoria": "Beleza", "valor_unitario": 199.90},
    {"produto": "Hidratante Corporal", "categoria": "Beleza", "valor_unitario": 39.90},
    {"produto": "Secador de Cabelo", "categoria": "Beleza", "valor_unitario": 159.90},
    {"produto": "Ferro de Passar", "categoria": "Eletrodomésticos", "valor_unitario": 99.90},
    {"produto": "Jogo de Panelas", "categoria": "Casa", "valor_unitario": 349.90},
    {"produto": "Jogo de Toalhas", "categoria": "Cama, Mesa e Banho", "valor_unitario": 89.90},
    {"produto": "Lençol Casal", "categoria": "Cama, Mesa e Banho", "valor_unitario": 119.90},
    {"produto": "Bola de Futebol", "categoria": "Esportes", "valor_unitario": 79.90},
    {"produto": "Halteres de 5 kg", "categoria": "Esportes", "valor_unitario": 99.90},
    {"produto": "Tapete de Yoga", "categoria": "Esportes", "valor_unitario": 69.90},
    {"produto": "Ração para Cachorro 10 kg", "categoria": "Pet Shop", "valor_unitario": 149.90},
    {"produto": "Cama para Pet", "categoria": "Pet Shop", "valor_unitario": 89.90},
    {"produto": "Coleira para Cachorro", "categoria": "Pet Shop", "valor_unitario": 34.90},
    {"produto": "Brinquedo Educativo", "categoria": "Brinquedos", "valor_unitario": 59.90},
    {"produto": "Jogo de Tabuleiro", "categoria": "Brinquedos", "valor_unitario": 129.90},
    {"produto": "Panela Elétrica de Arroz", "categoria": "Eletrodomésticos", "valor_unitario": 139.90},
    {"produto": "Fritadeira Air Fryer", "categoria": "Eletrodomésticos", "valor_unitario": 399.90},
    {"produto": "Óculos de Sol", "categoria": "Acessórios", "valor_unitario": 119.90},
    {"produto": "Carteira Masculina", "categoria": "Acessórios", "valor_unitario": 69.90},
    {"produto": "Jaqueta Jeans", "categoria": "Moda", "valor_unitario": 199.90},
    {"produto": "Calça Jeans", "categoria": "Moda", "valor_unitario": 139.90},
    {"produto": "Sandália Casual", "categoria": "Calçados", "valor_unitario": 79.90},
    {"produto": "Caixa de Som Bluetooth", "categoria": "Eletrônicos", "valor_unitario": 229.90},
    {"produto": "Smartwatch", "categoria": "Eletrônicos", "valor_unitario": 299.90},
    {"produto": "Micro-ondas 20 Litros", "categoria": "Eletrodomésticos", "valor_unitario": 549.90}
]

df_cliente = pd.DataFrame(cliente)
df_produtos = pd.DataFrame(produtos)

#passo 5 - gerando pedidos com numpy
id_pedido = np.arange(1,N_PEDIDOS +1 )
id_cliente = np.random.randint(1,N_CLIENTES +1,size=N_PEDIDOS)
pos_produto = np.random.randint(0,len(df_produtos), size=N_PEDIDOS)

quantidade = np.random.choice([1,2,3], size=N_PEDIDOS, p=[0.7, 0.2, 0.1])
status = np.random.choice(
    ["ENTREGUE","CANCELADO","EM TRANSPORTE", "DEVOLVIDO"],
    size=N_PEDIDOS,
    p=[0.85, 0.08, 0.05, 0.02],
)
forma_pagamento = np.random.choice(
    ["PIX","CARTÃO","BOLETO"],
    size=N_PEDIDOS,
    p=[0.5, 0.4, 0.1],     
)

inicio = pd.to_datetime("2024-01-01")
segundos = np.random.randint(0, 63_072_000, size=N_PEDIDOS)
data_pedido = inicio + pd.to_timedelta(segundos,unit="s")


df_produtos["pos_produto"] = df_produtos.index #coluna criada para fazer o merg

##criando tabela de pedidos

df_pedidos = pd.DataFrame({
    "id_pedido": id_pedido,
    "id_cliente": id_cliente,
    "data_pedido": data_pedido,
    "pos_produto": pos_produto,
    "quantidade": quantidade,
    "status": status,
    "forma_pagamento": forma_pagamento
})


#passo 6 - juntando tudo

pedidos = pd.merge(df_pedidos,df_cliente, how= 'left',on="id_cliente")
df_final = pd.merge(pedidos,df_produtos, how="left", on="pos_produto")


#passo 7
#valor total
df_final["valor_total"] = (df_final["quantidade"] * df_final  ["valor_unitario"]).round(2)
print(df_final[["quantidade", "valor_unitario", "valor_total"]].head())
#print(df_cliente)
#print(df_produtos)

#cidades vazias
# 1) sorteia 1% das linhas e guarda o "número" (índice) delas
indices = df_final.sample(frac=0.01).index
# 2) nessas linhas, coluna cidade vira vazio
df_final.loc[indices,"cidade"] = np.nan

# sample(frac=0.01) devolve 1% das linhas, escolhidas aleatoriamente.
# .index pega só a “identidade” delas (o número da linha).
# .loc[linhas, coluna] = valor altera a coluna só nessas linhas.
# np.nan é o “vazio” do pandas.

#duplicdos
duplicados = df_final.sample(frac=0.0005)
df_final = pd.concat([df_final, duplicados], ignore_index=True)


df_final = df_final.drop(columns=["pos_produto"])#removendo a coluna auxiliar
df_final = df_final.rename(columns={"nome": "nome_cliente"})#renomeando a coluna nome
df_final = df_final[[
    "id_pedido", "data_pedido", "id_cliente", "nome_cliente", "cidade", "estado",
    "produto", "categoria", "quantidade", "valor_unitario", "valor_total",
    "forma_pagamento", "status",
]] #ordenando as colunas

#passo 8 - salvar csv

df_final.to_csv("data/pedidos3.csv", index=False)