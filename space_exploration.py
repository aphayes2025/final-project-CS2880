import sqlite3 # included in standard python distribution
import pandas as pd

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
        print(" d) Exit")
        
        main_menu_input = input("=> ")
        while (main_menu_input != 'a' and main_menu_input != 'A' and
               main_menu_input != 'b' and main_menu_input != 'B' and 
               main_menu_input != 'c' and main_menu_input != 'C' and
               main_menu_input != 'd' and main_menu_input != 'D'):
            main_menu_input = input("=> ")

        if (main_menu_input == 'a' or main_menu_input == 'A'):
            view_data()

        if (main_menu_input == 'b' or main_menu_input == 'B'):
            modify_data()

        if (main_menu_input == 'c' or main_menu_input == 'C'):
            stat_queries()
        
        if (main_menu_input == 'd' or main_menu_input == 'D'):
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
    print("placeholder")

if __name__ == "__main__":
    main()
