from fastapi import FastAPI

from app.routers import categoria, mesa, pedido, produto, usuario

app = FastAPI(
    title="Bar API",
    description="API para gerenciamento de categorias, produtos, mesas e pedidos do bar",
    version="1.0.0",
)

app.include_router(usuario.router)
app.include_router(categoria.router)
app.include_router(produto.router)
app.include_router(mesa.router)
app.include_router(pedido.router)


@app.get("/")
def raiz():
    return {"mensagem": "Bar API funcionando! Acesse /docs para ver os endpoints."}
