from app.database import get_cursor


def listar_categorias():
    with get_cursor() as cursor:
        cursor.execute(
            """
            SELECT id_categoria, descricao
            FROM categoria
            ORDER BY id_categoria
            """
        )
        return cursor.fetchall()


def buscar_categoria_por_id(id_categoria):
    with get_cursor() as cursor:
        cursor.execute(
            """
            SELECT id_categoria, descricao
            FROM categoria
            WHERE id_categoria = %s
            """,
            (id_categoria,),
        )
        return cursor.fetchone()


def criar_categoria(descricao):
    with get_cursor(commit=True) as cursor:
        cursor.execute(
            """
            INSERT INTO categoria (descricao)
            VALUES (%s)
            RETURNING id_categoria, descricao
            """,
            (descricao,),
        )
        return cursor.fetchone()


def atualizar_categoria(id_categoria, descricao):
    with get_cursor(commit=True) as cursor:
        cursor.execute(
            """
            UPDATE categoria
            SET descricao = %s
            WHERE id_categoria = %s
            RETURNING id_categoria, descricao
            """,
            (descricao, id_categoria),
        )
        return cursor.fetchone()


def deletar_categoria(id_categoria):
    with get_cursor(commit=True) as cursor:
        cursor.execute(
            """
            DELETE FROM categoria
            WHERE id_categoria = %s
            RETURNING id_categoria
            """,
            (id_categoria,),
        )
        return cursor.fetchone()
