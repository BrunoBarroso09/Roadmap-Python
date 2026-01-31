import uuid
from typing import Final

class GenerateUUID:

    NAMESPACE: Final = uuid.NAMESPACE_OID

    @staticmethod
    def v4() -> str:
        return uuid.uuid4()

    @staticmethod
    def hex() -> str:
        return str(uuid.uuid4().hex)

    @staticmethod
    def v5(identifier: str) -> str:
        my_namespace = uuid.NAMESPACE_OID
        return str(uuid.uuid5(my_namespace, identifier))