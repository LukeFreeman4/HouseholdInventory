from sqlalchemy import (create_engine, Column, Integer, String, DATE, MetaData, DATETIME)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import pandas as pd
from datetime import datetime


engine = create_engine('sqlite:///Inventory.db', echo = False)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

class Item(Base):
    __tablename__ = 'items'

    id = Column(Integer, primary_key = True)
    name = Column('Name', String, nullable = False)
    date_purchased = Column('Date Purchased', DATE, nullable = False)
    date_expires = Column('Date Expires', DATE)
    item_quantity = Column('Quantity', Integer, nullable = False)
    item_price = Column('Price', Integer, nullable = False)
    item_location = Column('Location', String, nullable = False)
    

    def __repr__(self):
        return f'Name: {self.name} Date Purchased: {self.date_purchased} Date Expires: {self.date_expires} Quantity: {self.item_quantity} Price: {self.item_price} Location: {self.item_location}'


# create a database
# inventory.db, locations.db, 
# create a model 1
    # Item, Expiry Date, Cost, Location
