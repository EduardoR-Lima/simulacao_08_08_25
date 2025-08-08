from werkzeug.security import check_password_hash, generate_password_hash

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
class Cliente(ModelBase):
    """
    Classe de mapeamento da entitade 'cliente' do banco de dados
    """

    # Atributos da entidade
    id_cliente: Mapped[int] = mapped_column(
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
    cpf: Mapped[str] = mapped_column(
        String(11),
        nullable=False,
        unique=True,
    )
    rua: Mapped[str] = mapped_column(
        String(45),
        nullable=False,
    )
    numero: Mapped[int] = mapped_column(
        nullable=False,
    )
    email: Mapped[str] = mapped_column(
        String(60),
        nullable=False,
        unique=True,
    )
    # Atributo não público. Deve ser acessado através dos métodos
    # atribuir_senha e validar_senha
    _hash_senha: Mapped[str] = mapped_column(
        String(162),
        name='hash_senha',
        nullable=False,
        init=False,
        repr=False,
    )

    # Atributos de relacionamento
    # pendente

    def atribuir_senha(self, senha: str):
        """
        Atribui uma nova senha ao usuário aplicando os procedimentos
        de hash

        :param senha: a senha crua em formato de texto
        """
        self._hash_senha = generate_password_hash(senha)

    def validar_senha(self, senha: str):
        """
        Verifica se a senha passa corresponde ao hash que está armazenado
        no banco de dados

        :param senha: a senha crua em formato de texto
        """
        return check_password_hash(self._hash_senha, senha)

    # Validações
    @validates('id_cliente', 'numero')
    def _validate_int(self, key, int_):
        return self._validate_type(key, int_, int)

    @validates('cpf', 'telefone')
    def _validate_varchar_11(self, key, varchar_11):
        return self._validate_length(key, varchar_11, 11)

    @validates('rua')
    def _validate_varchar_45(self, key, varchar_45):
        return self._validate_length(key, varchar_45, 45)

    @validates('nome', 'email')
    def _validate_varchar_60(self, key, varchar_60):
        return self._validate_length(key, varchar_60, 60)

    @validates('hash_senha')
    def _validate_varchar_162(self, key, varchar_162):
        return self._validate_length(key, varchar_162, 162)
