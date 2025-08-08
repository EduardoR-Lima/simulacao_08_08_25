from __future__ import annotations
from typing import TYPE_CHECKING
from datetime import time

from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    validates,
    relationship,
)

from app.model._base import ModelBase
from app.model._associacoes import horario_disponivel_m2m

if TYPE_CHECKING:
    from app.model import Profissional, Agendamento

# As funções mapped_column e relationship retornam um decriptor, que já 
# implementa, por padrão, getters e setters para os atributos da classe
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
    profissionais: Mapped[list[Profissional]] = relationship(
        secondary=horario_disponivel_m2m,
        back_populates='horarios',
        init=False,
        repr=False,
    )
    agendamentos: Mapped[list[Agendamento]] = relationship(
        back_populates='hora',
        init=False,
        repr=False,
    )

    # Validações
    @validates('id_hora')
    def _validate_int(self, key, int_):
        return self._validate_type(key, int_, int)

    @validates('valor')
    def _validate_time(self, key, time_):
        return self._validate_type(key, time_, time)
