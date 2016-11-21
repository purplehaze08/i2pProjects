from datetime import datetime
now = datetime.now()
import random


print('%s/%s/%s %s:%s:%s'% (now.day, now.month, now.year, now.hour, now.minute, now.second))
import time
playerProgress = 0
inventoryList = ["healing potion", "healing potion", "healing potion"]
def introStory():
    print("""This is a story of hatred, a young innocent soul Billy’s destiny was
changed forever on this date. Billy was an innocent young boy from the local village.
He spend most of his time helping around the village helping around and doing chores.""")
time.sleep(4)

print("""\nTwas the night of April 20, when young Billy’s life changed forever. The wind howled,
the trees rustled, and a thunderstorm formed over Billy’s hut. The night grew ever more
restless as time passed. It was at that moment, when the clock struck 12 when a dark shade appeared.""")
time.sleep(4)

print('''\n"Billy, you will never forget this day, for I,
Captain Van Sparrow has stolen your potatoes in the fridge."
''')
time.sleep(3)

print(
'''
\nBilly's eyes flashed in bewilderment, as he scrambled to his feet, running for
the fridge. Sweat dripped down face, his veins bulging out of his forehead. His
arm reached out for the handle and flung open the fridge with the force of a
thousand men. Time seemed to pause as his eyes were transfixed on the empty
space within the middle of the fridge.
''')
time.sleep(5)

print(
'''
\n"It can’t be...” whimpered Billy. To this day, Billy has never forgotten
about this incident; it haunted him day and night. His dignity, pride, passion,
and future had been ruined in a blink of an eye. The potatoes he grew last
summer were stolen. And then Billy died.
''')
time.sleep(5)

def kidnap():
    print("""You wake up to the sound of an engine. You are chained up in the backseat of Van's car, and the last thing you remmeber is drinking that whiskey a stranger offered you.""")
    print("""However, you see a golden key on Captain Van. You can reach for the key but there is a risk of getting caught.""")
    hehexd = 0
    while hehexd < 20:
        vChoice = input("Do you reach for the key? Yes or no. ")
        vChoice = vChoice.lower()
        if vChoice == "yes":
            print("You reach for the key hanging on Van's buckle and open the chains around your hand. You seize the opportunity and jump off the vehicle.")
            time.sleep(1)
            escape()
            break

        elif vChoice == "no":
            print("You hesitate for a moment and decide to not reach for the key. Van arrives at a shack and he kills you. \nYou failed to avenge Billy.")
            break

        else:
            print("Choose a valid input.")
            continue

def escape():
    global playerProgress
    print("Progress: ", playerProgress,"%")
    print("""\nAs you fumble to your feet after jumping off the vehicle, you see a bush nearby and hide behind it. You peek out from the bush and see Van looking for you.""")
    time.sleep(2)
    print("""You then see a bag lying right in the open. The bag is within reach but there is a chance of getting caught.""")
    hehexd = 0
    while hehexd < 20:
        vChoice2 = input("Do you reach for the bag? Yes or no. ")
        vChoice2 = vChoice2.lower()
        if vChoice2 =="yes":
            print("""You reach for the bag and quickly retract your hand. Thankfully Van doesn't notice. You open the bag and find some handful items.""")
            inventoryList = ["healing potion", "healing potion", "healing potion"]
            print("You aquired ",len(inventoryList), "items:", inventoryList)
            playerProgress = playerProgress + 25
            time.sleep(1)
            decision()
            break
        elif vChoice2 == "no":
            print("""You patiently wait for Van to go away. However, a rock suddenly drops over your head. The rock slams into your head and now you lose the capability to think! You walk out of the bush and Van kills you.""")
            break
        else:
            print("Choose a valid input.")
            continue

def decision():
    global playerProgress
    print("Progress: ", playerProgress, "%")
    print("""\nYou turn around and see Van staring back at you. There's a short wall in front of you. You can try to climb over or fight Van.""")
    hehexd = 0
    while hehexd < 20:
        vChoice3 = input("Do you climb over the wall? Yes or no. ")
        vChoice3 = vChoice3.lower()
        if vChoice3 == "yes":
            print("""You sprint straight at the wall in an attempt to jump over. However, you trip and run into the wall Usain Bolt speed. Your head is instantly mushed into meat paste. You died!""")
            break
        elif vChoice3 == "no":
            print("""You look back at Van and make you final stand. Van reloads his pistol to take a shot at you, but only a click sound is heard. Smirking, Van throws away the gun and pulls out a dagger.""")
            playerProgress = playerProgress + 25
            time.sleep(1)
            battle()
            break
        else:
            print("Choose a valid input.")
            continue

def battle():
    vanHealth = 10
    playerHealth = 10
    swordAttack = 1
    vanAttack = 2
    healing_potion = 10
    gachigasm = 0
    swordCrit = 4
    print("You are now fighting Van!")
    while gachigasm == 0:
        global inventoryList
        if vanHealth > 0 and playerHealth > 0:
            vBattleChoice = input("What do you do? Fight or Inventory.")
            vBattleChoice = vBattleChoice.lower()
            if playerHealth > 10:
                playerHealth = 10
                continue
            else:
                if vBattleChoice == "fight":
                    vCritchance = random.randrange(1,10)
                    if vCritchance <= 2:
                        swordAttack = swordCrit

                        print("\nYou attack Van, it was super effective. You did:",swordAttack,"damage.")
                        time.sleep(1)
                        vanHealth = vanHealth - swordAttack
                        print("Van attacks you. He did.",vanAttack, "damage.")
                        time.sleep(1)
                        playerHealth = playerHealth - vanAttack
                        print("\nYour health: ",playerHealth)
                        print("Van's health: ",vanHealth)
                        time.sleep(1)
                        continue
                    else:
                        print("\nYou attack Van. You did.",swordAttack,"damage.")
                        time.sleep(1)
                        vanHealth = vanHealth - swordAttack
                        print("Van attacks you. He did.",vanAttack, "damage.")
                        time.sleep(1)
                        playerHealth = playerHealth - vanAttack
                        print("\nYour health: ",playerHealth)
                        print("Van's health: ",vanHealth)
                        time.sleep(1)
                        continue

                elif vBattleChoice == "inventory":
                    print("Your inventory: ",inventoryList)
                    vInventoryChoice = input("Use healing potion or cancel? ")
                    vInventoryChoice = vInventoryChoice.lower()
                    if vInventoryChoice == "healing potion":
                        inventoryList.remove("healing potion")
                        playerHealth = playerHealth + 10
                        print("You healed for 10 health")
                        if playerHealth > 10:
                            playerHealth = 10
                            time.sleep(1)
                            print("Your health: ",playerHealth)
                            print("Van attacks you. He did.",vanAttack, "damage.")
                            time.sleep(1)
                            playerHealth = playerHealth - vanAttack
                            print("\nYour health: ",playerHealth)
                            print("Van's health: ",vanHealth)
                            time.sleep(1)
                            continue
                        else:
                            time.sleep(1)
                            print("Your health: ",playerHealth)
                            continue

                    elif vInventoryChoice == "cancel":
                        continue
                    else:
                        print("Choose a valid input.")
                        continue
                else:
                    print("Choose a valid input.")
                    continue
        elif playerHealth == 0:
            print("You are dead!")
            break
        elif vanHealth <= 0:
            print("You win!")
            playerProgress = 100
            print("Progress: ", playerProgress, "%")
            break
###Running the game
introStory()
kidnap()
