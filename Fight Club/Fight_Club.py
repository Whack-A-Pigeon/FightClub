import Character
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


#Battle Part of the game - (3)
def Battle_2(user_moves, random_moves, user_character, random_character, username): #ADD SPECIAL TOO
    def Special(user_tuple, random_tuple, i, user_health, random_health, user_character, random_character, user_moves, random_moves):
        count = 0
        user_special_check = random_special_check = bat_count = 0
        while True:
            """if count > 0:
                user_tuple = user_moves.get(i)
                random_tuple = random_moves.get(i)

            if count == 0:
                bs_check = len(user_tuple[0])
                if bs_check <= 8:
                    print(user_tuple[0], end = "\t\t\t\t\t")
                else:
                    if bs_check > 8 and bs_check <= 16:
                        print(user_tuple[0], end = "\t\t\t\t")
                    if bs_check > 16:
                        print(user_tuple[0], end = "\t\t\t")   
                print(random_tuple[0])"""

            #Jotaro Special
            if user_tuple[0] in "Star Platinum: The World" or random_tuple[0] in "Star Platinum: The World":
                if user_tuple[0] in "Star Platinum: The World":
                    bat_count += 1
                    if bat_count == 2:
                        return i, user_health, random_health
                    else:
                        if random_tuple[2] == 0 or random_special_check != 0:
                            print("ZA WARUDOO!")
                            print("-"*90)
                            sleep(2)
                            if random_tuple[0] in "Recovery Regenerate":
                                random_health += random_tuple[1]
                                print(str(random_character).capitalize(), "Has regenerated. Lets see if its enough to survive whats coming")
                            elif random_tuple[1] > 0:
                                user_health -= random_tuple[1]
                                print("Jotaro may Have stopped time, But he definitely incurred damage from", str(random_character).capitalize(), "attack")
                            sleep(2)
                            seconds = 1
                            count_check = i + 3
                        
                            while i < count_check:
                                if i == 8 or i > 7:
                                    return i, user_health, random_health
                                else:
                                    print('-' * 90)
                                    print("Round:", i + 1)
                                    print('-' * 90)
                                    print(seconds, "seconds have passed...")
                                    sleep(2)
                                    seconds += 4
                                    user_tuple = user_moves.get(i + 1)
                                    if user_tuple[0] in "Recovery":
                                        user_health += user_tuple[1]
                                    elif user_tuple[1] > 0:
                                        random_health -= user_tuple[1] - 50
                                    else:
                                        random_health -= user_tuple[1]

                                    print(user_tuple[0])
                                    print("Damage:", user_tuple[1])
                                    sleep(2)
                                    print("Health:", user_health, "\t\t\t\t", "Health:", random_health)
                                    input("Press Enter to continue")
                                    
                                if i == count_check - 1:
                                    print("Time will start running again...")
                                    sleep(2)
                                    i += 1
                                    return i, user_health, random_health
                                
                                i += 1
                                
                if random_tuple[0] in "Star Platinum: The World":
                    bat_count += 1
                    if bat_count == 2:
                        return i, user_health, random_health
                    else:
                        if user_tuple[2] == 0 or user_special_check != 0:
                            print("ZA WARUDOO!")
                            print("-"*90)
                            sleep(2)
                            if user_tuple[0] in "Recovery Regenerate":
                                user_health += user_tuple[1]
                                print(str(user_character).capitalize(), "Has regenerated. Lets see if its enough to survive whats coming")
                            else:
                                random_health -= user_tuple[1]
                                print("Jotaro may Have stopped time, But he definitely incurred damage from", str(user_character).capitalize(), "attack")
                            sleep(2)
                            seconds = 1
                            count_check = i + 3
                        
                            while i < count_check:
                                if i == 8 or i > 7:
                                    print("Oh it seems Jotaro isnt able to follow through with his Special Attack fully")
                                    return i, user_health, random_health
                                else:
                                    print('-' * 90)
                                    print("Round:", i + 1)
                                    print('-' * 90)
                                    print(seconds, "seconds have passed...")
                                    sleep(2)
                                    seconds += 4
                                    random_tuple = random_moves.get(i + 1)
                                    if random_tuple[0] in "Recovery":
                                        random_health += random_tuple[1]
                                    elif random_tuple[1] > 0:
                                        user_health -= random_tuple[1] - 50
                                    else:
                                        user_health -= random_tuple[1]
                        
                                    print(random_tuple[0])
                                    print("\t\t\t\tDamage:", random_tuple[1])
                                    sleep(2)
                                    print("Health:", user_health, "\t\t\t\t", "Health:", random_health)
                                    input("Press Enter to continue")
                                    
                                if i == count_check - 1:
                                    print("Time will start running again...")
                                    sleep(2)
                                    i += 1
                                    return i, user_health, random_health
                                i += 1    
                        
                        
                            
                    
            #Superman Special
            if user_tuple[0] in "Frost Breath" or random_tuple[0] in "Frost Breath":
                if bat_count != 0:
                    return i, user_health, random_health
                if user_tuple[0] in "Frost Breath":
                    user_special_check += 1

                    if random_tuple[2] == 0 or user_special_check > 1:
                        if random_special_check == 0:
                            if random_tuple[0] in "Recovery Regenerate":
                                random_health += random_tuple[1] - user_tuple[1]
                            elif user_tuple[1] > random_tuple[1]:
                               random_health -= user_tuple[1] - random_tuple[1]
                            else:
                               user_health -= random_tuple[1] - user_tuple[1]

                        
                            
                        
                        sleep(2)
                    
                        #print("DAMAGE:", user_tuple[1], "\t\t\t\t", "DAMAGE:", random_tuple[1])-----> Not needed I think
                        print("Well Well Well, It seems Superman managed to Freeze", str(random_character).capitalize(), "\nThey wont be able to move to react the next attack!")
                        i += 1 #If there is a special attack from opponent after i + 1, the function will not enter this place again.
                        if i > 8:
                            return i, user_health, random_health
                        user_tuple = user_moves.get(i)
                        random_tuple = random_moves.get(i)
                        input("Press Enter to continue")
                        print('-' * 90)
                        print("Round:", i)
                        print('-' * 90)
                        bs_check = len(user_tuple[0])
                        if bs_check <= 8:
                            print(user_tuple[0], end = "\t\t\t\t\t")
                        else:
                            if bs_check > 8 and bs_check <= 16:
                                print(user_tuple[0], end = "\t\t\t\t")
                            if bs_check > 16:
                                print(user_tuple[0], end = "\t\t\t")
                        print(random_tuple[0])

                        sleep(1)
                        print("DAMAGE:", user_tuple[1], "\t\t\t\t", "DAMAGE:", random_tuple[1])
                        random_health -= user_tuple[1]
                        sleep(2)
                        if user_tuple[1] == 0:
                            print("Ohohohoho, Superman Decides not to attack! This could prove fatal later on")
                        else:
                            print(str(random_character).capitalize(), "Will be taking the full extent of that attack due to the Freeze Breath")
                        return i, user_health, random_health

                    
                        
                
                if random_tuple[0] in "Frost Breath":
                    random_special_check += 1
                    
                    if user_tuple[2] == 0 or random_special_check > 1:
                        if user_special_check == 0:
                            if random_tuple[0] in "Recovery Regenerate":
                                user_health += user_tuple[1] - random_tuple[1]
                            if user_tuple[1] > random_tuple[1]:
                                random_health -= user_tuple[1] - random_tuple[1]
                            else:
                                user_health -= random_tuple[1] - user_tuple[1]

                        
                            
                        
                        sleep(2)
                    
                        #print("DAMAGE:", user_tuple[1], "\t\t\t\t", "DAMAGE:", random_tuple[1])
                        print("Well Well Well, It seems Superman managed to Freeze", str(user_character).capitalize(), "\nThey wont be able to move to react the next attack!")
                        i += 1 #If there is a special attack from opponent after i + 1, the function will not enter this place again.
                        if i > 8:
                            return i, user_health, random_health
                        user_tuple = user_moves.get(i)
                        random_tuple = random_moves.get(i)
                        input("Press Enter to continue")
                        print('-' * 90)
                        print("Round:", i)
                        print('-' * 90)
                        bs_check = len(user_tuple[0])
                        if bs_check <= 8:
                            print(user_tuple[0], end = "\t\t\t\t\t")
                        else:
                            if bs_check > 8 and bs_check <= 16:
                                print(user_tuple[0], end = "\t\t\t\t")
                            if bs_check > 16:
                                print(user_tuple[0], end = "\t\t\t")
                        print(random_tuple[0])

                        sleep(1)
                        print("DAMAGE:", user_tuple[1], "\t\t\t\t", "DAMAGE:", random_tuple[1])
                        user_health -= random_tuple[1]
                        sleep(2)
                        if random_tuple[1] == 0:
                            print("Ohohohoho, Superman Decides not to attack! This could prove fatal later on")
                        else:
                            print(str(user_character).capitalize(), "Will be taking the full extent of that attack due to the Freeze Breath")
                        return i, user_health, random_health
                            #SUPERMAN SPECIAL ENDS HERE
                    
                        
                    

        

            #Batman Special
            if user_tuple[0] in "Tactical Evade" or random_tuple[0] in "Tactical Evade":
                if user_tuple[0] in "Tactical Evade":
                    user_special_check += 1
                    bat_count += 1
                    sleep(2)
                    print(str(user_character).capitalize(), "has managed to Evade", str(random_character).capitalize(), "attack! \nBatman is always prepped for a fight after all")
                    if random_tuple[2] == 0:
                        return i, user_health, random_health
                    
                        
                if random_tuple[0] in "Tactical Evade":
                    random_special_check += 1
                    bat_count += 1
                    sleep(2)
                    print(str(random_character).capitalize(), "has managed to Evade", str(user_character).capitalize(), "attack! \nBatman is always prepped for a fight after all")
                    if random_tuple[2] == 0:
                        return i, user_health, random_health
                    
                            
            
            count += 1
                
                

                                
                    
            
                
            
    random_list = [0, 1, 2, 3, 4, 5, 6, 7]
    sleep(1)
    print("\nNow that the Moves Have Decided, Lets commence The BATTLE!!!\nBut Before we start, Remember the First rule of the Fight Club")
    sleep(2)
    print("NEVER TALK ABOUT FIGHT CLUB!")
    sleep(2)
    user_health = random_health = 1000
    random.shuffle(random_list)
    cls()
    print(str(user_character).capitalize(), "\t\t\t\t\t", str(random_character).capitalize())
    i = 1
    
    while i < 9:

        regenerate_check = 0 #increases if damage is more than regeneration.
        print("Health:", user_health, "\t\t\t\t", "Health:", random_health)
        input("Press Enter to continue")
        print('-' * 90)
        print("Round:", i)
        print('-' * 90)
        user_tuple = user_moves.get(i)
        random_tuple = random_moves.get(i)
        

        bs_check = len(user_tuple[0])
        if bs_check <= 8:
            print(user_tuple[0], end = "\t\t\t\t\t")
        else:
            if bs_check > 8 and bs_check <= 16:
                print(user_tuple[0], end = "\t\t\t\t")
            if bs_check > 16:
                print(user_tuple[0], end = "\t\t\t")   
        print(random_tuple[0])
        print("DAMAGE:", user_tuple[1], "\t\t\t\t", "DAMAGE:", random_tuple[1])
        sleep(2)

        #User defined functions usage for special moves
        if user_tuple[2] != 0 or random_tuple[2] != 0:
           i, user_health, random_health = Special(user_tuple, random_tuple, i, user_health, random_health, user_character, random_character, user_moves, random_moves)
           i += 1
           continue
        
        else:
            user_damage = user_tuple[1] - random_tuple[1]
            random_damage = random_tuple[1] - user_tuple[1]
        
        uncommon_moves = "Recovery Regenerate Dodge Substitution Jutsu Run Pass"
        

        #print(user_damage, random_damage)    
        if user_tuple[0] in uncommon_moves or random_tuple[0] in uncommon_moves or user_tuple[1] >= 300 or random_tuple[1] >= 300:
            if user_tuple[0] in 'Recovery Regenerate' or random_tuple[0] in "Recovery Regenerate":
                if user_tuple[0] in 'Recovery Regenerate' and random_tuple[0] in "Recovery Regenerate":
                     user_health += user_tuple[1]
                     random_health += random_tuple[1]
                     print("Seems both have taken time to Regenerate themselves")
                     i += 1
                     continue
                     sleep(2)
                else:    
                    if user_tuple[0] in "Recovery Regenerate":
                        regenerate_check += 1
                        if user_tuple[1] > random_tuple[1]:
                            user_health = user_health + user_damage
                            print(str(user_character).upper(), "Has Regenerated!")
                            sleep(2)
                        else:
                            user_health = user_health - random_damage
                            print(str(user_character).upper(), "Could Regenerate, But The damage dealt was too much to regenerate")
                            sleep(2)
                                
                    if random_tuple[0] in "Recovery Regenerate":
                        regenerate_check += 1
                        if random_tuple[1] > user_tuple[1]:
                            random_health = random_health + random_damage
                            print(str(random_character).upper(), "Has Regenerated!")
                            sleep(2)
                        else:
                            random_health = random_health - user_damage
                            print(str(random_character).upper(), "Could Regenerate, But The damage dealt was too much to regenerate")
                            sleep(2)
                
            if user_tuple[0] in "Dodge Substitution Jutsu" or random_tuple[0] in "Dodge Substitution Jutsu":        
                if user_tuple[0] in "Dodge Substitution Jutsu":
                    print(str(user_character).upper(), "Has Dodged the Attack!!")
                    sleep(2)
                    random_damage = 0
                
                if random_tuple[0] in "Dodge Substitution Jutsu":
                    print(str(random_character).upper(), "Has Dodged The Attack")
                    sleep(2)
                    user_damage = 0
                    
            if user_tuple[0] in  "Run" or random_tuple[0] in "Run":        
                if user_tuple[0] in "Run":
                    print("JOJO has decided to make a run for it, This Technique has been passed on for generations")
                    sleep(2)
                        
                
                if random_tuple[0] in "Run":
                    print("JOJO has decided to make a run for it, This Technique has been passed on for generations")
                    sleep(2)
                        
                
            if user_tuple[0] in "Pass" or random_tuple[0] in "Pass":    
                if user_tuple[0] in "Pass":
                    if regenerate_check == 0:
                        user_health = user_health - random_damage
                    print(str(user_character).upper(), "Couldnt Counter Attack And takes the full extent of the attack!")
                    sleep(2)
                        
                
                if random_tuple[0] in "Pass":
                    if regenerate_check == 0:
                        random_health = random_health - user_damage
                    print(str(random_character).upper(), "Couldnt Counter Attack and Takes the full extent of the attack!")
                    sleep(2)
                        

            
            if user_tuple[1] >= 300 and random_tuple[1] >= 300:
                print("Its a BATTLE OF THE ULTIMATE, Lets see whose attack is more Powerful!!")
                sleep(2)
            
            if user_tuple[1] >= 300 and user_tuple[1] > random_tuple[1]:
                if regenerate_check == 0:
                    random_health -= user_damage
                print(str(user_character).upper(), "Has delivered A Power Attack, That is sure to Hurt")
                sleep(2)
                
            if random_tuple[1] >= 300 and random_tuple[1] > user_tuple[1]:
                if regenerate_check == 0:
                    user_health -=  random_damage
                print(str(random_character).upper(), "Has delivered A Power Attack, That is sure to Hurt")
                sleep(2)
                    
                
        else:
            if user_tuple[1] > random_tuple[1]:
                random_health -= user_damage
                print("Ooh, It seems", str(user_character).upper(), "got the Upperhand here")
                sleep(2)
            else:
                user_health -= random_damage
                print("Ooh, It seems", str(random_character).upper(), "got the Upperhand here")
                sleep(2)
        
        if user_tuple[1] == random_tuple[1]:
            print("It seems Both Attacks Did Equal Damage and Cancelled each other Out!")        
                    
            
        
        if user_tuple[3] > 0 or random_tuple[3] > 0:
            if user_tuple[3] > 0:
                user_health -= user_tuple[3]
                print("Seems like The Damage wasnt Done to the Enemy Only, and ", str(user_character).upper(), "has taken a knockback")
                sleep(2)
            if random_tuple[3] > 0:
                random_health -= random_tuple[3]
                print("Seems like The Damage wasnt Done to the Enemy Only, and ", str(random_character).upper(), "has taken a knockback")
                sleep(2)
        i += 1        

    print("Health:", user_health, "\t\t\t\t", "Health:", random_health)
    sleep(3)
    print("="*71)
    if user_health > random_health:
        print("THE BATTLE IS OVER!!, It was a fierce one, Big blows from both sides, but only ONE VICTOR")
        sleep(1)
        print("And it seems", str(user_character).capitalize(), "Has come out on Top and is the winner of this Glorious Battle!!")
        sleep(1)
        print(username, ",You are the Winner of this Fight Club")
    else:
        print("THE BATTLE IS OVER!!, It was a fierce one, Big blows from both sides, but only ONE VICTOR")
        sleep(1)
        print("And it seems", str(random_character).capitalize(), "Has come out on Top and is the winner of this Glorious Battle!!")
        sleep(1)
        print(username, "You lose this battle my friend. Better Luck next time!")
   
        
        
        

