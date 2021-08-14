from time import sleep
import random
import mysql.connector


mydb = mysql.connector.connect(
    host = 'localhost',
    username = 'root',
    password = 'root',
    database = 'characters'
    )

print(mydb)
mycursor = mydb.cursor()

#Clearing screen
def cls():
    print("Loading", end = ' ')
    for i in range(0,3):
            sleep(1)
            print(".", end = ' ')

    print("\n")
    print("="*71)

#Battle Part of the game - (2)
def Battle(user_character, random_character):
    print("YOUR BATTLE SHALL BE AGAINST THE FEARED:", str(random_character).capitalize())
    sleep(3)
    print("Here is the List of the Attacks Your Character Performs:")
    print("-" * 90)
    print("Name\t\tDAMAGE\t\tKnockback")
    show_attacks = "SELECT * FROM " + str(user_character)
    mycursor.execute(show_attacks)
    list_of_moves = [list(item) for item in mycursor.fetchall()]
    for i in list_of_moves:
        for j in i:
            print(j)
    
    

#Playing the Game - (1)
def Gameplay():
    cls()

    print("\n\nHello Contestant, Welcome to The Fight Club! May I know your name?")
    username = input("Enter your Name:")
    print("Nice Name, Pleased to meet you", username)
    print("I am sure you read the instructions when you came here, If you havent, Here is the brief:")
    sleep(2)
    print("You will be given a character to choose from, and that character will contain a set of 8 Moves.")
    sleep(2)
    print("You will be going against another character")
    sleep(2)
    print("You have to number these moves from 1 to 8.")
    sleep(2)
    print("And the game starts by the Host picking a number,")
    sleep(2)
    print("which will decide which move your character will be using for round 1 and the rest of the rounds")
    sleep(2)
    print("against the other player")
    
    while True:
        print("\nPick your Champion!!\n")
        sleep(1)
        mycursor.execute("SHOW TABLES")
        show_character = [item[0] for item in mycursor.fetchall()]
        j = 1
        for i in show_character:
             print(j,".", str(i).capitalize())
             j = j+1
        pick_character = int(input("Enter your choice:"))
        sleep(2)
        random_character_pick = random.randint(0, 9)
        if pick_character > 10 or pick_character <= 0:
            print("Invalid Choice Bucko, Cant do that")
            continue
        break

    user_character = show_character[pick_character - 1] #This allows for making a Dictionary out of the given table. This is a user character and we need a random character too
    random_character = show_character[random_character_pick]
    
    cls()
    print("YOU CHOSE:", str(user_character).upper(), "!!")
    #REPLACE THIS WITH A QUOTE FOR THE CHARACTER

    Battle(user_character, random_character)

    
    
    
    
#Main Menu of the Game
def Main_Menu():
    print("\n\t\tWELCOME TO FIGHT CLUB")
    print("\n\t\t\tMAIN MENU")
    print("-"*90)
    print("1. Play the Game\n2. List of Characters\n3. How to Play\n4. Exit")
    print("-"*90)
    menu_choice = int(input("Enter your choice:"))
    if menu_choice == 1:
        Gameplay()
    elif menu_choice == 2:
        List_Characters()
    elif menu_choice == 3:
        Instructions()
    elif menu_choice == 4:
        Exit()
    else:
        print("Invalid Choice. How did you mess up picking between 4 numbers?")
        try_again = input("Wish to Try again? Press and Enter 'Y' for Yes and 'N' for No:")
        if try_again in 'Yy':
            Main_Menu()
        elif try_again in 'Nn':
            Exit()
        else:
            print("Failed again? How many Chances Should I provide? You should Honestly Just quit and try again or reflect on life choices")
            
    
































    
Main_Menu()                 
