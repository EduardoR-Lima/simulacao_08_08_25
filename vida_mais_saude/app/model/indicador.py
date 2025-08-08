from __future__ import annotations
from typing import Optional, TYPE_CHECKING
from datetime import datetime

from sqlalchemy import String, ForeignKey, func
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    validates,
    relationship,
)

from app.model._base import ModelBase

if TYPE_CHECKING:
    from app.model import Cliente

# As funções mapped_column e relationship retornam um decriptor, que já 
# implementa, por padrão, getters e setters para os atributos da classe
class Indicador(ModelBase):
    """
    Classe de mapeamento da entitade 'indicador' do banco de dados
    """

    # Atributos da entidade
    id_indicador: Mapped[int] = mapped_column(
        autoincrement=True,
        primary_key=True,
        nullable=True,
        init=False,
    )
    tipo: Mapped[str] = mapped_column(
        String(45),
        nullable=False,
    )
    valor: Mapped[str] = mapped_column(
        String(15),
        nullable=False,
    )
    id_cliente: Mapped[int] = mapped_column(
        ForeignKey('cliente.id_cliente'),
        nullable=False
    )
    observacoes: Mapped[Optional[str]] = mapped_column(
        nullable=True,
        default=None,
    )
    data_registro: Mapped[datetime] = mapped_column(
        server_default=func.current_timestamp(),
        nullable=False,
        init=False,
    )

    # Atributos de relacionamento
    cliente: Mapped[Cliente] = relationship(
        back_populates='indicadores',
        init=False,
        repr=False,
    )

    # Validações
    @validates('id_indicador', 'id_cliente')
    def _validate_int(self, key, int_):
        return self._validate_type(key, int_, int)

    @validates('data_registro')
    def _validate_datetime(self, key, datetime_):
        return self._validate_type(key, datetime_, datetime)

    @validates('observacoes')
    def _validate_nullable_text(self, key, text):
        return self._validate_type(key, text, str) if text else None

    @validates('valor')
    def _validate_varchar_15(self, key, varchar_15):
        return self._validate_length(key, varchar_15, 15)

    @validates('tipo')
    def _validate_varchar_45(self, key, varchar_45):
        return self._validate_length(key, varchar_45, 45)