#Battle Part of the game - (2)
def Battle(user_character, random_character, username):
    print("YOUR BATTLE SHALL BE AGAINST THE FEARED:", str(random_character).capitalize())
    sleep(3)
    print("Here is the List of the Attacks Your Character Performs:")
    print("-" * 90)
    print("Name\t\t\t\t\tDAMAGE\t\t\t\t\tKnockback")
    #Fetching Both User's and Random's Character data from Database
    show_user_attacks = "SELECT * FROM " + str(user_character)
    show_random_attacks = "SELECT * FROM " + str(random_character)
    mycursor.execute(show_user_attacks)
    user_list_of_moves = mycursor.fetchall()
    for i in user_list_of_moves:
        for j in range(0,4):
            if j == 2:
                continue
            bs_check = len(i[0])
            if bs_check <= 8:
                print(i[j], end = "\t\t\t\t\t")
            else:
                if j == 1:
                    print(i[1], end = "\t\t\t\t\t")
                    continue
                if bs_check > 16:
                    print(i[j], end = "\t\t\t")
                else:   
                    print(i[j], end = "\t\t\t\t")
                
        print("\n")

    mycursor.execute(show_random_attacks)
    random_list_of_attacks = mycursor.fetchall()
    random_list = [1, 2, 3, 4, 5, 6, 7, 8]
    user_moves = {}
    random_moves = {}
    input("Press Enter To Continue...")
    print("Now Its time you assign Random Numbers to These Moves so We can Commence Battle,\nIf you wish to, you can let the computer to randomise the move for you, Or you can\nRandomise them yourself")
    randomising_choice = int(input("Enter 1 to assign the moves yourself, and Enter 2 to let Computer do it for you, we are all lazy after all\nEnter your Choice:"))
    if randomising_choice == 2:
        random.shuffle(random_list)
        for i in range(0, 8):
            user_moves.update({random_list[i]: user_list_of_moves[i]})
            
    elif randomising_choice == 1:
        
        cls()
        print("\nRemember Not to assign same number to another Move")
        while True:
            user_check = []
            mistake = 0
            for i in user_list_of_moves:
                print(i[0], ":", end = " ")
                user_move_assignment = int(input())
                if user_move_assignment in user_check:
                    print("You seem to have inputted a number that has already been assigned to another move. Cant do that Bucko. Try again")
                    print("="*71)
                    mistake = 1
                    break
                else:
                    user_check.append(user_move_assignment)
                    user_moves.update({user_move_assignment: i})
            break
        print("\n")
        
    else:
        print("You had to choose between 1 and 2.... And you chose something different entirely, why do you do this")
        sleep(2)
        Battle(user_character, random_character, username)
        
    random.shuffle(random_list)
    for i in range(0,8):
        random_moves.update({random_list[i]: random_list_of_attacks[i]})

    Battle_2(user_moves, random_moves, user_character, random_character, username)  

                                  
                                  
