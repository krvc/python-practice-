from sys import exit 

morning = False

num_monsters = 1
mountains_count = 0

def mountains():
    global mountains_count
    mountains_count += 1
    
    if morning == False:
        print "You are in dark, you can barely make out the outline of a light"
        print "What do you do?"
        decision_mountains = raw_input("> ")
        if "turn" in decision_mountains or "flip" in decision_mountains:
            mountains_morning()
        elif "walk" in decision_mountains or "explore" in decision_mountains:
            dead("You wander around the in the dark and fall into a pit of spikes.")
        else:
            dead("You have selected none of the above.")
    else:
        print "Its morning now"
        mountains_morning() 
            
def mountains_morning():
    print "That's great, we have got the light, you see a pit of spikes which you avoid."   
    print "Two caves, one on the left with a lamp on the door, one on the right with a diamond symbol, what do you choose?"
    door_choose = raw_input("> ")
    if door_choose == "left" or door_choose == "Left":
        monster_room()
    elif door_choose == "Right" or door_choose == "right":
        luck_unluck_cave()
    else:
        dead("Seriously, why didn't you choose the one on left or right?")

def luck_unluck_cave():
    print "You face a hound in front of a door, and you see toy, what do you do?"
    hound_choice = raw_input("> ")
    if "throw" in hound_choice:
        print "The hound chases after the toy, and you proceed through the door."
        lucky_room()
    elif "growl" in hound_choice:
        dead("The hound bites you and you die")
    else:
        print "Since you want to", "\"" + hound_choice + "\"", "I'm not going to stop you." 
        dead("Good luck with that.")
    

def monster_room():
    global num_monsters
    swear_list = ['leave', 'die', 'damn', 'push', 'run']
    if num_monsters == 1:
        print "**A monster appears!"
        print "\nWhat do you wish for?"
    else:
        print "\n"
        print "Then " + "a monster appears then " * num_monsters + "they ask you:"
        print "\nNow that you have more monsters and wishes, what do you wish for?"
    wish = raw_input("> ")
    if "wishes" in wish:
        num_monsters += 1
        monster_room()
    elif "diamond" in wish or "gem" in wish or "luck" in wish:
        lucky_room()
    elif wish in swear_list:
        dead("You have a potty mouth!")
    else:
        print "Your wish: \"" + wish + "\" is granted!"
        dead("Good job.")
        
def lucky_room():
    luck_list = ['diamond', 'money', 'guns', 'chains', 'sapphire', 'stones', 'pearl', 'rings', 'silver', 'gold'] 
    print "*** Welcome to the luck room (in the luck module) ***"
    print "You see a giant pile of lucks, what type of lucks will you take?"
    luck_choice = raw_input("> ")
    if luck_choice in luck_list:
        print "You have chosen", "\"" + luck_choice + "\"" + ", excellent choice!"
    elif "all of them" in luck_choice or "everything" in luck_choice:
        print "As you take all of the lucks, a giant rock crashes down on you."
    else:
        print"So you didn't pick any of the available lucks."


def dead(end_text):
    print end_text, "\nGame Over." 
    print"input \"again\" to start over, or any other key then enter to exit"
    play_again = raw_input("> ")
    if play_again == "again":
        global morning
        global num_monsters
        num_monsters = 1
        morning = False # reintialize the first room with lights off
        mountains()
    else:
        exit()
mountains()
