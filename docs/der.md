# DER — Diagrama Entidade-Relacionamento

```mermaid
erDiagram
    CATEGORIA {
        serial  ID_CATEGORIA PK
        varchar DESCRICAO
    }

    PRODUTO {
        serial  ID_PRODUTO     PK
        varchar NOME
        numeric PRECO_UNITARIO
        int     FK_CATEGORIA   FK
    }

    MESA {
        serial  ID_MESA  PK
        int     NUMERO
        varchar STATUS
    }

    PEDIDO {
        serial    ID_PEDIDO   PK
        timestamp DATA_HORA
        int       FK_MESA     FK
        numeric   VALOR_TOTAL
    }

    USUARIO {
        serial  ID_USUARIO PK
        varchar NOME
        varchar LOGIN
        text    SENHA_HASH
    }

    ITENS_PEDIDO {
        int FK_PEDIDO  FK
        int FK_PRODUTO FK
        int QUANTIDADE
    }

    CATEGORIA ||--o{ PRODUTO      : "classifica"
    MESA      ||--o{ PEDIDO       : "possui"
    PEDIDO    ||--|{ ITENS_PEDIDO : "contém"
    PRODUTO   ||--o{ ITENS_PEDIDO : "compõe"
```

## Legenda

| Símbolo  | Significado              |
|----------|--------------------------|
| `||`     | exatamente um            |
| `o{`     | zero ou muitos           |
| `|{`     | um ou muitos             |
| `PK`     | chave primária           |
| `FK`     | chave estrangeira        |

## Observações

- **USUARIO** não possui relacionamento com as demais entidades no modelo atual; é utilizado exclusivamente para autenticação dos operadores do sistema.
- **ITENS_PEDIDO** é uma entidade associativa (tabela de junção) que resolve o relacionamento N:N entre PEDIDO e PRODUTO, adicionando o atributo QUANTIDADE.
- A chave primária de **ITENS_PEDIDO** é composta por (FK_PEDIDO, FK_PRODUTO).
