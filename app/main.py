from fastapi import FastAPI
from app.database import engine, Base
from app.routers import categoria, produto

# Cria as tabelas no banco caso ainda não existam
# (o init.sql já faz isso no Docker, mas isso garante fora do Docker também)
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Bar API",
    description="API para gerenciamento de categorias e produtos do bar",
    version="1.0.0",
)

# Registra as rotas de cada módulo
app.include_router(categoria.router)
app.include_router(produto.router)


@app.get("/")
def raiz():
    return {"mensagem": "Bar API funcionando! Acesse /docs para ver os endpoints."}
