from models.inventory import Inventory
from sqlalchemy.orm import Session


class InventoryRepository:

    def __init__(self):
        self.model = Inventory

    def get(self, db: Session, id: int):
        return db.get(Inventory, id)

    def get_all(self, db: Session):
        return db.query(Inventory).all()

    def create(self, db: Session, data: dict):
        inventory = Inventory(**data)
        db.add(inventory)
        db.commit()
        db.refresh(inventory)
        return inventory

    def update(self, db: Session, db_obj: Inventory, data: dict):
        for field, value in data.items():
            setattr(db_obj, field, value)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def delete(self, db: Session, db_obj: Inventory):
        db.delete(db_obj)
        db.commit()


inventory_repository = InventoryRepository()