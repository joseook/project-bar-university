from app.queries.categoria_queries import (
    buscar_categoria_por_id,
    criar_categoria,
    listar_categorias,
)
from app.queries.mesa_queries import (
    listar_mesas,
    criar_mesa,
)
from app.queries.produto_queries import (
    buscar_produto_por_id,
    criar_produto,
    listar_produtos,
)


def exibir_menu():
    print("\n=== SISTEMA DO BAR ===")
    print("1. Listar categorias")
    print("2. Cadastrar categoria")
    print("3. Buscar categoria por ID")
    print("4. Listar produtos")
    print("5. Cadastrar produto")
    print("6. Buscar produto por ID")
    print("7. Listar mesas")
    print("8. Cadastrar mesa")
    print("0. Sair")


def ler_inteiro(mensagem):
    return int(input(mensagem).strip())


def ler_decimal(mensagem):
    return float(input(mensagem).strip().replace(",", "."))


def mostrar_categorias():
    categorias = listar_categorias()
    if not categorias:
        print("Nenhuma categoria cadastrada.")
        return

    for categoria in categorias:
        print(f"{categoria['id_categoria']} - {categoria['descricao']}")


def cadastrar_categoria():
    descricao = input("Descricao da categoria: ").strip()
    categoria = criar_categoria(descricao)
    print(f"Categoria criada com ID {categoria['id_categoria']}.")


def consultar_categoria():
    id_categoria = ler_inteiro("ID da categoria: ")
    categoria = buscar_categoria_por_id(id_categoria)
    if not categoria:
        print("Categoria nao encontrada.")
        return
    print(categoria)


def mostrar_produtos():
    produtos = listar_produtos()
    if not produtos:
        print("Nenhum produto cadastrado.")
        return

    for produto in produtos:
        categoria = produto["categoria_descricao"] or "Sem categoria"
        print(
            f"{produto['id_produto']} - {produto['nome']} - "
            f"R$ {produto['preco_unitario']:.2f} - {categoria}"
        )


def cadastrar_produto():
    nome = input("Nome do produto: ").strip()
    preco_unitario = ler_decimal("Preco unitario: ")
    categoria_digitada = input("ID da categoria (enter para vazio): ").strip()
    fk_categoria = int(categoria_digitada) if categoria_digitada else None
    produto = criar_produto(nome, preco_unitario, fk_categoria)
    print(f"Produto criado com ID {produto['id_produto']}.")


def consultar_produto():
    id_produto = ler_inteiro("ID do produto: ")
    produto = buscar_produto_por_id(id_produto)
    if not produto:
        print("Produto nao encontrado.")
        return
    print(produto)


def mostrar_mesas():
    mesas = listar_mesas()
    if not mesas:
        print("Nenhuma mesa encontrada.")
        return
    for mesa in mesas:
        print(mesa)

def registrar_mesa():
    numero = ler_inteiro("Numero da mesa: ")
    status = input("Status da mesa: ").strip()
    mesa = criar_mesa(numero, status)
    print(f"Mesa criada com ID {mesa['id_mesa']}.")
    print(f"Numero: {mesa['numero']}, Status: {mesa['status']}")


def main():
    acoes = {
        "1": mostrar_categorias,
        "2": cadastrar_categoria,
        "3": consultar_categoria,
        "4": mostrar_produtos,
        "5": cadastrar_produto,
        "6": consultar_produto,
        "7": mostrar_mesas,
        "8": registrar_mesa,
    }

    while True:
        exibir_menu()
        opcao = input("Escolha uma opcao: ").strip()

        if opcao == "0":
            print("Encerrando sistema.")
            break

        acao = acoes.get(opcao)
        if not acao:
            print("Opcao invalida.")
            continue

        try:
            acao()
        except ValueError:
            print("Valor informado invalido.")
        except Exception as erro:
            print(f"Erro ao executar operacao: {erro}")


if __name__ == "__main__":
    main()
