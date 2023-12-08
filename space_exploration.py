import sqlite3 # included in standard python distribution
import pandas as pd
import matplotlib.pyplot as plt
#connect or create if doesn’t exist (same folder)
con = sqlite3.connect('SpaceExplore.db')

def main():
    keep_playing = True
    while(keep_playing):
        print("Welcome to Space Exploration!")
        print("Choose an option:")
        print(" a) View Data")
        print(" b) Modify Data")
        print(" c) Statistical Queries")
        print(" d) Data visualization")
        print(" e) Exit")
        
        main_menu_input = input("=> ")
        while (main_menu_input != 'a' and main_menu_input != 'A' and
               main_menu_input != 'b' and main_menu_input != 'B' and 
               main_menu_input != 'c' and main_menu_input != 'C' and
               main_menu_input != 'd' and main_menu_input != 'D' and 
               main_menu_input != 'e' and main_menu_input != 'E'):
            main_menu_input = input("=> ")

        if (main_menu_input == 'a' or main_menu_input == 'A'):
            view_data()

        if (main_menu_input == 'b' or main_menu_input == 'B'):
            modify_data()

        if (main_menu_input == 'c' or main_menu_input == 'C'):
            stat_queries()
        if (main_menu_input == 'd' or main_menu_input == 'D'):
            data_viz()
    
        if (main_menu_input == 'e' or main_menu_input == 'E'):
            keep_playing = False
            print("\nHave a good day!")

    con.close()

def view_data():
    con.row_factory = sqlite3.Row
    
    view_data_keep_playing = True
    while view_data_keep_playing:
        print("\nChoose which database to view")
        print("1: Annual Space Visits")
        print("2: Cost of Space Launches")
        print("3: Cumulative Exoplanets Discovered")
        print("4: Cumulative People in Space")
        print("5: Cumulative Space Visits")
        print("6: Largest Impact Craters")
        print("7: Low Earth Orbit Objecets")
        print("8: Nasa Annual Budget")
        print("9: Near Earth Asteroids")
        print("10: Space Objects By Orbit")
        print("11: Objects Launched Into Space")
        print("12: Go Back")
        
        user_info_input = input( "=> ")
        while (user_info_input != '1' and user_info_input != '2' and
               user_info_input != '3' and user_info_input != '4' and
               user_info_input != '5' and user_info_input != '6' and
               user_info_input != '7' and user_info_input != '8' and
               user_info_input != '9' and user_info_input != '10' and
               user_info_input != '11' and user_info_input != '12'):
            user_info_input = input( "=> ")

        if (user_info_input == '1'):
            cur = con.cursor() #back to beginning
            cur.execute("SELECT * FROM annual_space_visits")
            rows = cur.fetchall()
            print("\nEntity, Code, Year, Annual Visits")
            for row in rows:
                print(f"{row['Entity']}, {row['Code']}, {row['Year']}, {row['annual_visits']}")

        elif (user_info_input == '2'):
            cur = con.cursor() #back to beginning
            cur.execute("SELECT * FROM cost_space_launches")
            rows = cur.fetchall()
            print("\nEntity, Year, Cost Per KG, Launch Class")
            for row in rows:
                print(f"{row['Entity']}, {row['Year']}, {row['cost_per_kg']}, {row['launch_class']}")

        elif (user_info_input == '3'):
            cur = con.cursor() #back to beginning
            cur.execute("SELECT * FROM cumulative_exoplanets")
            rows = cur.fetchall()
            print("\nEntity, Year, Cumulative Number of Exoplanets Discovered")
            for row in rows:
                print(f"{row['Entity']}, {row['Year']}, {row['cumulative_number_of_exoplanets_discovered']}")

        elif (user_info_input == '4'):
            cur = con.cursor() #back to beginning
            cur.execute("SELECT * FROM cumulative_people_space")
            rows = cur.fetchall()
            print("\nEntity, Code, Year, Cumulative People")
            for row in rows:
                print(f"{row['Entity']}, {row['Code']}, {row['Year']}, {row['cumulative_individuals']}")
        
        elif (user_info_input == '5'):
            cur = con.cursor() #back to beginning
            cur.execute("SELECT * FROM cumulative_space_visits")
            rows = cur.fetchall()
            print("\nEntity, Code, Year, Cumulative Visits")
            for row in rows:
                print(f"{row['Entity']}, {row['Code']}, {row['Year']}, {row['cumulative_visits']}")
        
        elif (user_info_input == '6'):
            cur = con.cursor() #back to beginning
            cur.execute("SELECT * FROM largest_impact_craters")
            rows = cur.fetchall()
            print("\nEntity, Year, Crater Diameter")
            for row in rows:
                print(f"{row['Entity']}, {row['Year']}, {row['crater_diameter']}")

        elif (user_info_input == '7'):
            cur = con.cursor() #back to beginning
            cur.execute("SELECT * FROM leo_objects")
            rows = cur.fetchall()
            print("\nEntity, Year, Objects in Space")
            for row in rows:
                print(f"{row['Entity']}, {row['Year']}, {row['objects_in_space']}")
        
        elif (user_info_input == '8'):
            cur = con.cursor() #back to beginning
            cur.execute("SELECT * FROM nasa_annual_budget")
            rows = cur.fetchall()
            print("\nEntity, Code, Year, Budget")
            for row in rows:
                print(f"{row['Entity']}, {row['Code']}, {row['Year']}, {row['Budget']}")

        elif (user_info_input == '9'):
            cur = con.cursor() #back to beginning
            cur.execute("SELECT * FROM near_earth_asteroids_over_time")
            rows = cur.fetchall()
            print("\nEntity, Code, Year, Smaller than 140m, Between 140m and 1km, Larger than 1km")
            for row in rows:
                print(f"{row['Entity']}, {row['Code']}, {row['Year']}, {row['smaller_than_140m']}, {row['between_140m_and_1km']}, {row['larger_than_1km']}")

        elif (user_info_input == '10'):
            cur = con.cursor() #back to beginning
            cur.execute("SELECT * FROM space_objects_by_orbit")
            rows = cur.fetchall()
            print("\nEntity, Year, Objects in Space")
            for row in rows:
                print(f"{row['Entity']}, {row['Year']}, {row['objects_in_space']}")

        elif (user_info_input == '11'):
            cur = con.cursor() #back to beginning
            cur.execute("SELECT * FROM objects_launched_in_space")
            rows = cur.fetchall()
            print("\nEntity, Year, Objects Launched")
            for row in rows:
                print(f"{row['Entity']}, {row['Year']}, {row['Objects_Launched']}")

        elif(user_info_input == '12'):
            view_data_keep_playing = False
        
    

