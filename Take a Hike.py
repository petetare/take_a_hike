''' Tareyn Peters | CSC 119 | Final Project '''

import time

# Establish variables
rope = 0
firstAidKit = 0
emergencyBeacon = 0


# Story Introduction
def intro():
    print("It's a beautiful day in Colorado.")
    print("You decide to take on the mountain, and go for a hike.")
    time.sleep(2)
    itemSelection()
    print("\nYou head out on the trail")   
    
# Item Selection Function
def itemSelection():
    print("\nYou grab your day pack and toss in a bottle of water,")
    print("some trail mix, and your rain coat.")
    time.sleep(2)
    print("\nThere is room for one more item in your pack, what do you grab?")
    print("\t1. Rope and Carabineer")
    print("\t2. First Aid Kit")
    print("\t3. Emergency Beacon")
    itemChoice = int(input("\t>>> "))
    if itemChoice == 1:
        print("You've added the rope and carabineer to your pack.")
        global rope
        rope = 1
        pathSelection()
    elif itemChoice == 2:    
        print("You've added the first aid kit to your pack.")
        global firstAidKit
        firstAidKit = 1
        pathSelection()
    elif itemChoice == 3:
        print("You've added the emergency beacon to your pack.")
        global emergencyBeacon
        emergencyBeacon = 1
        pathSelection()
    else:
        print("\nChoose option 1, 2, or 3.")
        itemSelection()
        time.sleep(2)
    return
    
    
# Path Selection Function
def pathSelection():
    print("\nBefore long, you come to an intersection. Which way do you go?")
    print("\t1. continue straight.")
    print("\t2. turn left.") 
    print("\t3. take the trail to the right.")
    time.sleep(2)
    pathChoice = int(input("\t>>> "))
    if pathChoice == 1:
        print("You head straight, going deeper into the trees.")
        pathOne()
    elif pathChoice == 2:    
        print("You turn left and head up a rugged, rocky trail...")
        pathTwo()
    elif pathChoice == 3:
        pathThree()
        print("You veer to the trail on the right.")
    else:
        print("Choose option 1, 2, or 3.")
        pathSelection()
        time.sleep(2)
    return


# Path One: Continue Straight
def pathOne():
    time.sleep(2)
    print("\nYou stop for a water break.")
    time.sleep(2)
    print("When you look up after putting your water bottle back into your pack...")
    time.sleep(2)
    print("There is a bear staring your down! What do you do?")
    print("\t1. Run!")
    print("\t2. Stand tall, wave your arms, and scream.")
    print("\t3. Play dead.")
    bearChoice = int(input("\t>>> "))
    if bearChoice == 1:
        print("You might be fast...")
        time.sleep(2)
        print("but you can't outrun a bear.")
        time.sleep(2)
        print("They never find your mutilated remains...")
        print("\nGame Over")
        exitGame()
    elif bearChoice == 2:    
        print("The bear gives you a strange look...")
        time.sleep(2)
        print("He's not interested in your crazy antics.")
        time.sleep(2)
        print("The bear turns and walks away.")
        pathTwo()
    elif bearChoice == 3:
        print("You hit the ground and put your arms around your kneck.")
        time.sleep(2)
        print("The bear takes your act as a threat and begins to charge.")
        time.sleep(2)
        print("You curl up and hold tight.")
        time.sleep(2)
        print("After an agressive attack that seams to go on for hours,")
        print("the bear gives up and moves on.")
        time.sleep(2)
        print("You are bleeding badly and your pretty sure your arm is broken.")
        global emergencyBeacon
        if emergencyBeacon == 1:
            print("You send a distress signal using the emergency beacon from your pack.")
            time.sleep(2)
            emergencyBeacon = -1
            print("Search and Rescue shows up before long and flies you off of the moutnain.")
            print("\nGame Over")
            exitGame()
        else:
            print("Without the emergency beacon, there's no way to get help...")
            time.sleep(2)
            print("Search and Rescue finds your body two weeks later.")
            print("\nGame Over")
            exitGame()
    else:
        print("Choose option 1, 2, or 3.")
        pathOne()
        time.sleep(1)
    return


# Path Two: Turn left, Rocky Trail
def pathTwo():
    print("\nAs you hike, the trail becomes more and more rugged.")
    time.sleep(2)
    print("After some time, you find yourseld above treeline.")
    time.sleep(2)
    print("The sky suddnely begins to darken and it starts to rain.")
    time.sleep(2)
    print("You hear thunder in the distance and know you have to get off the mountain as soon as possible.")
    storm()
    return
    
    
