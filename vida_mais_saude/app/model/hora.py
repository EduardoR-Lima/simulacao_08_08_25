from datetime import time

from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    validates,
    relationship,
)

from app.model._base import ModelBase

# A função mapped_column retorna um decriptor, que já implementa, por
# padrão, getters e setters para os atributos da classe
class Hora(ModelBase):
    """
    Classe de mapeamento da entitade 'hora' do banco de dados
    """

    # Atributos da entidade
    id_hora: Mapped[int] = mapped_column(
        primary_key=True,
        nullable=True,
    )
    valor: Mapped[time] = mapped_column(
        nullable=False,
    )

    # Atributos de relacionamento
    # pendente

    # Validações
    @validates('id_hora')
    def _validate_int(self, key, int_):
        return self._validate_type(key, int_, int)

    @validates('valor')
    def _validate_time(self, key, time_):
        return self._validate_type(key, time_, time)
