from typing import Any

from src.services.service_base import BaseService
from src.adapters.repositories import EntityRepository
from src.adapters.database.models.usuario_model import UsuarioModel
from src.schemas.usuario_schema import CreateUsuarioPayload, ResponseUsuarioPayload, UpdateUsuarioPayload


class UsuarioService(BaseService):
    def __init__(self, repository: EntityRepository) -> None:
        self.repository = repository
    
    def get_all(self):
        values= self.query_result(result=self.repository.usuario.get_all())
        rows = [ResponseUsuarioPayload.model_validate(i).model_dump() for i in values]
        return {
            'items': rows,
            'quantidade': len(rows)
        }
     
    def get(self, id: int) -> dict | None:
        row = self.query_result(self.repository.usuario.search_by_id(model_id=id))
        if not row:
            return None
        return row.__dict__
     
    def getByCpf(self, cpf: str) -> dict | None:
        row = self.query_result(self.repository.usuario.search_by_cpf(cpf=cpf))
        if not row:
            return None
        return row.__dict__
    
    def create(self, data: CreateUsuarioPayload) -> dict | None:
        row = UsuarioModel(**dict(data))
        self.repository.usuario.save(model=row)
        self.repository.usuario.model_refresh(model=row)
        return ResponseUsuarioPayload.model_validate(row).model_dump()

    # def update(self, data: UpdateUsuarioPayload) -> ResponseUsuarioPayload:
    #     self.repository.usuario.update(model_id=data.id, values=dict(data))
    #     row = self.repository.usuario.search_by_id(model_id=data.id)
    #     return ResponseUsuarioPayload.model_validate(row).model_dump()

    # def delete(self, id: int) -> ResponseUsuarioPayload:
    #     self.repository.usuario.delete(model_id=id)
    #     row = self.repository.usuario.delete(model_id=id)
    #     return ResponseUsuarioPayload.model_validate(row).model_dump()
    