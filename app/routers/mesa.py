from typing import List

from fastapi import APIRouter, HTTPException

from app.schemas import MesaCreate, MesaResponse
from app.queries.mesa_queries import (
    atualizar_mesa,
    buscar_mesa_por_id,
    criar_mesa,
    deletar_mesa,
    listar_mesas,
)

router = APIRouter(
    prefix="/mesas",
    tags=["Mesas"],
)


@router.get("/", response_model=List[MesaResponse])
def rota_listar_mesas():
    """Retorna todas as mesas cadastradas."""
    return listar_mesas()


@router.get("/{id_mesa}", response_model=MesaResponse)
def rota_buscar_mesa(id_mesa: int):
    """Retorna uma mesa pelo ID."""
    mesa = buscar_mesa_por_id(id_mesa)
    if not mesa:
        raise HTTPException(status_code=404, detail="Mesa nao encontrada")
    return mesa


@router.post("/", response_model=MesaResponse, status_code=201)
def rota_criar_mesa(dados: MesaCreate):
    """Cria uma nova mesa."""
    return criar_mesa(numero=dados.numero, status=dados.status)


@router.put("/{id_mesa}", response_model=MesaResponse)
def rota_atualizar_mesa(id_mesa: int, dados: MesaCreate):
    """Atualiza os dados de uma mesa existente."""
    mesa = atualizar_mesa(
        id_mesa=id_mesa,
        numero=dados.numero,
        status=dados.status,
    )
    if not mesa:
        raise HTTPException(status_code=404, detail="Mesa nao encontrada")
    return mesa


@router.delete("/{id_mesa}", status_code=204)
def rota_deletar_mesa(id_mesa: int):
    """Remove uma mesa pelo ID."""
    mesa = deletar_mesa(id_mesa)
    if not mesa:
        raise HTTPException(status_code=404, detail="Mesa nao encontrada")
