# MER — Modelo Entidade-Relacionamento

## Entidades e Atributos

### CATEGORIA
| Atributo     | Tipo          | Restrição       |
|--------------|---------------|-----------------|
| ID_CATEGORIA | Inteiro       | PK, auto-gerado |
| DESCRICAO    | Texto (100)   | NOT NULL        |

### PRODUTO
| Atributo       | Tipo           | Restrição             |
|----------------|----------------|-----------------------|
| ID_PRODUTO     | Inteiro        | PK, auto-gerado       |
| NOME           | Texto (255)    | NOT NULL              |
| PRECO_UNITARIO | Numérico(10,2) | NOT NULL              |
| FK_CATEGORIA   | Inteiro        | FK → CATEGORIA, nulo  |

### MESA
| Atributo | Tipo        | Restrição                       |
|----------|-------------|---------------------------------|
| ID_MESA  | Inteiro     | PK, auto-gerado                 |
| NUMERO   | Inteiro     | UNIQUE, NOT NULL                |
| STATUS   | Texto (20)  | DEFAULT 'Disponivel'            |

### PEDIDO
| Atributo    | Tipo           | Restrição                |
|-------------|----------------|--------------------------|
| ID_PEDIDO   | Inteiro        | PK, auto-gerado          |
| DATA_HORA   | Timestamp      | DEFAULT CURRENT_TIMESTAMP|
| FK_MESA     | Inteiro        | FK → MESA, nulo          |
| VALOR_TOTAL | Numérico(10,2) | —                        |

### USUARIO
| Atributo   | Tipo        | Restrição        |
|------------|-------------|------------------|
| ID_USUARIO | Inteiro     | PK, auto-gerado  |
| NOME       | Texto (100) | NOT NULL         |
| LOGIN      | Texto (50)  | UNIQUE, NOT NULL |
| SENHA_HASH | Texto       | NOT NULL         |

### ITENS_PEDIDO
| Atributo   | Tipo    | Restrição              |
|------------|---------|------------------------|
| FK_PEDIDO  | Inteiro | PK + FK → PEDIDO       |
| FK_PRODUTO | Inteiro | PK + FK → PRODUTO      |
| QUANTIDADE | Inteiro | NOT NULL               |

> Chave primária composta: (FK_PEDIDO, FK_PRODUTO)

---

## Relacionamentos

| Relacionamento      | Cardinalidade | Entidades envolvidas         |
|---------------------|---------------|------------------------------|
| classifica          | (0,N) : (0,1) | CATEGORIA — PRODUTO          |
| possui              | (0,N) : (1,1) | MESA — PEDIDO                |
| contém              | (1,N) : (1,1) | PEDIDO — ITENS_PEDIDO        |
| compõe              | (0,N) : (1,1) | PRODUTO — ITENS_PEDIDO       |

### Descrição dos relacionamentos

**CATEGORIA classifica PRODUTO**
- Uma categoria pode classificar nenhum ou vários produtos.
- Um produto pode pertencer a no máximo uma categoria (opcional).

**MESA possui PEDIDO**
- Uma mesa pode ter nenhum ou vários pedidos ao longo do tempo.
- Um pedido pertence a exatamente uma mesa.

**PEDIDO contém ITENS_PEDIDO**
- Um pedido deve ter pelo menos um item.
- Cada item pertence a exatamente um pedido.

**PRODUTO compõe ITENS_PEDIDO**
- Um produto pode compor nenhum ou vários itens de pedido.
- Cada item de pedido referencia exatamente um produto.