def modify_data():
    # setting vars
    conn = sqlite3.connect('SpaceExplore.db')
    cur = conn.cursor()

    # getting the ui 
    print("How would you like to modify the data? 1) Add 2) Remove 3) Modify ")
    ui = str(input("=> "))

    # make sure user is entering the correct 
    while (ui != '1' and ui != '2' and ui != '3'):
        print("Sorry, Incorrect input. Please pick 1,2,3.")
        ui = input( "=> ")

    # add
    if ui == "1":
        # getting the ui
        print("What table would you like to add to?")
        table_choice = str(input("=> "))
        statement = f'''PRAGMA table_info({table_choice});'''
        cur.execute(statement)

        # getting all the columns names
        lst = cur.fetchall()
        column_tuple = tuple(lst)
        column_lst = []
        for i in range(len(lst)):
            column_lst.append(lst[i][1])

        # asking user what values they want to add for 
        column_tuple = tuple(column_lst)
        print(f"Values Required: {column_lst}")
        print("Please enter the values you want for this table with each value separated by a dash")
        print("Ex: Entity-Year-Objects_launched")
        user_values = str(input("=> "))
        lst_values = user_values.split("-")

        values = ""
        comma_stopper = len(lst_values)
        for i in range(len(lst_values)):
            if comma_stopper - 1 != i:
                values += f"'{lst_values[i]}',"
            else:
                values += f"'{lst_values[i]}'"

        insert_statement = f'''INSERT INTO {table_choice} {column_tuple} VALUES ({values});'''
        try:
            cur.execute(insert_statement)
        except sqlite3.OperationalError:
            print("Table does not exist or values inputted incorrectly")
        print("Great Success!")
        print()
        conn.commit()

    elif ui == "2":
       # getting the ui
        print("What table would you like to remove from?")
        table_choice = str(input("=> "))
        statement = f'''PRAGMA table_info({table_choice});'''
        cur.execute(statement)

        # getting all the columns names
        lst = cur.fetchall()
        column_tuple = tuple(lst)
        column_lst = []
        for i in range(len(lst)):
            column_lst.append(lst[i][1])

        # asking user what they want to remove on 
        print(f"Values Required: {column_lst}")
        print("Please enter the values you want for this table with each value separated by a dash")
        print("Ex for objects launched table: Algeria-1985-4")
        user_values = str(input("=> "))
        lst_values = user_values.split("-")

        # converting inputs into a usable delete statement and then executing it
        values = ""
        comma_stopper = len(lst_values)
        try:
            for i in range(len(lst_values)):
                if comma_stopper - 1 != i:
                    values += f"{column_lst[i]}='{lst_values[i]}' AND "
                else:
                    values += f"{column_lst[i]}='{lst_values[i]}'"
        except IndexError:
            print("Incorrect amount of inputs")
        else:
            insert_statement = f'''DELETE FROM {table_choice} WHERE {values};'''        
            try:
                cur.execute(insert_statement)
            except sqlite3.OperationalError:
                print("Table does not exist or values inputted incorrectly")
            else:
                print("Great Success!")
                print()
                conn.commit()

    elif ui == "3":
        # getting the ui
        print("What table would you like to modify?")
        table_choice = str(input("=> "))
        statement = f'''PRAGMA table_info({table_choice});'''
        cur.execute(statement)

        # getting all the columns names
        lst = cur.fetchall()
        column_tuple = tuple(lst)
        column_lst = []
        for i in range(len(lst)):
            column_lst.append(lst[i][1])

        column_tuple = tuple(column_lst)
        print(f"Values Required: {column_lst}")
        print("Please enter the values you want to set for table with each value separated by a dash")
        print("Ex: Entity-Year-Objects_launched")
        user_values = str(input("=> "))
        lst_values = user_values.split("-")
        
        # getting values for the set 
        set_values = ""
        comma_stopper = len(lst_values)
        for i in range(len(lst_values)):
            if comma_stopper - 1 != i:
                set_values += f"{column_lst[i]}='{lst_values[i]}',"
            else:
                set_values += f"{column_lst[i]}='{lst_values[i]}'"

        # getting values for the where condition
        print(f"Values Required: {column_lst}")
        print("Please enter the values you want for the WHERE condition for table with each value separated by a dash")
        print("Ex: Entity-Year-Objects_launched")
        user_values = str(input("=> "))
        lst_values = user_values.split("-")
        where_values = ""
        comma_stopper = len(lst_values)
        for i in range(len(lst_values)):
            if comma_stopper - 1 != i:
                where_values += f"{column_lst[i]}='{lst_values[i]}' AND "
            else:
                where_values += f"{column_lst[i]}='{lst_values[i]}'"

        # insert statement 
        insert_statement = f'''UPDATE {table_choice} SET {set_values} WHERE {where_values};'''
        try:
            cur.execute(insert_statement)
        except sqlite3.OperationalError:
            print("Table does not exist or values inputted incorrectly")
        print("Great Success!")
        print()
        conn.commit() 

    

