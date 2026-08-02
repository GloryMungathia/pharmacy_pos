from datetime import datetime
from pydantic import BaseModel, ConfigDict


class ReceiptBase(BaseModel):
    sale_id: int
    receipt_number: str
    is_voided: bool = False


class ReceiptCreate(ReceiptBase):
    pass


class ReceiptUpdate(BaseModel):
    is_voided: bool | None = None


class ReceiptRead(ReceiptBase):
    model_config = ConfigDict(from_attributes=True)
    id: int
    issued_at: datetime