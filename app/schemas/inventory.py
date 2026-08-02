from datetime import date, datetime
from pydantic import BaseModel, ConfigDict


class InventoryBase(BaseModel):
    product_id: int
    batch_number: str | None = None
    quantity: int = 0
    expiry_date: date | None = None


class InventoryCreate(InventoryBase):
    pass


class InventoryUpdate(BaseModel):
    batch_number: str | None = None
    quantity: int | None = None
    expiry_date: date | None = None


class InventoryRead(InventoryBase):
    model_config = ConfigDict(from_attributes=True)
    id: int
    received_at: datetime