def stat_queries():
    # setting vars
    conn = sqlite3.connect('SpaceExplore.db')
    cur = conn.cursor()

    # showing all tables
    statement = '''SELECT name FROM sqlite_schema WHERE type='table' ORDER BY name;'''
    cur.execute(statement)
    lst = (cur.fetchall())
    col_lst = []
    print("Tables to Choose from.")
    for i in range(len(lst)):
        col_lst.append(lst[i][0])
        print(lst[i][0])
    
    # finding what table the user wants
    print("What table would you like to make a query on?")
    ui_table =  str(input("=>"))

    # ui validation
    while ui_table not in col_lst:
        print("Not valid option. Options are: ")
        print(col_lst)
        print("What table would you like to make a query on?")
        ui_table =  str(input("=>"))

    # find what column they want to do the query on
    print("What column would you like to make a statistical query?")
    statement = f'''PRAGMA table_info({ui_table});'''
    cur.execute(statement)

    # getting all the columns names
    lst = cur.fetchall()
    column_lst = []

    for i in range(len(lst)):
        print(lst[i][1])
        column_lst.append(lst[i][1])

    # getting user column
    ui_column = str(input("=> "))
    while ui_column not in column_lst:
        print("Not valid option. Options are: ")
        print(column_lst)
        print("What column would you like to make a query on?")
        ui_column = str(input("=>"))

    # finding what statistical query the user wants
    print("What statistical query would you like to make?")
    print("(a) mean, (b) min, (c) max, (d) median, (e) standard dev")
    ui = str(input("=> "))
    uil = ui.lower()
    
    # validating input
    while uil != 'a' and uil != 'b' and uil != 'c' and uil != 'd' and uil != 'e':
        print("Incorrect choice, try again.")
        print("(a) mean, (b) min, (c) max, (d) median, (e) standard dev")
        ui = str(input("=> "))
        uil = ui.lower()

    # calculating mean
    if uil == 'a':
        statement = f'''SELECT AVG({ui_column}) from {ui_table}'''
        cur.execute(statement)
        num = cur.fetchall()[0][0]
        print(f"Mean {ui_column} is {num:.2f}")

    # calculating min
    elif uil == 'b':
        statement = f'''SELECT MIN({ui_column}) from {ui_table}'''
        cur.execute(statement)
        num = cur.fetchall()[0][0]
        print(f"Min {ui_column} is {num:.2f}")

    # calculating max
    elif uil == 'c':
        statement = f'''SELECT MAX({ui_column}) from {ui_table}'''
        cur.execute(statement)
        num = cur.fetchall()[0][0]
        print(f"Max {ui_column} is {num:.2f}")
    
    # calculating median (TODO)
    elif uil == 'd':
        statement = f''''''
    
    # calculating standard dev
    elif uil == 'e':
        statement = f''''''
        
