from pydantic import BaseModel


class Cliente(BaseModel):
    nome: str = None
    cpf: str = None
    telefone: str = None
    marca_fiado: bool = False  # True para sim, False para não
    dia_fiado: int = 0  # 0 para dias corridos, 1~31 para dia fixo
    senha: str = None

    def validate_fields(self):
        if self.marca_fiado:
            if (
                self.nome is None
                or self.cpf is None
                or self.telefone is None
                or self.senha is None
            ):
                raise ValueError("Todos os campos são obrigatórios para compra fiado.")
        elif self.nome is None:
            raise ValueError("O campo nome é obrigatório.")
