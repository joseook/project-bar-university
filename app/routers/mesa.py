from typing import List
from fastapi import APIRouter, HTTPException
from app.schemas import MesaBase, MesaCreate, MesaResponse

from app.queries.mesa_queries import (
    listar_mesas,
    criar_mesa,

)
router = APIRouter(
    prefix="/mesas",
    tags=["Mesas"],
)

@router.get("/", response_model=List[MesaResponse])
def rota_listar_mesas():
    """Retorna todas as mesas cadastrados."""
    try:
        mesas = listar_mesas()
        return mesas
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/", response_model=MesaResponse, status_code=201)
def rota_criar_mesa(mesa: MesaCreate):
    """Cria uma nova mesa."""
    try:
        mesa = criar_mesa(
            numero=mesa.numero,
            status=mesa.status
        )
        return mesa
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
