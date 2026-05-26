from passlib.context import CryptContext

from app.database import get_cursor

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def _hash_senha(senha: str) -> str:
    return pwd_context.hash(senha)


def _verificar_senha(senha: str, senha_hash: str) -> bool:
    return pwd_context.verify(senha, senha_hash)


def criar_usuario(nome: str, login: str, senha: str):
    senha_hash = _hash_senha(senha)
    with get_cursor(commit=True) as cursor:
        cursor.execute(
            """
            INSERT INTO usuario (nome, login, senha_hash)
            VALUES (%s, %s, %s)
            RETURNING id_usuario, nome, login
            """,
            (nome, login, senha_hash),
        )
        return cursor.fetchone()


def buscar_usuario_por_login(login: str):
    with get_cursor() as cursor:
        cursor.execute(
            """
            SELECT id_usuario, nome, login, senha_hash
            FROM usuario
            WHERE login = %s
            """,
            (login,),
        )
        return cursor.fetchone()


def autenticar_usuario(login: str, senha: str):
    usuario = buscar_usuario_por_login(login)
    if not usuario:
        return None
    if not _verificar_senha(senha, usuario["senha_hash"]):
        return None
    return {
        "id_usuario": usuario["id_usuario"],
        "nome": usuario["nome"],
        "login": usuario["login"],
    }
