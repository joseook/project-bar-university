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

def criar_mesa(numero, status):
    with get_cursor(commit=True) as cursor:
        if status is None:
            cursor.execute(
                """
                INSERT INTO mesa (numero)
                VALUES (%s)
                RETURNING *
                """,
                (numero,)
            )
        else:
            cursor.execute(
                """
                INSERT INTO mesa (numero, status)
                VALUES (%s, %s)
                RETURNING *
                """,
                (numero, status)
            )
        return cursor.fetchone()
