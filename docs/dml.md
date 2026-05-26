# DML — Data Manipulation Language

Exemplos de operações de consulta, inserção, atualização e remoção utilizadas pela aplicação.

---

## SELECT (consultas)

### Listar todas as categorias
```sql
SELECT id_categoria, descricao
FROM categoria
ORDER BY id_categoria;
```

### Buscar categoria por ID
```sql
SELECT id_categoria, descricao
FROM categoria
WHERE id_categoria = 1;
```

### Listar todos os produtos (com nome da categoria via JOIN)
```sql
SELECT
    p.id_produto,
    p.nome,
    p.preco_unitario::float AS preco_unitario,
    p.fk_categoria,
    c.descricao AS categoria_descricao
FROM produto p
LEFT JOIN categoria c ON c.id_categoria = p.fk_categoria
ORDER BY p.id_produto;
```

### Buscar produto por ID (com categoria)
```sql
SELECT
    p.id_produto,
    p.nome,
    p.preco_unitario::float AS preco_unitario,
    p.fk_categoria,
    c.descricao AS categoria_descricao
FROM produto p
LEFT JOIN categoria c ON c.id_categoria = p.fk_categoria
WHERE p.id_produto = 1;
```

### Listar todas as mesas
```sql
SELECT id_mesa, numero, status
FROM mesa
ORDER BY id_mesa;
```

### Listar todos os pedidos
```sql
SELECT
    id_pedido,
    data_hora,
    fk_mesa,
    valor_total::float AS valor_total
FROM pedido
ORDER BY id_pedido;
```

### Buscar usuário por login
```sql
SELECT id_usuario, nome, login, senha_hash
FROM usuario
WHERE login = 'operador1';
```

---

## INSERT (inserções)

### Criar categoria
```sql
INSERT INTO categoria (descricao)
VALUES ('Bebidas')
RETURNING id_categoria, descricao;
```

### Criar produto
```sql
INSERT INTO produto (nome, preco_unitario, fk_categoria)
VALUES ('Cerveja Heineken', 9.50, 1)
RETURNING id_produto;
```

### Criar mesa
```sql
INSERT INTO mesa (numero, status)
VALUES (1, 'Disponivel')
RETURNING id_mesa, numero, status;
```

### Criar pedido
```sql
INSERT INTO pedido (fk_mesa, valor_total)
VALUES (1, 0.00)
RETURNING id_pedido, data_hora, fk_mesa, valor_total::float AS valor_total;
```

### Criar usuário (senha como hash bcrypt)
```sql
INSERT INTO usuario (nome, login, senha_hash)
VALUES ('João Silva', 'joao', '$2b$12$...')
RETURNING id_usuario, nome, login;
```

### Adicionar item ao pedido
```sql
INSERT INTO itens_pedido (fk_pedido, fk_produto, quantidade)
VALUES (1, 2, 3);
```

---

## UPDATE (atualizações)

### Atualizar categoria
```sql
UPDATE categoria
SET descricao = 'Cervejas Artesanais'
WHERE id_categoria = 1
RETURNING id_categoria, descricao;
```

### Atualizar produto
```sql
UPDATE produto
SET nome           = 'Cerveja Artesanal IPA',
    preco_unitario = 14.90,
    fk_categoria   = 1
WHERE id_produto = 1
RETURNING id_produto;
```

### Atualizar status da mesa
```sql
UPDATE mesa
SET numero = 1,
    status = 'Ocupada'
WHERE id_mesa = 1
RETURNING id_mesa, numero, status;
```

### Atualizar pedido
```sql
UPDATE pedido
SET fk_mesa     = 2,
    valor_total = 28.40
WHERE id_pedido = 1
RETURNING id_pedido, data_hora, fk_mesa, valor_total::float AS valor_total;
```

---

## DELETE (remoções)

### Deletar categoria
```sql
DELETE FROM categoria
WHERE id_categoria = 1
RETURNING id_categoria;
```

### Deletar produto
```sql
DELETE FROM produto
WHERE id_produto = 1
RETURNING id_produto;
```

### Deletar mesa
```sql
DELETE FROM mesa
WHERE id_mesa = 1
RETURNING id_mesa;
```

### Deletar pedido
```sql
DELETE FROM pedido
WHERE id_pedido = 1
RETURNING id_pedido;
```

---

## JOINs

### Produtos com suas categorias (LEFT JOIN)
Retorna todos os produtos, incluindo os sem categoria.

```sql
SELECT
    p.id_produto,
    p.nome,
    p.preco_unitario,
    c.descricao AS categoria
FROM produto p
LEFT JOIN categoria c ON c.id_categoria = p.fk_categoria;
```

### Pedidos com o número da mesa (INNER JOIN)
Retorna apenas pedidos que possuem mesa vinculada.

```sql
SELECT
    pe.id_pedido,
    pe.data_hora,
    pe.valor_total,
    m.numero AS numero_mesa,
    m.status AS status_mesa
FROM pedido pe
INNER JOIN mesa m ON m.id_mesa = pe.fk_mesa;
```

### Itens de um pedido com detalhes do produto (INNER JOIN)
```sql
SELECT
    ip.fk_pedido,
    ip.quantidade,
    p.nome           AS produto,
    p.preco_unitario,
    (ip.quantidade * p.preco_unitario) AS subtotal
FROM itens_pedido ip
INNER JOIN produto p ON p.id_produto = ip.fk_produto
WHERE ip.fk_pedido = 1;
```

### Pedido completo: mesa + itens + produtos + categorias
```sql
SELECT
    pe.id_pedido,
    pe.data_hora,
    pe.valor_total,
    m.numero          AS mesa,
    p.nome            AS produto,
    c.descricao       AS categoria,
    ip.quantidade,
    p.preco_unitario,
    (ip.quantidade * p.preco_unitario) AS subtotal
FROM pedido pe
INNER JOIN mesa        m  ON m.id_mesa      = pe.fk_mesa
INNER JOIN itens_pedido ip ON ip.fk_pedido  = pe.id_pedido
INNER JOIN produto     p  ON p.id_produto   = ip.fk_produto
LEFT  JOIN categoria   c  ON c.id_categoria = p.fk_categoria
WHERE pe.id_pedido = 1;
```
