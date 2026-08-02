from repositories.inventory_repository import inventory_repository
from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from schemas.inventory import InventoryCreate, InventoryUpdate


def get_inventory(db: Session, id: int):
    inventory = inventory_repository.get(db, id)
    if not inventory:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Inventory not Found")
    return inventory


def list_inventory(db: Session):
    return inventory_repository.get_all(db)


def create_inventory(db: Session, data: InventoryCreate):
    return inventory_repository.create(db, data.model_dump())


def update_inventory(db: Session, inventory_id: int, data: InventoryUpdate):
    inventory = get_inventory(db, inventory_id)
    return inventory_repository.update(db, inventory, data.model_dump(exclude_unset=True))


def delete_inventory(db: Session, inventory_id: int):
    inventory = get_inventory(db, inventory_id)
    inventory_repository.delete(db, inventory)