#Playing the Game - (1)
def Gameplay():
    cls()

    print("\nHello Contestant, Welcome to The Fight Club! May I know your name?")
    username = input("Enter your Name:")
    print("Nice Name, Pleased to meet you", username)
    sleep(2)
    print("Before proceed ahead, I am hoping you have read the Instructions or It will get very confusing to keep up")
    check = input("Did you read the Instruction? If not, you shall be taken to the Instruction page to be given a brief on the way this Fight Club works (Yes or No):")
    if check.lower() in "no":
        Instructions()
        
    elif check.lower() in "yes":    
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
            if pick_character > 10 or pick_character <= 0:
                print("Invalid Choice Bucko, Cant do that")
                continue
            break
        
        user_character = show_character[pick_character - 1] #This allows for making a Dictionary out of the given table. This is a user character and we need a random character too
        while True:
            random_character = show_character[random.randint(0,9)]
            if str(user_character) in str(random_character):
                continue
            break
        
        cls()
        print("YOU CHOSE:", str(user_character).upper(), "!!")
        #REPLACE THIS WITH A QUOTE FOR THE CHARACTER

        Battle(user_character, random_character, username)

    else:
        print("Error, Wrong option chosen, There wasnt such option at all, You shall be directed to the Main Page")
        print("="*71)
        sleep(2)
        Main_menu()

