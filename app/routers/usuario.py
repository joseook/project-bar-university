from fastapi import APIRouter, HTTPException

from app.queries.usuario_queries import (
    autenticar_usuario,
    buscar_usuario_por_login,
    criar_usuario,
)
from app.schemas import UsuarioCreate, UsuarioLogin, UsuarioResponse

router = APIRouter(
    prefix="/usuarios",
    tags=["Usuarios"],
)


@router.post("/registro", response_model=UsuarioResponse, status_code=201)
def rota_registrar_usuario(dados: UsuarioCreate):
    """Registra um novo usuario no sistema."""
    if buscar_usuario_por_login(dados.login):
        raise HTTPException(status_code=400, detail="Login ja esta em uso")
    return criar_usuario(dados.nome, dados.login, dados.senha)


@router.post("/login", response_model=UsuarioResponse)
def rota_login(dados: UsuarioLogin):
    """Autentica um usuario pelo login e senha."""
    usuario = autenticar_usuario(dados.login, dados.senha)
    if not usuario:
        raise HTTPException(status_code=401, detail="Login ou senha invalidos")
    return usuario
