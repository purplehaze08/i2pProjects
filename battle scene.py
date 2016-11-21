inventoryList = ["healing potion", "healing potion", "healing potion"]

import time
def battle():
    vanHealth = 10
    playerHealth = 10
    swordAttack = 1
    vanAttack = 2
    healing_potion = 10
    gachigasm = 0
    print("You are now fighting Van!")
    while gachigasm == 0:
        if vanHealth > 0 and playerHealth > 0:
            vBattleChoice = input("What do you do? Fight or Inventory.")
            vBattleChoice = vBattleChoice.lower()
            if playerHealth > 10:
                playerHealth = 10
                continue
            else:
                if vBattleChoice == "fight":
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
            break

battle()
