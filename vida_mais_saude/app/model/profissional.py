from __future__ import annotations
from typing import Optional, TYPE_CHECKING

from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    validates,
    relationship,
)

from app.model._base import ModelBase
from app.model._associacoes import (
    dia_disponivel_m2m,
    horario_disponivel_m2m
)

if TYPE_CHECKING:
    from app.model import Especialidade, Agendamento, Dia, Hora

# As funções mapped_column e relationship retornam um decriptor, que já
# implementa, por padrão, getters e setters para os atributos da classe
class Profissional(ModelBase):
    """
    Classe de mapeamento da entitade 'profissional' do banco de dados
    """

    # Atributos da entidade
    id_profissional: Mapped[int] = mapped_column(
        autoincrement=True,
        primary_key=True,
        nullable=True,
        init=False,
    )
    nome: Mapped[str] = mapped_column(
        String(60),
        nullable=False,
    )
    telefone: Mapped[str] = mapped_column(
        String(11),
        nullable=False,
        unique=True,
    )
    id_especialidade: Mapped[int] = mapped_column(
        ForeignKey('especialidade.id_especialidade'),
        nullable=False,
    )
    descricao: Mapped[str] = mapped_column(
        nullable=False
    )
    registro_profissional: Mapped[Optional[str]] = mapped_column(
        String(15),
        nullable=True,
        unique=True,
        default=None
    )

    # Atributos de relacionamento
    especialidade: Mapped[Especialidade] = relationship(
        back_populates='profissionais',
        init=False,
        repr=False,
    )
    agendamentos: Mapped[list[Agendamento]] = relationship(
        back_populates='profissional',
        init=False,
        repr=False,
    )
    dias: Mapped[list[Dia]] = relationship(
        secondary=dia_disponivel_m2m,
        back_populates='profissionais',
        init=False,
        repr=False,
    )
    horarios: Mapped[list[Hora]] = relationship(
        secondary=horario_disponivel_m2m,
        back_populates='profissionais',
        init=False,
        repr=False,
    )

    # Validações
    @validates('id_profissional', 'id_especialidade')
    def _validate_int(self, key, int_):
        return self._validate_type(key, int_, int)

    @validates('descricao')
    def _validate_text(self, key, text):
        return self._validate_type(key, text, str)

    @validates('telefone')
    def _validate_varchar_11(self, key, varchar_11):
        return self._validate_length(key, varchar_11, 11)

    @validates('registro_profissional')
    def _validate_nullable_varchar_15(self, key, varchar_15):
        return self._validate_length(key, varchar_15, 15) if varchar_15 else None

    @validates('nome')
    def _validate_varchar_60(self, key, varchar_60):
        return self._validate_length(key, varchar_60, 60)
