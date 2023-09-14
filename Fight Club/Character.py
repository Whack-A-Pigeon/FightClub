import mysql.connector

mydb = mysql.connector.connect(
    host = 'localhost',
    username = 'root',
    password = 'root',
    )

mycursor = mydb.cursor()

<<<<<<< HEAD
#mycursor.execute("CREATE DATABASE characters")
mycursor.execute("USE characters")

#Use the following lines for copy paste
#Name VARCHAR(255), Damage INT, Special BOOL, Knockback INT
#(Name, Damage, Special, Knockback) VALUES(%s, %s, %s, %s)"
#('Kick', 125, 0, 0), ('Dodge', 0, 0, 0), ('Pass', 0, 0, 0), ('Recovery', 150, 0, 0),

mycursor.execute("CREATE TABLE All_Might (Name VARCHAR(255), Damage INT, Special BOOL, Knockback INT)")
=======
mycursor.execute("DROP DATABASE IF EXISTS characters")
print("Creating Database...")
mycursor.execute("CREATE DATABASE characters")
mycursor.execute("USE characters")

#Use the following lines for copy paste
#Name VARCHAR(255), Damage INT, Special INT, Knockback INT
#(Name, Damage, Special, Knockback) VALUES(%s, %s, %s, %s)"
#('Kick', 125, 0, 0), ('Dodge', 0, 0, 0), ('Pass', 0, 0, 0), ('Recovery', 150, 0, 0),

mycursor.execute("CREATE TABLE IF NOT EXISTS All_Might (Name VARCHAR(255), Damage INT, Special INT, Knockback INT)")
>>>>>>> 02cba0d (First Version)
All_Might_Insert = "INSERT IGNORE INTO All_Might(Name, Damage, Special, Knockback) VALUES (%s, %s, %s, %s)"
All_Might_Moves = [('Consecutive Punches', 150, 0, 0), ('Kick', 125, 0, 0), ('Dodge', 0, 0, 0), ('Pass', 0, 0, 0), ('Recovery', 150, 0, 0), ('United States of SMASH', 350, 0, 50), ('Texas Smash', 225, 0, 0), ('California Smash', 250, 0, 0)]
mycursor.executemany(All_Might_Insert, All_Might_Moves)
mydb.commit()

<<<<<<< HEAD
mycursor.execute("CREATE TABLE Superman (Name VARCHAR(255), Damage INT, Special BOOL, Knockback INT)")
=======
mycursor.execute("CREATE TABLE IF NOT EXISTS Superman (Name VARCHAR(255), Damage INT, Special INT, Knockback INT)")
>>>>>>> 02cba0d (First Version)
Superman_Insert = "INSERT IGNORE INTO Superman(Name, Damage, Special, Knockback) VALUES (%s, %s, %s, %s)"
Superman_Moves = [('Punches',125,0,0), ('Kick',125,0,0), ('Dodge',0,0,0), ('Pass',0,0,0), ('Recovery',150,0,0), ('Heat Vision',250,0,25), ('Frost Breath',25,1,0), ('Inhuman Punch',350,0,50)]
mycursor.executemany(Superman_Insert, Superman_Moves)
mydb.commit()

<<<<<<< HEAD
mycursor.execute("CREATE TABLE Thor (Name VARCHAR(255), Damage INT, Special BOOL, Knockback INT)")
=======
mycursor.execute("CREATE TABLE IF NOT EXISTS Thor (Name VARCHAR(255), Damage INT, Special INT, Knockback INT)")
>>>>>>> 02cba0d (First Version)
Thor_Insert = "INSERT IGNORE INTO Thor(Name, Damage, Special, Knockback) VALUES(%s, %s, %s, %s)"
Thor_Moves = [('Kick', 125, 0, 0), ('Dodge', 0, 0, 0), ('Pass', 0, 0, 0), ('Recovery', 150, 0, 0), ('Odins Punch', 150, 0, 0), ('Lightning Storm', 250, 0, 0), ('Thors Wrath', 350, 0, 25), ('Mjolnir Punt', 225, 0, 0)]
mycursor.executemany(Thor_Insert, Thor_Moves)
mydb.commit()

<<<<<<< HEAD
mycursor.execute("CREATE TABLE Batman (Name VARCHAR(255), Damage INT, Special BOOL, Knockback INT)")
=======
mycursor.execute("CREATE TABLE IF NOT EXISTS Batman (Name VARCHAR(255), Damage INT, Special INT, Knockback INT)")
>>>>>>> 02cba0d (First Version)
Batman_Insert = "INSERT IGNORE INTO Batman(Name, Damage, Special, Knockback) VALUES(%s, %s, %s, %s)"
Batman_Moves = [('Kick', 90, 0, 0), ('Dodge', 0, 0, 0), ('Pass', 0, 0, 0), ('Recovery', 125, 0, 0), ('Punches', 100, 0, 0), ('HellBat Attack', 400, 0, 75), ('Tactical Evade', 0, 1, 0), ('BatMobiles Might', 225, 0, 0)]
mycursor.executemany(Batman_Insert, Batman_Moves)
mydb.commit()

