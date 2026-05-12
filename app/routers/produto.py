from typing import List

from fastapi import APIRouter, HTTPException

from app.queries.produto_queries import (
    atualizar_produto,
    buscar_produto_por_id,
    criar_produto,
    deletar_produto,
    listar_produtos,
)
from app.schemas import ProdutoCreate, ProdutoResponse

router = APIRouter(
    prefix="/produtos",
    tags=["Produtos"],
)


@router.get("/", response_model=List[ProdutoResponse])
def rota_listar_produtos():
    """Retorna todos os produtos cadastrados."""
    return listar_produtos()


@router.get("/{id_produto}", response_model=ProdutoResponse)
def rota_buscar_produto(id_produto: int):
    """Retorna um produto pelo ID."""
    produto = buscar_produto_por_id(id_produto)
    if not produto:
        raise HTTPException(status_code=404, detail="Produto nao encontrado")
    return produto


@router.post("/", response_model=ProdutoResponse, status_code=201)
def rota_criar_produto(dados: ProdutoCreate):
    """Cria um novo produto."""
    return criar_produto(
        nome=dados.nome,
        preco_unitario=dados.preco_unitario,
        fk_categoria=dados.fk_categoria,
    )


@router.put("/{id_produto}", response_model=ProdutoResponse)
def rota_atualizar_produto(id_produto: int, dados: ProdutoCreate):
    """Atualiza os dados de um produto existente."""
    produto = atualizar_produto(
        id_produto=id_produto,
        nome=dados.nome,
        preco_unitario=dados.preco_unitario,
        fk_categoria=dados.fk_categoria,
    )
    if not produto:
        raise HTTPException(status_code=404, detail="Produto nao encontrado")
    return produto


@router.delete("/{id_produto}", status_code=204)
def rota_deletar_produto(id_produto: int):
    """Remove um produto pelo ID."""
    produto = deletar_produto(id_produto)
    if not produto:
        raise HTTPException(status_code=404, detail="Produto nao encontrado")
