
/*tem que manter a mesma ordem das coluna do parquet*/
CREATE TABLE IF NOT EXISTS pedidos_staging (
    id_pedido        INTEGER,
    data_pedido      TIMESTAMP,
    id_cliente       INTEGER,
    nome_cliente     TEXT,
    cidade           TEXT,
    estado           CHAR(2),
    produto          TEXT,
    categoria        TEXT,
    quantidade       SMALLINT,
    valor_unitario   NUMERIC(10,2),
    valor_total      NUMERIC(10,2),
    forma_pagamento  TEXT,
    status           TEXT
);

CREATE TABLE IF NOT EXISTS pedidos (
    id_pedido        INTEGER PRIMARY KEY,
    data_pedido      TIMESTAMP,
    id_cliente       INTEGER,
    nome_cliente     TEXT,
    cidade           TEXT,
    estado           CHAR(2),
    produto          TEXT,
    categoria        TEXT,
    quantidade       SMALLINT,
    valor_unitario   NUMERIC(10,2),
    valor_total      NUMERIC(10,2),
    forma_pagamento  TEXT,
    status           TEXT
);