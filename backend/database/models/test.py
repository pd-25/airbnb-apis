from database.base_class import Base
from sqlalchemy import Column, Integer, String
class Test(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String, nullable=False)