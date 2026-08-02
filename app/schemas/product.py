from datetime import date, datetime
from decimal import Decimal

from pydantic import BaseModel,ConfigDict

class ProductBase(BaseModel):
    product_name: str
    barcode: str
    unit_price: Decimal
    stock_quantity: int = 0
    expiry_date: date | None = None
    requires_prescription: bool = False
    category_id: int | None = None
    supplier_id: int | None = None
    is_active: bool = True


class ProductCreate(ProductBase):
    pass


class ProductUpdate(BaseModel):
    product_name: str | None = None
    barcode: str | None = None
    unit_price: Decimal | None = None
    stock_quantity: int | None = None
    expiry_date: date | None = None
    requires_prescription: bool | None = None
    category_id: int | None = None
    supplier_id: int | None = None
    is_active: bool | None = None


class ProductRead(ProductBase):
    model_config = ConfigDict(from_attributes=True)
    id: int
    created_at: datetime

