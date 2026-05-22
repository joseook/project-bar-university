from app.database import get_cursor


def listar_mesas():
    with get_cursor() as cursor:
        cursor.execute(
            """
            SELECT id_mesa, numero, status
            FROM mesa
            ORDER BY id_mesa
            """
        )
        return cursor.fetchall()


def criar_mesa(numero, status):
    with get_cursor(commit=True) as cursor:
        if status is None:
            cursor.execute(
                """
                INSERT INTO mesa (numero)
                VALUES (%s)
                RETURNING id_mesa, numero, status
                """,
                (numero,),
            )
        else:
            cursor.execute(
                """
                INSERT INTO mesa (numero, status)
                VALUES (%s, %s)
                RETURNING id_mesa, numero, status
                """,
                (numero, status),
            )
        return cursor.fetchone()


def buscar_mesa_por_id(id_mesa):
    with get_cursor() as cursor:
        cursor.execute(
            """
            SELECT id_mesa, numero, status
            FROM mesa
            WHERE id_mesa = %s
            """,
            (id_mesa,),
        )
        return cursor.fetchone()


def atualizar_mesa(id_mesa, numero, status):
    with get_cursor(commit=True) as cursor:
        cursor.execute(
            """
            UPDATE mesa
            SET numero = %s,
                status = %s
            WHERE id_mesa = %s
            RETURNING id_mesa, numero, status
            """,
            (numero, status, id_mesa),
        )
        return cursor.fetchone()


def deletar_mesa(id_mesa):
    with get_cursor(commit=True) as cursor:
        cursor.execute(
            """
            DELETE FROM mesa
            WHERE id_mesa = %s
            RETURNING id_mesa
            """,
            (id_mesa,),
        )
        return cursor.fetchone()
