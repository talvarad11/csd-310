#Tim Alvarado Assignment 8.3
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

cursor.execute("SELECT team_id, team_name, mascot FROM pysports.team")

teams = cursor.fetchall()

print("-- DISPLAYING TEAM RECORDS --")

for team in teams:
    print("\nTeam ID: {}".format(team[0]), "\nTeam Name: {}".format(team[1]), "\nMascot: {}".format(team[2]))

print("")
print("")

#player records

cursor = db.cursor()

cursor.execute("SELECT player_id, first_name, last_name, team_id FROM pysports.player")

players = cursor.fetchall()


print("-- DISPLAYING PLAYER RECORDS --")

for player in players:
    print("\nPlayer ID: {}".format(player[0]), "\nFirst Name: {}".format(player[1]), "\nLast Name: {}".format(player[2]), "\nTeam ID: {}".format(player[3])) 
    
    db.close()
print("")
print("")
print("")

print("Press any key to continue...")
    