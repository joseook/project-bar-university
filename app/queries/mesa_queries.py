from app.database import get_cursor


def listar_mesas():
    with get_cursor() as cursor:
        cursor.execute(
            """
            SELECT *
            FROM mesa
            ORDER BY id_mesa
            """
        )
        return cursor.fetchall()
