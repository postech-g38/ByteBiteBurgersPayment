from datetime import datetime

from pydantic import BaseModel


class CreateUsuarioPayload(BaseModel):
    id: int
    nome: str
    senha: str
    cpf: str | None
    tipo: int


class UpdateUsuarioPayload(CreateUsuarioPayload):
    id: int
    tipo: str


class ResponseUsuarioPayload(CreateUsuarioPayload):
    created_at: datetime
    updated_at: datetime | None
    deleted_at: datetime | None


class ResponsePagination(BaseModel):
    items: list[dict] | None
    quantidade: int
