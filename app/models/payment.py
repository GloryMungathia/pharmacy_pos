from sqlalchemy import Column, Integer, String, Boolean, Numeric, ForeignKey
from sqlalchemy.orm import relationship

from database import Base


class Payment(Base):
    __tablename__ = "payments"

    id = Column(Integer, primary_key=True, index=True)
    sale_id = Column(Integer, ForeignKey("sales.id"), nullable=False, unique=True)
    payment_method = Column(String, nullable=False)
    payment_status = Column(Boolean, nullable=False, default=False)
    transaction_reference = Column(String, nullable=True)

    sale = relationship("Sale", back_populates="payment")