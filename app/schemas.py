from pydantic import BaseModel
from typing import Optional


# ----- CATEGORIA -----

class CategoriaBase(BaseModel):
    descricao: str


class CategoriaCreate(CategoriaBase):
    """Dados necessários para criar uma categoria."""
    pass


class CategoriaResponse(CategoriaBase):
    """Dados retornados ao consultar uma categoria."""
    id_categoria: int

    class Config:
        from_attributes = True  # permite converter objeto SQLAlchemy → JSON


# ----- PRODUTO -----

class ProdutoBase(BaseModel):
    nome: str
    preco_unitario: float
    fk_categoria: Optional[int] = None


class ProdutoCreate(ProdutoBase):
    """Dados necessários para criar um produto."""
    pass


class ProdutoResponse(ProdutoBase):
    """Dados retornados ao consultar um produto."""
    id_produto: int

    class Config:
        from_attributes = True
