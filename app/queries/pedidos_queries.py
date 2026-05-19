from app.database import get_cursor

def criar_pedido (data_hora, valor_total, status_pagamento, id_mesa, id_funcionario):
    with get_cursor(commit=True) as cursor:
        if status_pagamento is None:
            cursor.execute(
                """
                INSERT INTO pedido (data_hora, valor_total, id_mesa, id_funcionario)
                VALUES (%s,%s,%s,%s)
                RETURNING *
                """,
                (data_hora, valor_total, id_mesa, id_funcionario)
            )
        else:
            cursor.execute(
                """
                INSERT INTO pedido (data_hora, valor_total, status_pagamento, id_mesa, id_funcionario)
                VALUES (%s, %s, %s, %s, %s)
                RETURNING *
                """,
                (data_hora, valor_total, status_pagamento, id_mesa, id_funcionario)
            )
        return cursor.fetchone()
    
def buscar_pedido_por_id(id_pedido):
    try:
        with get_cursor() as cursor:
            cursor.execute(
                """
                SELECT
                    p.id_pedido,
                    p.data_hora,
                    p.valor_total
                    p.status_pagamento
                    p.id_mesa
                    p.id_funcionario
                FROM pedido p
                WHERE p.id_pedido = %s
                """,
                (id_mesa,),
            )
            return cursor.fetchone()
    except Exception as e:
        raise