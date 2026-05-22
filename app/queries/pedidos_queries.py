from app.database import get_cursor


def listar_pedidos():
    with get_cursor() as cursor:
        cursor.execute(
            """
            SELECT
                id_pedido,
                data_hora,
                fk_mesa,
                valor_total::float AS valor_total
            FROM pedido
            ORDER BY id_pedido
            """
        )
        return cursor.fetchall()


def buscar_pedido_por_id(id_pedido):
    with get_cursor() as cursor:
        cursor.execute(
            """
            SELECT
                id_pedido,
                data_hora,
                fk_mesa,
                valor_total::float AS valor_total
            FROM pedido
            WHERE id_pedido = %s
            """,
            (id_pedido,),
        )
        return cursor.fetchone()


def criar_pedido(fk_mesa, valor_total, data_hora=None):
    with get_cursor(commit=True) as cursor:
        if data_hora is None:
            cursor.execute(
                """
                INSERT INTO pedido (fk_mesa, valor_total)
                VALUES (%s, %s)
                RETURNING
                    id_pedido,
                    data_hora,
                    fk_mesa,
                    valor_total::float AS valor_total
                """,
                (fk_mesa, valor_total),
            )
        else:
            cursor.execute(
                """
                INSERT INTO pedido (data_hora, fk_mesa, valor_total)
                VALUES (%s, %s, %s)
                RETURNING
                    id_pedido,
                    data_hora,
                    fk_mesa,
                    valor_total::float AS valor_total
                """,
                (data_hora, fk_mesa, valor_total),
            )
        return cursor.fetchone()


def atualizar_pedido(id_pedido, fk_mesa, valor_total, data_hora=None):
    with get_cursor(commit=True) as cursor:
        if data_hora is None:
            cursor.execute(
                """
                UPDATE pedido
                SET fk_mesa = %s,
                    valor_total = %s
                WHERE id_pedido = %s
                RETURNING
                    id_pedido,
                    data_hora,
                    fk_mesa,
                    valor_total::float AS valor_total
                """,
                (fk_mesa, valor_total, id_pedido),
            )
        else:
            cursor.execute(
                """
                UPDATE pedido
                SET data_hora = %s,
                    fk_mesa = %s,
                    valor_total = %s
                WHERE id_pedido = %s
                RETURNING
                    id_pedido,
                    data_hora,
                    fk_mesa,
                    valor_total::float AS valor_total
                """,
                (data_hora, fk_mesa, valor_total, id_pedido),
            )
        return cursor.fetchone()


def deletar_pedido(id_pedido):
    with get_cursor(commit=True) as cursor:
        cursor.execute(
            """
            DELETE FROM pedido
            WHERE id_pedido = %s
            RETURNING id_pedido
            """,
            (id_pedido,),
        )
        return cursor.fetchone()
