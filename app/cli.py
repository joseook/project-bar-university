import getpass
from datetime import datetime

import psycopg2
import psycopg2.errors

from app.queries.usuario_queries import autenticar_usuario, criar_usuario
from app.queries.categoria_queries import (
    atualizar_categoria,
    buscar_categoria_por_id,
    criar_categoria,
    deletar_categoria,
    listar_categorias,
)
from app.queries.mesa_queries import (
    atualizar_mesa,
    buscar_mesa_por_id,
    criar_mesa,
    deletar_mesa,
    listar_mesas,
)
from app.queries.pedidos_queries import (
    atualizar_pedido,
    buscar_pedido_por_id,
    criar_pedido,
    deletar_pedido,
    listar_pedidos,
)
from app.queries.produto_queries import (
    atualizar_produto,
    buscar_produto_por_id,
    criar_produto,
    deletar_produto,
    listar_produtos,
)


def exibir_menu_autenticacao():
    print("\n=== SISTEMA DO BAR ===")
    print("1. Login")
    print("2. Registrar conta")
    print("0. Sair")


def fazer_login():
    login = input("Login: ").strip()
    senha = getpass.getpass("Senha: ")
    usuario = autenticar_usuario(login, senha)
    if not usuario:
        print("Login ou senha invalidos.")
        return None
    print(f"Login realizado com sucesso! Bem-vindo, {usuario['nome']}!")
    return usuario


def registrar_usuario():
    nome = input("Nome: ").strip()
    login = input("Login: ").strip()
    senha = getpass.getpass("Senha: ")
    confirmar = getpass.getpass("Confirmar senha: ")
    if senha != confirmar:
        print("As senhas nao conferem.")
        return None
    try:
        usuario = criar_usuario(nome, login, senha)
        print(f"Conta criada com sucesso! Bem-vindo, {usuario['nome']}!")
        return {"id_usuario": usuario["id_usuario"], "nome": usuario["nome"], "login": usuario["login"]}
    except psycopg2.errors.UniqueViolation:
        print("Esse login ja esta em uso.")
        return None
    except Exception as erro:
        print(f"Erro ao criar conta: {erro}")
        return None


def exibir_menu(nome_usuario):
    print(f"\n=== SISTEMA DO BAR - Bem-vindo, {nome_usuario}! ===")
    print("1. Listar categorias")
    print("2. Cadastrar categoria")
    print("3. Buscar categoria por ID")
    print("4. Atualizar categoria")
    print("5. Deletar categoria")
    print("6. Listar produtos")
    print("7. Cadastrar produto")
    print("8. Buscar produto por ID")
    print("9. Atualizar produto")
    print("10. Deletar produto")
    print("11. Listar mesas")
    print("12. Cadastrar mesa")
    print("13. Buscar mesa por ID")
    print("14. Atualizar mesa")
    print("15. Deletar mesa")
    print("16. Listar pedidos")
    print("17. Cadastrar pedido")
    print("18. Buscar pedido por ID")
    print("19. Atualizar pedido")
    print("20. Deletar pedido")
    print("0. Sair (logout)")


def ler_inteiro(mensagem):
    return int(input(mensagem).strip())


def ler_inteiro_opcional(mensagem):
    valor = input(mensagem).strip()
    return int(valor) if valor else None


def ler_decimal(mensagem):
    return float(input(mensagem).strip().replace(",", "."))


def ler_decimal_opcional(mensagem):
    valor = input(mensagem).strip()
    return float(valor.replace(",", ".")) if valor else None


def ler_data_hora_opcional(mensagem):
    valor = input(mensagem).strip()
    if not valor:
        return None
    return datetime.fromisoformat(valor)


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


def alterar_categoria():
    id_categoria = ler_inteiro("ID da categoria: ")
    descricao = input("Nova descricao: ").strip()
    categoria = atualizar_categoria(id_categoria, descricao)
    if not categoria:
        print("Categoria nao encontrada.")
        return
    print(f"Categoria atualizada: {categoria}")


def remover_categoria():
    id_categoria = ler_inteiro("ID da categoria: ")
    categoria = deletar_categoria(id_categoria)
    if not categoria:
        print("Categoria nao encontrada.")
        return
    print("Categoria removida.")


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
    fk_categoria = ler_inteiro_opcional("ID da categoria (enter para vazio): ")
    produto = criar_produto(nome, preco_unitario, fk_categoria)
    print(f"Produto criado com ID {produto['id_produto']}.")


def consultar_produto():
    id_produto = ler_inteiro("ID do produto: ")
    produto = buscar_produto_por_id(id_produto)
    if not produto:
        print("Produto nao encontrado.")
        return
    print(produto)