# Storm Function
def storm():
    time.sleep(1)
    print("What do you do?")
    print("\t1. crouch under a large rock and wait it out.")
    print("\t2. scramble down the steep, slippery mountain.")
    print("\t3. use your rope and carabineer to rappel quickly to your base camp.")
    stormChoice = int(input("\t>>> "))
    if stormChoice == 1:
        print("You grab your raincoat from your pack and huddle under a rock.")
        time.sleep(2)
        print("The temperature drops quickly and before you know it, it's dark out.")
        if emergencyBeacon == 1:
            print("You send a distress signal using the emergency beacon from your pack.")
            time.sleep(2)
            print("Search and Rescue shows up before long and flies you off of the moutnain.")
            print("\nGame Over")
            exitGame()
        else:
            time.sleep(1)
            print("You shiver, and shake, and your hands start to feel numb.")
            time.sleep(2)
            print("Hypothermia starts to set in.")
            time.sleep(2)
            print("Without the emergency beacon, there's no way to get help.")
            time.sleep(2)
            print("Search and Rescue finds your body two days later.")
            print("\nGame Over")
            exitGame()
    elif stormChoice == 2:    
        print("As the thunder crashed closer, and closer, you start back down the mountain.")
        time.sleep(2)
        print("The path is slippery and the rain comes down harder and harder.")
        time.sleep(1)
        print("You slip, and take a nasty fall down the mountain to your death.")
        print("\nGame Over")
        exitGame()
    elif stormChoice == 3:
        if rope ==1:
           print("You quickly tie your rope around a large boulder.")
           time.sleep(2)
           print("Using the carabineer you create a hitch on the rope and rappel safely off the mountain.")
           time.sleep(2)
           print("You're releived you made it out safe.")
           time.sleep(2)
           print("\nGame Over")
           exitGame()
        else:
            print("You decide to rappel down the mountain.")
            time.sleep(2)
            print("But, wait, you didn't bring the rope and carabineer.")
            time.sleep(2)
            print("You'll have to try something else.")
            storm()
    else:
        print("Choose option 1, 2, or 3.")
        storm()
    return


# Path Three: Trail to the Right
def pathThree():
    print("\nThe trail to the right leads to a beautiful meadow.")
    time.sleep(2)
    print("The view of the mountain from the valley is spectacular.")
    time.sleep(2)
    print("You walk, in awe, staring at the breathtaking view until...")
    time.sleep(2)
    print("You step into a prairie dog hole and twist your ankle.")
    time.sleep(2)
    print("\nYou stand, but immediately crumble to the ground.")
    time.sleep(2)
    print("You can't walk...")
    if firstAidKit == 1:
        print("Luckily, you have the first aid kit.")
        time.sleep(2)
        print("You use it to wrap your ankle.")
        time.sleep(2)
        print("It's paintful, but with the wrap you're able to hobble back to your base camp.")
        print("\nGame Over")
        exitGame()
    else:
        print("If you had the first aid kit, you could wrap your ankle.")
        time.sleep(2)
        print("But you don't, so you try to crawl back to your base camp.")
        time.sleep(2)
        print("\nYou don't make it far before you startle a rattle snake.")
        time.sleep(2)
        print("It strikes.....")
        print("The snake bites your arm and the venom quickly sets in.")
        global emergencyBeacon
        if emergencyBeacon == 1:
            print("\nYou use the emergency beacon to send a distress signal.")
            time.sleep(2)
            print("Search and Resucue is able to find you quickly.")
            time.sleep(2)
            print("Your flown to the nearest hospital and live to tell the story.")
            time.sleep(2)
            print("You're one lucky s.o.b.!")
            time.sleep(2)
            print("\nGame Over")
            exitGame()
        else:
            print("\nWithout the emergency beacon to signal for help, you die quickly.")
            time.sleep(2)
            print("Search and rescue finds your body a few days later.")
            time.sleep(2)
            print("\nGame Over")
            exitGame()

# Restart or Exit Function
def exitGame():
    exitGameChoice = int(input("\nPress 1 to start over. Press 2 to exit: "))
    if exitGameChoice == 1:
        print("\n" * 5)
        intro()
    else:
        exit(0)

# Game Title!
print(" _ _ _   _ _ _   _  _   _ _ _")  
print("|_   _| |  _  | | |/ / | _ _ |")
print("  | |   | | | | |   /  | |_")
print("  | |   | |_| | |   \  |  _|_")
print("  |_|   |_| |_| |_|\_\ |_ _ _|") 
print("  _ _ _")  
print(" |  _  |") 
print(" | | | |") 
print(" | |_| |") 
print(" |_| |_|") 
print(" _     _   _ _ _   _  _   _ _ _")  
print("| |_ _| | |_   _| | |/ / | _ _ |")
print("|  _ _  |   | |   |   /  | |_")
print("| |   | |  _| |_  |   \  |  _|_")
print("|_|   |_| |_ _ _| |_|\_\ |_ _ _|")
print("\n" * 5)

intro()