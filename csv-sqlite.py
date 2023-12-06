import sqlite3 # included in standard python distribution
import csv
# test commit

#connect or create if doesn’t exist (same folder)
con = sqlite3.connect('SpaceExplore.db')

#create database cursor - enables traversal of records in db
cur = con.cursor()

cur.execute("DROP TABLE IF EXISTS annual_space_visits;")
cur.execute("DROP TABLE IF EXISTS cost_space_launches;")
cur.execute("DROP TABLE IF EXISTS cumulative_exoplanets;")
cur.execute("DROP TABLE IF EXISTS cumulative_gravitational_wave;")
cur.execute("DROP TABLE IF EXISTS cumulative_objects_in_space;")
cur.execute("DROP TABLE IF EXISTS cumulative_people_space;")
cur.execute("DROP TABLE IF EXISTS cumulative_space_visits;")
cur.execute("DROP TABLE IF EXISTS largest_impact_craters;")
cur.execute("DROP TABLE IF EXISTS leo_objects;")
cur.execute("DROP TABLE IF EXISTS nasa_annual_budget;")
cur.execute("DROP TABLE IF EXISTS near_earth_asteroids_over_time;")
cur.execute("DROP TABLE IF EXISTS space_objects_by_orbit;")
cur.execute("DROP TABLE IF EXISTS objects_launched_in_space;")

#create a table for our Annual_Space_Visits
create_table = '''CREATE TABLE annual_space_visits('Entity', 'Code', 'Year', 'Annual_Visits')'''

cur.execute(create_table)
con.commit()

file = open('annual-space-visits.csv')
contents = csv.reader(file)

users_headers = print(next(contents))

insert_records = '''INSERT INTO annual_space_visits('Entity', 'Code', 'Year', 'Annual_Visits')
                    VALUES(?,?,?,?)'''

cur.executemany(insert_records, contents)

con.commit()
file.close()


#create a table for our Cost_Space_Launches
create_table = '''CREATE TABLE cost_space_launches('Entity', 'Code', 'Year', 'cost_per_kg', 'launch_class')'''


cur.execute(create_table)
con.commit()

file = open('cost-space-launches-low-earth-orbit.csv')
contents = csv.reader(file)

users_headers = print(next(contents))

insert_records = '''INSERT INTO cost_space_launches('Entity', 'Code', 'Year', 'cost_per_kg', 'launch_class')
                    VALUES(?,?,?,?,?)'''

cur.executemany(insert_records, contents)
drop_column = '''ALTER TABLE cost_space_launches DROP Code;'''
cur.execute(drop_column)

con.commit()
file.close()

#create a table for our Cumulative_Exoplanets
create_table = '''CREATE TABLE cumulative_exoplanets('Entity', 'Code', 'Year', 'cumulative_number_of_exoplanets_discovered')'''

cur.execute(create_table)
con.commit()

file = open('cumulative-exoplanets-by-method.csv')
contents = csv.reader(file)

users_headers = print(next(contents))

insert_records = '''INSERT INTO cumulative_exoplanets('Entity', 'Code', 'Year', 'cumulative_number_of_exoplanets_discovered')
                    VALUES(?,?,?,?)'''

cur.executemany(insert_records, contents)
drop_column = '''ALTER TABLE cumulative_exoplanets DROP Code;'''
cur.execute(drop_column)

con.commit()
file.close()


#create a table for our Cumulative_People_Space
create_table = '''CREATE TABLE cumulative_people_space('Entity', 'Code', 'Year', 'cumulative_individuals')'''

cur.execute(create_table)
con.commit()

file = open('cumulative-people-space.csv')
contents = csv.reader(file)

users_headers = print(next(contents))

insert_records = '''INSERT INTO cumulative_people_space('Entity', 'Code', 'Year', 'cumulative_individuals')
                    VALUES(?,?,?,?)'''

cur.executemany(insert_records, contents)

con.commit()
file.close()

#create a table for our Cumulative_Space_Visits
create_table = '''CREATE TABLE cumulative_space_visits('Entity', 'Code', 'Year', 'cumulative_visits')'''

cur.execute(create_table)
con.commit()

file = open('cumulative-space-visits.csv')
contents = csv.reader(file)

users_headers = print(next(contents))

