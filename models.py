from sqlalchemy import (create_engine, Column, Integer, String, DATE)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///Inventory.db', echo = False)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

class Item(Base):
    __tablename__ = 'items'

    id = Column(Integer, primary_key = True)
    name = Column('Name', String)
    date_purchased = Column('Date Purchased', DATE)
    date_expires = Column('Date Expires', DATE)
    item_quantity = Column('Quantity', Integer)
    item_price = Column('Price', Integer)
    item_location = Column('Location', String)

    def __repr__(self):
        return f'Name: {self.name} Date Purchased: {self.date_purchased} Date Expires: {self.date_expires} Quantity: {self.item_quantity} Price: {self.item_price} Location: {self.item_location}'

# create a database
# inventory.db, locations.db, 
# create a model 1
    # Item, Expiry Date, Cost, Location
