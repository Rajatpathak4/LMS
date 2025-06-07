from sqlalchemy import Column, Integer, String, DateTime, func, Boolean
from Database.database import Base 

class LoginUser(Base):
    __tablename__ = "login_user"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String(255), nullable=False, unique=True)
    password = Column(String(255), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    is_deleted = Column(Boolean, default=False, nullable=False)