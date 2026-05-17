from optparse import Option
from typing import Optional
from pydantic import BaseModel

class CategoriaBase(BaseModel):
    descricao: str


class CategoriaCreate(CategoriaBase):
    pass


class CategoriaResponse(CategoriaBase):
    id_categoria: int


class ProdutoBase(BaseModel):
    nome: str
    preco_unitario: float
    fk_categoria: Optional[int] = None

class ProdutoCreate(ProdutoBase):
    pass

class ProdutoResponse(ProdutoBase):
    id_produto: int
    categoria_descricao: Optional[str] = None

class MesaBase(BaseModel):
    numero: int
    status: Optional[str] = None

class MesaCreate(MesaBase):
    pass

class MesaResponse(MesaBase):
    id_mesa: int
