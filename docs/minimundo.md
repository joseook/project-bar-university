# Minimundo — Sistema de Gerenciamento de Bar

## Contexto

Um bar precisa controlar seu cardápio, suas mesas, os pedidos realizados e os usuários que operam o sistema. O objetivo é ter uma aplicação que permita cadastrar e consultar categorias de produtos, produtos, mesas, pedidos e os itens que compõem cada pedido, além de autenticar os operadores do estabelecimento.

## Regras de Negócio

### Categorias
- Cada produto pertence a uma categoria (ex.: Bebidas, Petiscos, Sobremesas).
- Uma categoria pode agrupar zero ou mais produtos.
- Uma categoria possui apenas uma descrição textual.

### Produtos
- Todo produto tem um nome, um preço unitário e pode estar associado a uma categoria.
- A associação com a categoria é opcional; um produto pode existir sem categoria definida.
- Um produto pode aparecer em nenhum ou vários pedidos.

### Mesas
- O bar possui um conjunto de mesas identificadas por número único.
- Cada mesa possui um status que indica se está disponível ou ocupada.
- Uma mesa pode ter nenhum ou vários pedidos ao longo do tempo.

### Pedidos
- Um pedido é sempre vinculado a uma mesa.
- O pedido registra a data e hora em que foi realizado e o valor total cobrado.
- Um pedido é composto por um ou mais itens.

### Itens do Pedido
- Cada item do pedido referencia um produto e registra a quantidade solicitada.
- A combinação pedido + produto é única (chave composta); para solicitar mais unidades do mesmo produto no mesmo pedido, basta atualizar a quantidade.

### Usuários
- O sistema possui usuários cadastrados que operam o sistema via CLI ou API.
- Cada usuário tem nome, login único e senha armazenada como hash bcrypt.
- Não há hierarquia de perfis nesta versão; qualquer usuário autenticado tem acesso completo.

## Entidades Principais

| Entidade      | Descrição                                              |
|---------------|--------------------------------------------------------|
| CATEGORIA     | Agrupa produtos por tipo (ex.: Bebidas, Petiscos)      |
| PRODUTO       | Item do cardápio com nome e preço                      |
| MESA          | Mesa física do bar com número e status                 |
| PEDIDO        | Registro de consumo vinculado a uma mesa               |
| ITENS_PEDIDO  | Associação entre pedido e produto com quantidade       |
| USUARIO       | Operador do sistema com credenciais de acesso          |

## Relacionamentos

- Uma **CATEGORIA** classifica zero ou mais **PRODUTOS**.
- Um **PRODUTO** pertence a no máximo uma **CATEGORIA**.
- Uma **MESA** possui zero ou mais **PEDIDOS**.
- Um **PEDIDO** pertence a uma **MESA**.
- Um **PEDIDO** contém um ou mais **ITENS_PEDIDO**.
- Um **PRODUTO** pode compor zero ou mais **ITENS_PEDIDO**.
