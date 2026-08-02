from decimal import Decimal
from pydantic import BaseModel, ConfigDict


class SaleItemBase(BaseModel):
    sale_id: int
    product_id: int
    quantity_sold: int
    unit_price_at_sale: Decimal
    sub_total: Decimal


class SaleItemCreate(SaleItemBase):
    pass


class SaleItemUpdate(BaseModel):
    quantity_sold: int | None = None
    unit_price_at_sale: Decimal | None = None
    sub_total: Decimal | None = None


class SaleItemRead(SaleItemBase):
    model_config = ConfigDict(from_attributes=True)
    id: int