<<<<<<< HEAD
mycursor.execute("CREATE TABLE Spiderman_2099 (Name VARCHAR(255), Damage INT, Special BOOL, Knockback INT)")
Spiderman_Insert = "INSERT IGNORE INTO Spiderman_2099(Name, Damage, Special, Knockback) VALUES(%s, %s, %s, %s)"
Spiderman_Moves = [('Kick', 125, 0, 0), ('Dodge', 0, 0, 0), ('Pass', 0, 0, 0), ('Recovery', 150, 0, 0), ('Punches', 150, 0, 0), ('Venom Blast', 325, 1, 50), ('Talon Strike', 225, 0, 0), ('Webslinging Strike', 225, 0, 0)]
mycursor.executemany(Spiderman_Insert, Spiderman_Moves)
mydb.commit()

mycursor.execute("CREATE TABLE Rick_Sanchez (Name VARCHAR(255), Damage INT, Special BOOL, Knockback INT)")
Rick_Insert = "INSERT IGNORE INTO Rick_Sanchez(Name, Damage, Special, Knockback) VALUES(%s, %s, %s, %s)"
Rick_Moves = [('Bionic Arm', 125, 0, 0), ('Nutcracker', 130, 0, 0), ('Pass', 0, 0, 0), ('Recovery', 150, 0, 0), ('Dodge', 0, 0, 0), ('Particle Beam', 200, 0, 0), ('Combat Suit', 250, 1, 0), ('Rick The Gunslinger', 200, 0, 0)]
mycursor.executemany(Rick_Insert, Rick_Moves)
mydb.commit()

mycursor.execute("CREATE TABLE Venom (Name VARCHAR(255), Damage INT, Special BOOL, Knockback INT)")
Venom_Insert = "INSERT IGNORE INTO Venom (Name, Damage, Special, Knockback) VALUES(%s, %s, %s, %s)"
Venom_Moves = [('Kick', 125, 0, 0), ('Dodge', 0, 0, 0), ('Pass', 0, 0, 0), ('Regenerate', 150, 0, 0), ('Venomous Punch', 150, 0, 0), ('Venomous SLASH', 250, 1, 0), ('Drill attack', 225, 0, 0), ('Throw Bang', 250, 0, 0)]
mycursor.executemany(Venom_Insert, Venom_Moves)
mydb.commit()

mycursor.execute("CREATE TABLE Jotaro (Name VARCHAR(255), Damage INT, Special BOOL, Knockback INT)")
Jotaro_Insert = "INSERT IGNORE INTO Jotaro(Name, Damage, Special, Knockback) VALUES(%s, %s, %s, %s)"
Jotaro_Moves = [('Kick', 125, 0, 0), ('Run', 0, 0, 0), ('Pass', 0, 0, 0), ('Recovery', 150, 0, 0), ('ORA ORA ORA!', 350, 0, 0), ('Star Platinum: The World', 0, 1, 0), ('Star Finger', 150, 0, 0), ('Uppercut', 200, 0, 0)]
mycursor.executemany(Jotaro_Insert, Jotaro_Moves)
mydb.commit()

mycursor.execute("CREATE TABLE Monkey_D_Luffy (Name VARCHAR(255), Damage INT, Special BOOL, Knockback INT)")
=======
mycursor.execute("CREATE TABLE IF NOT EXISTS Spiderman_2099 (Name VARCHAR(255), Damage INT, Special INT, Knockback INT)")
Spiderman_Insert = "INSERT IGNORE INTO Spiderman_2099(Name, Damage, Special, Knockback) VALUES(%s, %s, %s, %s)"
Spiderman_Moves = [('Kick', 125, 0, 0), ('Dodge', 0, 0, 0), ('Pass', 0, 0, 0), ('Recovery', 150, 0, 0), ('Punches', 150, 0, 0), ('Venom Blast', 325, 0, 50), ('Talon Strike', 225, 0, 0), ('Webslinging Strike', 225, 0, 0)]
#Venom Blast is a special
mycursor.executemany(Spiderman_Insert, Spiderman_Moves)
mydb.commit()

