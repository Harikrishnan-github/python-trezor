# Automatically generated by pb2py
from .. import protobuf as p


class StellarMessageSignature(p.MessageType):
    MESSAGE_WIRE_TYPE = 205
    FIELDS = {
        1: ('public_key', p.BytesType, 0),
        2: ('signature', p.BytesType, 0),
    }

    def __init__(
        self,
        public_key: bytes = None,
        signature: bytes = None
    ) -> None:
        self.public_key = public_key
        self.signature = signature
