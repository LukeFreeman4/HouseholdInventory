# To activate virtual enviornment use 'source env/bin/activate'

from models import (Base, session, Item, engine)
import pandas as pd

def menu():
    while True:
        print('''
                \rINVENTORTY
                \r1.) Add Item
                \r2.) View All Items
                \r3.) Search for Item
                \r4.) exit''')
        user_choice = int(input('What would you like to do? '))
        return user_choice

def view_inventory():
    user_table = pd.read_sql_table(table_name = "items", con=engine)
    print(user_table)

def add_new():
    pass
    # insert data into columns. 
        # Item.inster().values(
            # Id = 'number', --should autoincrement
            # Name = 'item name') -- but assing these to variatbles and ask for user intput. 
    # ask for input on each column
    # should give option to add another of greak so needs to be a loop


def run_app():
    app_running = True
    while app_running:
        menu_choice = menu()
        if menu_choice == 1:
            view_inventory()
            input('press enter to continue')
            # View Inventory
        elif menu_choice == 2:
            pass
            # add new
        elif menu_choice == 3:
            pass
            # data analysis
        elif menu_choice == 4:
            app_running = False
            break
        #limit user choice to the inputs listed for options. 
        

if __name__ == '__main__':
    Base.metadata.create_all(engine)
    run_app()




               



# edit items function
# delete items function
# search function function
# data cleaning -- may not need
# loop that runs the program -- the runn_app should be what I want