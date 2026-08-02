from pydantic import BaseModel, ConfigDict


class PaymentBase(BaseModel):
    sale_id: int
    payment_method: str
    payment_status: bool = False
    transaction_reference: str | None = None


class PaymentCreate(PaymentBase):
    pass


class PaymentUpdate(BaseModel):
    payment_method: str | None = None
    payment_status: bool | None = None
    transaction_reference: str | None = None


class PaymentRead(PaymentBase):
    model_config = ConfigDict(from_attributes=True)
    id: int