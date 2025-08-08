from __future__ import annotations
from typing import TYPE_CHECKING

from sqlalchemy import String
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    validates,
    relationship,
)

from app.model._base import ModelBase
from app.model._associacoes import dia_disponivel_m2m

if TYPE_CHECKING:
    from app.model import Profissional, Agendamento

# As funções mapped_column e relationship retornam um decriptor, que já
# implementa, por padrão, getters e setters para os atributos da classe
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
    profissionais: Mapped[list[Profissional]] = relationship(
        secondary=dia_disponivel_m2m,
        back_populates='dias',
        init=False,
        repr=False,
    )
    agendamentos: Mapped[list[Agendamento]] = relationship(
        back_populates='dia',
        init=False,
        repr=False,
    )

    # Validações
    @validates('id_dia')
    def _validate_int(self, key, int_):
        return self._validate_type(key, int_, int)

    @validates('nome')
    def _validate_varchar_15(self, key, varchar_15):
        return self._validate_length(key, varchar_15, 15)
