from datetime import date

from sqlalchemy import ForeignKey
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    validates,
    relationship,
)

from app.model._base import ModelBase

# A função mapped_column retorna um decriptor, que já implementa, por
# padrão, getters e setters para os atributos da classe
class Agendamento(ModelBase):
    """
    Classe de mapeamento da entitade 'agendamento' do banco de dados
    """

    # Atributos da entidade
    id_agendamento: Mapped[int] = mapped_column(
        autoincrement=True,
        primary_key=True,
        nullable=True,
        init=False,
    )
    id_profissional: Mapped[int] = mapped_column(
        ForeignKey('profissional.id_profissional'),
        nullable=False,
    )
    id_cliente: Mapped[int] = mapped_column(
        ForeignKey('cliente.id_cliente'),
        nullable=False,
    )
    id_hora: Mapped[int] = mapped_column(
        ForeignKey('hora.id_hora'),
        nullable=False,
    )
    id_dia: Mapped[int] = mapped_column(
        ForeignKey('dia.id_dia'),
        nullable=False,
    )
    data: Mapped[date] = mapped_column(
        nullable=False,
    )

    # Atributos de relacionamento
    # pendente

    # Validações
    @validates(
            'id_agendamento', 'id_profissional', 'id_cliente',
            'id_hora', 'id_dia'
    )
    def _validate_int(self, key, int_):
        return self._validate_type(key, int_, int)

    @validates('data')
    def _validate_date(self, key, date_):
        return self._validate_type(key, date_, date)