def alterar_produto():
    id_produto = ler_inteiro("ID do produto: ")
    nome = input("Novo nome: ").strip()
    preco_unitario = ler_decimal("Novo preco unitario: ")
    fk_categoria = ler_inteiro_opcional("ID da categoria (enter para vazio): ")
    produto = atualizar_produto(id_produto, nome, preco_unitario, fk_categoria)
    if not produto:
        print("Produto nao encontrado.")
        return
    print(f"Produto atualizado: {produto}")


def remover_produto():
    id_produto = ler_inteiro("ID do produto: ")
    produto = deletar_produto(id_produto)
    if not produto:
        print("Produto nao encontrado.")
        return
    print("Produto removido.")


def mostrar_mesas():
    mesas = listar_mesas()
    if not mesas:
        print("Nenhuma mesa encontrada.")
        return
    for mesa in mesas:
        print(mesa)


def registrar_mesa():
    numero = ler_inteiro("Numero da mesa: ")
    status = input("Status da mesa (enter para Disponivel): ").strip() or None
    mesa = criar_mesa(numero, status)
    print(f"Mesa criada com ID {mesa['id_mesa']}.")
    print(f"Numero: {mesa['numero']}, Status: {mesa['status']}")


def consultar_mesa():
    id_mesa = ler_inteiro("ID da mesa: ")
    mesa = buscar_mesa_por_id(id_mesa)
    if not mesa:
        print("Mesa nao encontrada.")
        return
    print(mesa)


def alterar_mesa():
    id_mesa = ler_inteiro("ID da mesa: ")
    numero = ler_inteiro("Novo numero da mesa: ")
    status = input("Novo status da mesa: ").strip() or None
    mesa = atualizar_mesa(id_mesa, numero, status)
    if not mesa:
        print("Mesa nao encontrada.")
        return
    print(f"Mesa atualizada: {mesa}")


def remover_mesa():
    id_mesa = ler_inteiro("ID da mesa: ")
    mesa = deletar_mesa(id_mesa)
    if not mesa:
        print("Mesa nao encontrada.")
        return
    print("Mesa removida.")


def mostrar_pedidos():
    pedidos = listar_pedidos()
    if not pedidos:
        print("Nenhum pedido encontrado.")
        return
    for pedido in pedidos:
        print(pedido)


def registrar_pedido():
    fk_mesa = ler_inteiro_opcional("ID da mesa (enter para vazio): ")
    valor_total = ler_decimal_opcional("Valor total (enter para vazio): ")
    data_hora = ler_data_hora_opcional("Data/hora ISO (enter para agora): ")
    pedido = criar_pedido(fk_mesa, valor_total, data_hora)
    print(f"Pedido criado com ID {pedido['id_pedido']}.")


def consultar_pedido():
    id_pedido = ler_inteiro("ID do pedido: ")
    pedido = buscar_pedido_por_id(id_pedido)
    if not pedido:
        print("Pedido nao encontrado.")
        return
    print(pedido)


def alterar_pedido():
    id_pedido = ler_inteiro("ID do pedido: ")
    fk_mesa = ler_inteiro_opcional("Novo ID da mesa (enter para vazio): ")
    valor_total = ler_decimal_opcional("Novo valor total (enter para vazio): ")
    data_hora = ler_data_hora_opcional("Nova data/hora ISO (enter para manter): ")
    pedido = atualizar_pedido(id_pedido, fk_mesa, valor_total, data_hora)
    if not pedido:
        print("Pedido nao encontrado.")
        return
    print(f"Pedido atualizado: {pedido}")


def remover_pedido():
    id_pedido = ler_inteiro("ID do pedido: ")
    pedido = deletar_pedido(id_pedido)
    if not pedido:
        print("Pedido nao encontrado.")
        return
    print("Pedido removido.")


def main():
    usuario_logado = None

    while not usuario_logado:
        exibir_menu_autenticacao()
        opcao = input("Escolha uma opcao: ").strip()

        if opcao == "0":
            print("Encerrando sistema.")
            return
        elif opcao == "1":
            usuario_logado = fazer_login()
        elif opcao == "2":
            usuario_logado = registrar_usuario()
        else:
            print("Opcao invalida.")

    acoes = {
        "1": mostrar_categorias,
        "2": cadastrar_categoria,
        "3": consultar_categoria,
        "4": alterar_categoria,
        "5": remover_categoria,
        "6": mostrar_produtos,
        "7": cadastrar_produto,
        "8": consultar_produto,
        "9": alterar_produto,
        "10": remover_produto,
        "11": mostrar_mesas,
        "12": registrar_mesa,
        "13": consultar_mesa,
        "14": alterar_mesa,
        "15": remover_mesa,
        "16": mostrar_pedidos,
        "17": registrar_pedido,
        "18": consultar_pedido,
        "19": alterar_pedido,
        "20": remover_pedido,
    }

    while True:
        exibir_menu(usuario_logado["nome"])
        opcao = input("Escolha uma opcao: ").strip()

        if opcao == "0":
            print(f"Ate logo, {usuario_logado['nome']}!")
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
