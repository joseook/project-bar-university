from typing import List

from fastapi import APIRouter, HTTPException

from app.queries.mesa_queries import listar_mesas

router = APIRouter()


@router.get("/mesas", response_model=List[dict])
async def get_mesas():
    mesas = listar_mesas()
    return mesas
