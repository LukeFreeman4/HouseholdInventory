# import models
from models import (Base, session, Item, engine)

if __name__ == '__main__':
    Base.metadata.create_all(engine)


# main menu - add, search, analysis, exit and view
# functions add item to database
# edit items
# delete items
# search function
# data cleaning
# loop that runs the program