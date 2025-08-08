from sqlalchemy import BigInteger, String, Column
from .db_base import Base

class User(Base):
    __tablename__ = 'users'
    

    telegram_id = Column(BigInteger, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String)
