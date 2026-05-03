from sqlalchemy import Column, Integer, String, Numeric, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base


class Categoria(Base):
    """Representa a tabela CATEGORIA no banco de dados."""
    __tablename__ = "categoria"

    id_categoria = Column("id_categoria", Integer, primary_key=True, index=True)
    descricao = Column("descricao", String(100), nullable=False)

    # Um categoria pode ter vários produtos
    produtos = relationship("Produto", back_populates="categoria")


class Produto(Base):
    """Representa a tabela PRODUTO no banco de dados."""
    __tablename__ = "produto"

    id_produto = Column("id_produto", Integer, primary_key=True, index=True)
    nome = Column("nome", String(255), nullable=False)
    preco_unitario = Column("preco_unitario", Numeric(10, 2), nullable=False)
    fk_categoria = Column("fk_categoria", Integer, ForeignKey("categoria.id_categoria"))

    # Relacionamento de volta para a Categoria
    categoria = relationship("Categoria", back_populates="produtos")
