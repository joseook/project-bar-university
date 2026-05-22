from typing import List

from fastapi import APIRouter, HTTPException

from app.queries.pedidos_queries import (
    atualizar_pedido,
    buscar_pedido_por_id,
    criar_pedido,
    deletar_pedido,
    listar_pedidos,
)
from app.schemas import PedidoCreate, PedidoResponse

router = APIRouter(
    prefix="/pedidos",
    tags=["Pedidos"],
)


@router.get("/", response_model=List[PedidoResponse])
def rota_listar_pedidos():
    """Retorna todos os pedidos cadastrados."""
    return listar_pedidos()


@router.get("/{id_pedido}", response_model=PedidoResponse)
def rota_buscar_pedido(id_pedido: int):
    """Retorna um pedido pelo ID."""
    pedido = buscar_pedido_por_id(id_pedido)
    if not pedido:
        raise HTTPException(status_code=404, detail="Pedido nao encontrado")
    return pedido


@router.post("/", response_model=PedidoResponse, status_code=201)
def rota_criar_pedido(dados: PedidoCreate):
    """Cria um novo pedido."""
    return criar_pedido(
        fk_mesa=dados.fk_mesa,
        valor_total=dados.valor_total,
        data_hora=dados.data_hora,
    )


@router.put("/{id_pedido}", response_model=PedidoResponse)
def rota_atualizar_pedido(id_pedido: int, dados: PedidoCreate):
    """Atualiza os dados de um pedido existente."""
    pedido = atualizar_pedido(
        id_pedido=id_pedido,
        fk_mesa=dados.fk_mesa,
        valor_total=dados.valor_total,
        data_hora=dados.data_hora,
    )
    if not pedido:
        raise HTTPException(status_code=404, detail="Pedido nao encontrado")
    return pedido


@router.delete("/{id_pedido}", status_code=204)
def rota_deletar_pedido(id_pedido: int):
    """Remove um pedido pelo ID."""
    pedido = deletar_pedido(id_pedido)
    if not pedido:
        raise HTTPException(status_code=404, detail="Pedido nao encontrado")
