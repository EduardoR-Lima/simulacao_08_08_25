from sqlalchemy import ForeignKey, Column

from app.database import db

dia_disponivel_m2m = db.Table(
    'dia_disponivel',
    Column(
        'id_dia',
        ForeignKey('dia.id_dia'),
        primary_key=True,
    ),
    Column(
        'id_profissional',
        ForeignKey('profissional.id_profissional'),
        primary_key=True,
    ),
)
horario_disponivel_m2m = db.Table(
    'horario_disponivel',
    Column(
        'id_hora',
        ForeignKey('hora.id_hora'),
        primary_key=True,
    ),
    Column(
        'id_profissional',
        ForeignKey('profissional.id_profissional'),
        primary_key=True,
    ),
)
