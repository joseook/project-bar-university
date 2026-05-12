from typing import List

from fastapi import APIRouter, HTTPException

from app.queries.categoria_queries import (
    atualizar_categoria,
    buscar_categoria_por_id,
    criar_categoria,
    deletar_categoria,
    listar_categorias,
)
from app.schemas import CategoriaCreate, CategoriaResponse

router = APIRouter(
    prefix="/categorias",
    tags=["Categorias"],
)


@router.get("/", response_model=List[CategoriaResponse])
def rota_listar_categorias():
    """Retorna todas as categorias cadastradas."""
    return listar_categorias()


@router.get("/{id_categoria}", response_model=CategoriaResponse)
def rota_buscar_categoria(id_categoria: int):
    """Retorna uma categoria pelo ID."""
    categoria = buscar_categoria_por_id(id_categoria)
    if not categoria:
        raise HTTPException(status_code=404, detail="Categoria nao encontrada")
    return categoria


@router.post("/", response_model=CategoriaResponse, status_code=201)
def rota_criar_categoria(dados: CategoriaCreate):
    """Cria uma nova categoria."""
    return criar_categoria(dados.descricao)


@router.put("/{id_categoria}", response_model=CategoriaResponse)
def rota_atualizar_categoria(id_categoria: int, dados: CategoriaCreate):
    """Atualiza a descricao de uma categoria existente."""
    categoria = atualizar_categoria(id_categoria, dados.descricao)
    if not categoria:
        raise HTTPException(status_code=404, detail="Categoria nao encontrada")
    return categoria


@router.delete("/{id_categoria}", status_code=204)
def rota_deletar_categoria(id_categoria: int):
    """Remove uma categoria pelo ID."""
    categoria = deletar_categoria(id_categoria)
    if not categoria:
        raise HTTPException(status_code=404, detail="Categoria nao encontrada")
