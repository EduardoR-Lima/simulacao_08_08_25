from sqlalchemy import String
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    validates,
    relationship,
)

from app.model._base import ModelBase

# A função mapped_column retorna um decriptor, que já implementa, por
# padrão, getters e setters para os atributos da classe
class Especialidade(ModelBase):
    """
    Classe de mapeamento da entitade 'especialidade' do banco de dados
    """

    # Atributos da entidade
    id_especialidade: Mapped[int] = mapped_column(
        autoincrement=True,
        primary_key=True,
        nullable=True,
        init=False,
    )
    nome: Mapped[str] = mapped_column(
        String(45),
        nullable=False,
    )

    # Atributos de relacionamento
    # pendente

    # Validações
    @validates('id_especialidade')
    def _validate_int(self, key, int_):
        return self._validate_type(key, int_, int)

    @validates('nome')
    def _validate_varchar_45(self, key, varchar_45):
        return self._validate_length(key, varchar_45, 45)
