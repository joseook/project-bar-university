from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db
from app.models import Produto
from app.schemas import ProdutoCreate, ProdutoResponse

router = APIRouter(
    prefix="/produtos",
    tags=["Produtos"],
)


@router.get("/", response_model=List[ProdutoResponse])
def listar_produtos(db: Session = Depends(get_db)):
    """Retorna todos os produtos cadastrados."""
    return db.query(Produto).all()


@router.get("/{id_produto}", response_model=ProdutoResponse)
def buscar_produto(id_produto: int, db: Session = Depends(get_db)):
    """Retorna um produto pelo ID."""
    produto = db.query(Produto).filter(Produto.id_produto == id_produto).first()
    if not produto:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    return produto


@router.post("/", response_model=ProdutoResponse, status_code=201)
def criar_produto(dados: ProdutoCreate, db: Session = Depends(get_db)):
    """Cria um novo produto."""
    novo_produto = Produto(
        nome=dados.nome,
        preco_unitario=dados.preco_unitario,
        fk_categoria=dados.fk_categoria,
    )
    db.add(novo_produto)
    db.commit()
    db.refresh(novo_produto)
    return novo_produto


@router.put("/{id_produto}", response_model=ProdutoResponse)
def atualizar_produto(id_produto: int, dados: ProdutoCreate, db: Session = Depends(get_db)):
    """Atualiza os dados de um produto existente."""
    produto = db.query(Produto).filter(Produto.id_produto == id_produto).first()
    if not produto:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    produto.nome = dados.nome
    produto.preco_unitario = dados.preco_unitario
    produto.fk_categoria = dados.fk_categoria
    db.commit()
    db.refresh(produto)
    return produto


@router.delete("/{id_produto}", status_code=204)
def deletar_produto(id_produto: int, db: Session = Depends(get_db)):
    """Remove um produto pelo ID."""
    produto = db.query(Produto).filter(Produto.id_produto == id_produto).first()
    if not produto:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    db.delete(produto)
    db.commit()
