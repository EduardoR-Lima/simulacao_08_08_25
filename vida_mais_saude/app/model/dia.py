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
class Dia(ModelBase):
    """
    Classe de mapeamento da entitade 'dia' do banco de dados
    """

    # Atributos da entidade
    id_dia: Mapped[int] = mapped_column(
        primary_key=True,
        nullable=True,
    )
    nome: Mapped[str] = mapped_column(
        String(15),
        nullable=False,
    )

    # Atributos de relacionamento
    # pendente

    # Validações
    @validates('id_dia')
    def _validate_int(self, key, int_):
        return self._validate_type(key, int_, int)

    @validates('nome')
    def _validate_varchar_15(self, key, varchar_15):
        return self._validate_length(key, varchar_15, 15)