mycursor.execute("CREATE TABLE IF NOT EXISTS Rick_Sanchez (Name VARCHAR(255), Damage INT, Special INT, Knockback INT)")
Rick_Insert = "INSERT IGNORE INTO Rick_Sanchez(Name, Damage, Special, Knockback) VALUES(%s, %s, %s, %s)"
Rick_Moves = [('Bionic Arm', 125, 0, 0), ('Nutcracker', 130, 0, 0), ('Pass', 0, 0, 0), ('Recovery', 150, 0, 0), ('Dodge', 0, 0, 0), ('Particle Beam', 200, 0, 0), ('Combat Suit', 250, 0, 0), ('Rick The Gunslinger', 200, 0, 0)]
#combat suit is a special
mycursor.executemany(Rick_Insert, Rick_Moves)
mydb.commit()

mycursor.execute("CREATE TABLE IF NOT EXISTS Venom (Name VARCHAR(255), Damage INT, Special INT, Knockback INT)")
Venom_Insert = "INSERT IGNORE INTO Venom (Name, Damage, Special, Knockback) VALUES(%s, %s, %s, %s)"
Venom_Moves = [('Kick', 125, 0, 0), ('Dodge', 0, 0, 0), ('Pass', 0, 0, 0), ('Regenerate', 150, 0, 0), ('Venomous Punch', 150, 0, 0), ('Venomous SLASH', 250, 0, 0), ('Drill attack', 225, 0, 0), ('Throw Bang', 250, 0, 0)]
#Vencome slash is a special
mycursor.executemany(Venom_Insert, Venom_Moves)
mydb.commit()

mycursor.execute("CREATE TABLE IF NOT EXISTS Jotaro (Name VARCHAR(255), Damage INT, Special INT, Knockback INT)")
Jotaro_Insert = "INSERT IGNORE INTO Jotaro(Name, Damage, Special, Knockback) VALUES(%s, %s, %s, %s)"
Jotaro_Moves = [('Kick', 125, 0, 0), ('Run', 0, 0, 0), ('Pass', 0, 0, 0), ('Recovery', 150, 0, 0), ('ORA ORA ORA!', 350, 0, 0), ('Star Platinum: The World', 0, 1, 0), ('Star Finger', 175, 0, 0), ('Uppercut', 225, 0, 0)]
mycursor.executemany(Jotaro_Insert, Jotaro_Moves)
mydb.commit()

mycursor.execute("CREATE TABLE IF NOT EXISTS Monkey_D_Luffy (Name VARCHAR(255), Damage INT, Special INT, Knockback INT)")
>>>>>>> 02cba0d (First Version)
Luffy_Insert = "INSERT IGNORE INTO Monkey_D_Luffy(Name, Damage, Special, Knockback) VALUES(%s, %s, %s, %s)"
Luffy_Moves = [('Gommu Gommu No Gattling', 150, 0, 0), ('Gommu Gommu No Spring Bullet', 125, 0, 0), ('Dodge', 0, 0, 0), ('Pass', 0, 0, 0), ('KING KONG GUN', 350, 0, 25), ('Gommu Gommu No Jet Pistol', 225, 0, 0), ('Gommu Gommu No Red Hawk', 225, 0, 0), ('Gommu Gommu No Culverin', 150, 0, 0)]   
mycursor.executemany(Luffy_Insert, Luffy_Moves)
mydb.commit()
              
<<<<<<< HEAD
mycursor.execute("CREATE TABLE Kakashi_Hatake (Name VARCHAR(255), Damage INT, Special BOOL, Knockback INT)")
Kakashi_Insert = "INSERT IGNORE INTO Kakashi_Hatake(Name, Damage, Special, Knockback) VALUES(%s, %s, %s, %s)"              
Kakashi_Moves = [('Substitution Jutsu', 0, 0, 0), ('Pass', 0, 0, 0), ('Recovery', 150, 0, 0), ('Chidori', 350, 0, 50), ('Punch', 150, 0, 0), ('Kick', 0, 0, 0), ('Rasengan', 250, 0, 0), ('Fire Release', 225, 0, 0)]
=======
mycursor.execute("CREATE TABLE IF NOT EXISTS Kakashi_Hatake (Name VARCHAR(255), Damage INT, Special INT, Knockback INT)")
Kakashi_Insert = "INSERT IGNORE INTO Kakashi_Hatake(Name, Damage, Special, Knockback) VALUES(%s, %s, %s, %s)"              
Kakashi_Moves = [('Substitution Jutsu', 0, 0, 0), ('Pass', 0, 0, 0), ('Recovery', 150, 0, 0), ('Chidori', 350, 0, 50), ('Punch', 150, 0, 0), ('Kick', 175, 0, 0), ('Rasengan', 250, 0, 0), ('Fire Release', 225, 0, 0)]
>>>>>>> 02cba0d (First Version)
mycursor.executemany(Kakashi_Insert, Kakashi_Moves)
mydb.commit()              



print("Done")











































