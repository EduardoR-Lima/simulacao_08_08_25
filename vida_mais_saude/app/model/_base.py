from typing import TypeVar

from sqlalchemy.orm import MappedAsDataclass

from app.database import db

T = TypeVar('T')

class ModelBase(db.Model, MappedAsDataclass):
    # Informa a ORM de que essa tabela não deve ser mapeada
    __abstract__ = True

    def _validate_type(self, key: str, value: T, type_: type[T]) -> T:
        _cls_name = self.__class__.__qualname__

        if not isinstance(value, type_):
            raise TypeError(
                f"'{_cls_name}.{key}' aceita apenas valores do tipo {type_!r}, "
                f"entretanto recebeu um valor do tipo {type(value)}: {value!r}"
            )

        return value

    def _validate_length(
            self, key: str, value: str,
            length: int, strict: bool = False
    ) -> str:
        self._validate_type(key, value, str)

        _cls_name = self.__class__.__qualname__
        _len = len(value)

        if strict and _len != length:
            raise ValueError(
                f"'{_cls_name}.{key}' aceita apenas 'str' com um coprimento "
                f"exato de {length} caracteres, entretanto recebeu um valor de "
                f"{_len} caracteres: {value!r}"
            )
        elif _len > length:
            raise ValueError(
                f"'{_cls_name}.{key}' aceita apenas 'str' com um coprimento "
                f"menor ou igual a {length} caracteres, entretanto recebeu um "
                f"valor de {_len} caracteres: {value!r}"
            )

        return value
