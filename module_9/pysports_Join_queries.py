#Tim Alvarardo
#Assignment 9.2 - Basic Table Joins
#7/8/2022

import mysql.connector

config = {
    "user": "pysports_user",
    "password": "M@stiff11",
    "host": "127.0.0.1",
    "database": "pysports",
    "raise_on_warnings": True
}
# connecting to database
db = mysql.connector.connect(**config)

#team records

cursor = db.cursor()

cursor.execute("SELECT player_id, first_name, last_name, team_name FROM pysports.player Inner Join pysports.team ON player.team_id = team.team_id")

players = cursor.fetchall()

print("-- DISPLAYING PLAYER RECORDS --")

for player in players:
    print("\nPlayer ID: {}".format(player[0]), "\nFirst Name: {}".format(player[1]), "\nLast Name: {}".format(player[2]), "\nTeam Name: {}".format(player[3])) 
    

print()
print()

print("Press any key to continue...")