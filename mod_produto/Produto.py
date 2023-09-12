from pydantic import BaseModel


class Produto(BaseModel):
    id_produto: int = None
    nome: str
    descricao: str = None
    foto: str
    valor_unit: int