insert_records = '''INSERT INTO cumulative_space_visits('Entity', 'Code', 'Year', 'cumulative_visits')
                    VALUES(?,?,?,?)'''

cur.executemany(insert_records, contents)

con.commit()
file.close()

#create a table for our Largest_Impact_Craters
create_table = '''CREATE TABLE largest_impact_craters('Entity', 'Code', 'Year', 'crater_diameter')'''

cur.execute(create_table)
con.commit()

file = open('largest-impact-craters.csv')
contents = csv.reader(file)

users_headers = print(next(contents))

insert_records = '''INSERT INTO largest_impact_craters('Entity', 'Code', 'Year', 'crater_diameter')
                    VALUES(?,?,?,?)'''

cur.executemany(insert_records, contents)
drop_column = '''ALTER TABLE largest_impact_craters DROP Code;'''
cur.execute(drop_column)


con.commit()
file.close()

#create a table for our Leo_Objects
create_table = '''CREATE TABLE leo_objects('Entity', 'Code', 'Year', 'objects_in_space')'''

cur.execute(create_table)
con.commit()

file = open('low-earth-orbits-objects.csv')
contents = csv.reader(file)

users_headers = print(next(contents))

insert_records = '''INSERT INTO leo_objects('Entity', 'Code', 'Year', 'objects_in_space')
                    VALUES(?,?,?,?)'''

cur.executemany(insert_records, contents)
drop_column = '''ALTER TABLE leo_objects DROP Code;'''
cur.execute(drop_column)


con.commit()
file.close()

#create a table for our Nasa_Annual_Budget
create_table = '''CREATE TABLE nasa_annual_budget('Entity', 'Code', 'Year', 'Budget')'''

cur.execute(create_table)
con.commit()

file = open('nasa-annual-budget.csv')
contents = csv.reader(file)

users_headers = print(next(contents))

insert_records = '''INSERT INTO nasa_annual_budget('Entity', 'Code', 'Year', 'Budget')
                    VALUES(?,?,?,?)'''

cur.executemany(insert_records, contents)

con.commit()
file.close()

#create a table for our Near_Earth_Asteroids_Over_Time
create_table = '''CREATE TABLE near_earth_asteroids_over_time('Entity', 'Code', 'Year', 'smaller_than_140m', 'between_140m_and_1km', 'larger_than_1km')'''

cur.execute(create_table)
con.commit()

file = open('near-earth-asteroids-discovered-over-time.csv')
contents = csv.reader(file)

users_headers = print(next(contents))

insert_records = '''INSERT INTO near_earth_asteroids_over_time('Entity', 'Code', 'Year', 'smaller_than_140m', 'between_140m_and_1km', 'larger_than_1km')
                    VALUES(?,?,?,?,?,?)'''

cur.executemany(insert_records, contents)

con.commit()
file.close()

#create a table for our Space_Objects_By_Orbit
create_table = '''CREATE TABLE space_objects_by_orbit('Entity', 'Code', 'Year', 'objects_in_space')'''

cur.execute(create_table)
con.commit()

file = open('space-objects-by-orbit.csv')
contents = csv.reader(file)

users_headers = print(next(contents))

insert_records = '''INSERT INTO space_objects_by_orbit('Entity', 'Code', 'Year', 'objects_in_space')
                    VALUES(?,?,?,?)'''

cur.executemany(insert_records, contents)
drop_column = '''ALTER TABLE space_objects_by_orbit DROP Code;'''
cur.execute(drop_column)


con.commit()
file.close()

#create a table for our Objects_Launched_In_Space
create_table = '''CREATE TABLE objects_launched_in_space('Entity', 'Code', 'Year', 'Objects_Launched')'''

cur.execute(create_table)
con.commit()

file = open('yearly-number-of-objects-launched-into-outer-space.csv')
contents = csv.reader(file)

users_headers = print(next(contents))

insert_records = '''INSERT INTO objects_launched_in_space('Entity', 'Code', 'Year', 'Objects_Launched')
                    VALUES(?,?,?,?)'''

cur.executemany(insert_records, contents)
drop_column = '''ALTER TABLE objects_launched_in_space DROP Code;'''
cur.execute(drop_column)


con.commit()
file.close()
con.close()



