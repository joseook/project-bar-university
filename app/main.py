from fastapi import FastAPI

from app.routers import categoria, produto

app = FastAPI(
    title="Bar API",
    description="API para gerenciamento de categorias e produtos do bar",
    version="1.0.0",
)

app.include_router(categoria.router)
app.include_router(produto.router)


@app.get("/")
def raiz():
    return {"mensagem": "Bar API funcionando! Acesse /docs para ver os endpoints."}
