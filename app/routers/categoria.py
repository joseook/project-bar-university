from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db
from app.models import Categoria
from app.schemas import CategoriaCreate, CategoriaResponse

router = APIRouter(
    prefix="/categorias",
    tags=["Categorias"],
)


@router.get("/", response_model=List[CategoriaResponse])
def listar_categorias(db: Session = Depends(get_db)):
    """Retorna todas as categorias cadastradas."""
    return db.query(Categoria).all()


@router.get("/{id_categoria}", response_model=CategoriaResponse)
def buscar_categoria(id_categoria: int, db: Session = Depends(get_db)):
    """Retorna uma categoria pelo ID."""
    categoria = db.query(Categoria).filter(Categoria.id_categoria == id_categoria).first()
    if not categoria:
        raise HTTPException(status_code=404, detail="Categoria não encontrada")
    return categoria


@router.post("/", response_model=CategoriaResponse, status_code=201)
def criar_categoria(dados: CategoriaCreate, db: Session = Depends(get_db)):
    """Cria uma nova categoria."""
    nova_categoria = Categoria(descricao=dados.descricao)
    db.add(nova_categoria)
    db.commit()
    db.refresh(nova_categoria)
    return nova_categoria


@router.put("/{id_categoria}", response_model=CategoriaResponse)
def atualizar_categoria(id_categoria: int, dados: CategoriaCreate, db: Session = Depends(get_db)):
    """Atualiza a descrição de uma categoria existente."""
    categoria = db.query(Categoria).filter(Categoria.id_categoria == id_categoria).first()
    if not categoria:
        raise HTTPException(status_code=404, detail="Categoria não encontrada")
    categoria.descricao = dados.descricao
    db.commit()
    db.refresh(categoria)
    return categoria


@router.delete("/{id_categoria}", status_code=204)
def deletar_categoria(id_categoria: int, db: Session = Depends(get_db)):
    """Remove uma categoria pelo ID."""
    categoria = db.query(Categoria).filter(Categoria.id_categoria == id_categoria).first()
    if not categoria:
        raise HTTPException(status_code=404, detail="Categoria não encontrada")
    db.delete(categoria)
    db.commit()
