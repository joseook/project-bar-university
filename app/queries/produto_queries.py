from app.database import get_cursor


def listar_produtos():
    try:
        with get_cursor() as cursor:
            cursor.execute(
                """
                SELECT
                    p.id_produto,
                    p.nome,
                    p.preco_unitario::float AS preco_unitario,
                    p.fk_categoria,
                    c.descricao AS categoria_descricao
                FROM produto p
                LEFT JOIN categoria c ON c.id_categoria = p.fk_categoria
                ORDER BY p.id_produto
                """
            )
            return cursor.fetchall()
    except Exception as e:
        raise


def buscar_produto_por_id(id_produto):
    try:
        with get_cursor() as cursor:
            cursor.execute(
                """
                SELECT
                    p.id_produto,
                    p.nome,
                    p.preco_unitario::float AS preco_unitario,
                    p.fk_categoria,
                    c.descricao AS categoria_descricao
                FROM produto p
                LEFT JOIN categoria c ON c.id_categoria = p.fk_categoria
                WHERE p.id_produto = %s
                """,
                (id_produto,),
            )
            return cursor.fetchone()
    except Exception as e:
        raise


def criar_produto(nome, preco_unitario, fk_categoria):
    try:
        with get_cursor(commit=True) as cursor:
            cursor.execute(
                """
                INSERT INTO produto (nome, preco_unitario, fk_categoria)
                VALUES (%s, %s, %s)
                RETURNING id_produto
                """,
                (nome, preco_unitario, fk_categoria),
            )
            novo_produto = cursor.fetchone()
            cursor.execute(
                """
                SELECT
                    p.id_produto,
                    p.nome,
                    p.preco_unitario::float AS preco_unitario,
                    p.fk_categoria,
                    c.descricao AS categoria_descricao
                FROM produto p
                LEFT JOIN categoria c ON c.id_categoria = p.fk_categoria
                WHERE p.id_produto = %s
                """,
                (novo_produto["id_produto"],),
            )
            return cursor.fetchone()
    except Exception as e:
        raise


def atualizar_produto(id_produto, nome, preco_unitario, fk_categoria):
    try:
        with get_cursor(commit=True) as cursor:
            cursor.execute(
                """
                UPDATE produto
                SET nome = %s,
                    preco_unitario = %s,
                    fk_categoria = %s
                WHERE id_produto = %s
                RETURNING id_produto
                """,
                (nome, preco_unitario, fk_categoria, id_produto),
            )
            produto_atualizado = cursor.fetchone()
            if not produto_atualizado:
                return None
            cursor.execute(
                """
                SELECT
                    p.id_produto,
                    p.nome,
                    p.preco_unitario::float AS preco_unitario,
                    p.fk_categoria,
                    c.descricao AS categoria_descricao
                FROM produto p
                LEFT JOIN categoria c ON c.id_categoria = p.fk_categoria
                WHERE p.id_produto = %s
                """,
                (produto_atualizado["id_produto"],),
            )
            return cursor.fetchone()
    except Exception as e:
        raise


def deletar_produto(id_produto):
    try:
        with get_cursor(commit=True) as cursor:
            cursor.execute(
                """
                DELETE FROM produto
                WHERE id_produto = %s
                RETURNING id_produto
                """,
                (id_produto,),
            )
            return cursor.fetchone()
    except Exception as e:
        raise
