from datetime import datetime

from pydantic import BaseModel, ConfigDict


class SupplierBase(BaseModel):
    company_name: str
    contact_name: str | None = None
    phone_number: str
    email: str | None = None
    physical_address: str | None = None


class SupplierCreate(SupplierBase):
    pass


class SupplierUpdate(BaseModel):
    company_name: str | None = None
    contact_name: str | None = None
    phone_number: str | None = None
    email: str | None = None
    physical_address: str | None = None


class SupplierRead(SupplierBase):
    model_config = ConfigDict(from_attributes=True)
    id: int
    created_at: datetime