def List_Characters():
    sleep(2)
    character_quote = [
        "It Is Fine Now. Why? Because I Am Here!",
        "All men have limits. They learn what they are and learn not to exceed them. I ignore mine.",
        "Yare Yare Daze",
        "To know what is right and choose to ignore it is the act of a coward.",
        "But A Hero Is A Guy Who Gives Out The Meat To Everyone Else. I Want To Eat The Damn Meat!",
        "Wubba Lubba Dub Dub!",
        "That'd be me. The Spider-Man of tomorrow, here to save today..",
        "I’m here to fight for truth and justice.",
        "You’re big. I’ve fought bigger.",
        "We are Venom,"
        ]
    mycursor.execute("SHOW TABLES")
    show_character = [item[0] for item in mycursor.fetchall()]
    j = 1
    for i in show_character:
        print(j,".", str(i).capitalize())
        print('"', character_quote[j-1], '"')
        print("\n")
        sleep(1)
        j = j+1
    input("\nPress Enter to Continue to Main Menu")
    print("=" * 90)
    Main_Menu()
    
    
def Instructions():
    
    print("="*71)
    print("\t\t INSTRUCTION PAGE")
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
    sleep(2)
    print("Damage Dealt will be decided by whoever's attack has the most damage, the damage will be reduced and dealt to the character accordingly")
    sleep(2)
    print("There are certain characters with Special attacks, LOOK OUT FOR THEM, cause if played right, could turn the tides around!")
    sleep(2)
    input("Enter to continue...")
    print("="*71)
    Main_Menu()
    
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
        return
    else:
        print("Invalid Choice. How did you mess up picking between 4 numbers?")
        try_again = input("Wish to Try again? Press and Enter 'Y' for Yes and 'N' for No:")
        if try_again in 'Yy':
            Main_Menu()
        elif try_again in 'Nn':
            return
        else:
            print("Failed again? How many Chances Should I provide? You should Honestly Just quit and try again or reflect on life choices")
            
    
































#MAIN PART OF THE FILE    
Main_Menu()                 