def data_viz():
    # setting vars
    conn = sqlite3.connect('SpaceExplore.db')
    cur = conn.cursor()

    # intro 
    print("We have two options of graphs to show you!")
    print("Would you like to see a graph of the NASA annual budget or Amount of near earth asteroids discovered.")
    print("(1) for NASA annual budget or (2) for near earth asteroids discovered")

    # validating input
    ui = str(input("=> "))
    while ui != '1' and ui != '2':
        print("Incorrect option, try again!")
        ui = str(input("=> "))

    # nasa data viz
    if ui == '1':
        # setting vars
        x_values = []
        y_values = []

        # getting x values
        x_statement = """SELECT year from nasa_annual_budget"""
        cur.execute(x_statement)
        lst = cur.fetchall()
        for i in range(0, len(lst), 10):
            x_values.append(lst[i][0])

        # getting y values
        y_statement = '''SELECT budget from nasa_annual_budget'''
        cur.execute(y_statement)
        lst2 = cur.fetchall()
        for i in range(0, len(lst2), 10):
            num = float(lst2[i][0])
            y_values.append(int(num))
    
        # plotting bar graph
        plt.bar(x_values, y_values)
        plt.xlabel('Years')
        plt.ylabel('Budget (In Billions)')
        plt.title("NASA Annual budget increase")
        plt.ylim(2000000000,23500000000)
        plt.show()

    # asteroids
    else:
        # setting vars
        x_values = []
        y_values_small = []
        y_values_med = []
        y_values_large = []

        # getting x values
        select_statement = '''SELECT YEAR from near_earth_asteroids_over_time'''
        cur.execute(select_statement)
        lst = cur.fetchall()
        for i in range(11, len(lst), 2):
            x_values.append(lst[i][0])

        # getting first line
        select_statement = '''SELECT smaller_than_140m from near_earth_asteroids_over_time'''
        cur.execute(select_statement)
        lst2 = cur.fetchall()
        for i in range(11, len(lst2), 2):
            num = int(lst2[i][0])
            y_values_small.append(num)

        # getting second line
        select_statement = '''SELECT between_140m_and_1km from near_earth_asteroids_over_time'''
        cur.execute(select_statement)
        lst2 = cur.fetchall()
        for i in range(11, len(lst2), 2):
            num = int(lst2[i][0])
            y_values_med.append(num)

        # getting third line
        select_statement = '''SELECT larger_than_1km from near_earth_asteroids_over_time'''
        cur.execute(select_statement)
        lst2 = cur.fetchall()
        for i in range(11, len(lst2), 2):
            num = int(lst2[i][0])
            y_values_large.append(num)

        # line graoh
        plt.plot(x_values, y_values_small , label="small")
        plt.plot(x_values, y_values_med, label="Medium")
        plt.plot(x_values, y_values_large, label="Large")
        plt.legend(loc="upper left")
        plt.xlabel('Years')
        plt.ylabel('Amount of asteroids')
        plt.title("Near Earth Asteroids discovered (by size) ")
        plt.show()

if __name__ == "__main__":
    main()
