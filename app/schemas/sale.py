from datetime import datetime
from decimal import Decimal

from pydantic import BaseModel, ConfigDict


class SaleBase(BaseModel):
    customer_id: int | None = None
    user_id: int
    total_amount: Decimal
    tax_amount: Decimal = 0
    discount_applied: Decimal = 0


class SaleCreate(SaleBase):
    pass


class SaleUpdate(BaseModel):
    customer_id: int | None = None
    user_id: int | None = None
    total_amount: Decimal | None = None
    tax_amount: Decimal | None = None
    discount_applied: Decimal | None = None


class SaleRead(SaleBase):
    model_config = ConfigDict(from_attributes=True)
    id: int
    sale_date_time: datetime