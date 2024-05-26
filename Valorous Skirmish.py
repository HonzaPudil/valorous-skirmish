#Osnova: Main menu ---> Bitva ---> Vyber cpu ---> vyber special ---> vyber item ---> [Bojové menu ---> bojvyber ---> cpuvyber ---> vypočet ---> opakovat do smrti všech v teamu] 

import os
import sys
import random
import colorama #Barvy
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

executable_dir = os.path.dirname(sys.executable)
os.chdir(executable_dir)

class Leader:

    def __init__(self, name):
        self.name = name        #atributa bude určená až při vytváření objektu
        self.hp = 1             #atributa je 1 u každého objektu této třídy do té doby, než je změněna.       počet životů
        self.defence = 0        #počítá pokolikáté se bojovník/velitel brání
        self.attack = 0         #určuje na koho bojovník/ kapitán útočí
        self.maxsh = False      #bude True pokud byl dosažen maximální počet bránění po sobě
        self.special = 0        #určuje jakou specialku bojovník má (kapitam žádnou nemá, proto zůstane 0), Specialky se dají použít jednou za hru
        self.dead = False       #True pokud hp je menší než 1
        self.using_special = 0  #změní se v 1 pokud bojovník využívá specialku v tomto tahu
        self.item = 0           #určuje jaký item bojovník má (kapitam žádnou nemá, proto zůstane 0)


class Warrior:

    def __init__(self,name):
        self.name = name
        self.hp = 3
        self.special = 0     
        self.using_special = 0                       
        self.defence = 0
        self.attack = 0
        self.maxsh = False                  
        self.specialmem = 0     #pokud specialmem je roven nule tak byla už specialka využita
        self.dead = False
        self.item = 0
        self.quick_boots = False    #potřebné pro třetí item
        

list_of_specials = [0, "Doubled Attack","Lasting Shield","Shield Break","Regenerate"]   
#Seznam speciálních schopností

list_of_items = [0, 'Sharp Sword', 'Strong Shield', 'Quick Boots', 'Reflectal Fragment']        
#Seznam pomocných předmětů

class Battle:
    
    def __init__(self):
        self.round = 0                  #počet kol
        self.warriors_total = 0         #počet bojovníků naživu
        self.enemy_warriors_total = 0   #počet nepřátel naživu
        self.leader = False             #zdali vyšel kapitán
        self.leaderX = False            #zdali vyšel nepřátelský kapitán
        self.cpu = 0                    #který protivník proti nám bude hrát

    def declare_warriors(self):
        global leader_1, enemy_leader_1, warrior_1, warrior_2, warrior_3, enemy_warrior_1, enemy_warrior_2, enemy_warrior_3
        #golbální proměnné

        leader_1 = Leader("     You     ")
        enemy_leader_1 = Leader("Enemy Leader")
        #tvorba kapitánů

        warrior_1 = Warrior("Warrior 1")
        warrior_2 = Warrior("Warrior 2")
        warrior_3 = Warrior("Warrior 3")

        enemy_warrior_1 = Warrior(" Enemy 1 ")
        enemy_warrior_2 = Warrior(" Enemy 2 ")
        enemy_warrior_3 = Warrior(" Enemy 3 ")
        #tvorba bojovníků

        global list_of_warriors, list_of_enemy_warriors, list_of_warriors_2, list_of_enemy_warriors_2
        #golbální seznamy

        list_of_warriors = [warrior_1, warrior_2, warrior_3, leader_1]
        list_of_enemy_warriors = [enemy_warrior_1, enemy_warrior_2, enemy_warrior_3, enemy_leader_1]

        list_of_warriors_2 = [warrior_1, warrior_2, warrior_3]
        list_of_enemy_warriors_2 = [enemy_warrior_1, enemy_warrior_2, enemy_warrior_3]
        #seznamy s bojovníky

    
    def choose_special(self):
        list_of_specials_choosing = list_of_specials[:]
        list_of_special_length = int(len(list_of_specials_choosing))
        list_of_special_length = list_of_special_length - 1
        #nakopíruje seznam speciálek a určí délku

        print("\n\n\nChoose which Specials your Warriors will have.")

        
        for i, warrior in enumerate(list_of_warriors):
            #vybere bojovníky ze seznamu
            if i < 3:
                #kapitán je čtvrtý a nemá mít speciálku
                while True:
                        try:
                            print("\nChoose Special for " + warrior.name + ".")
                            for j in range(len(list_of_specials_choosing)-1):            
                                j += 1
                                print(f"({j}) {list_of_specials_choosing[j]}", end="  ")   
                                #vypíše výběr schopností vedle sebe

                            choose_special = input("\n\n> ")             
                            if 1 > int(choose_special) or int(choose_special) > int(list_of_special_length)-i:
                                print("\nThat is not a valid option. Try again.") 
                                continue
                                #kontroluje zdali nebyla zmáčknuta špatná klávesa
                            else:
                                if list_of_specials_choosing[int(choose_special)] == list_of_specials[1]:
                                    warrior.special= 1
                                    warrior.specialmem = 1
                                elif list_of_specials_choosing[int(choose_special)] == list_of_specials[2]:
                                    warrior.special = 2
                                    warrior.specialmem = 1
                                elif list_of_specials_choosing[int(choose_special)] == list_of_specials[3]:
                                    warrior.special = 3
                                    warrior.specialmem = 1
                                elif list_of_specials_choosing[int(choose_special)] == list_of_specials[4]:
                                    warrior.special = 4
                                    warrior.specialmem = 1
                                #porovnává výběr a přiřazuje schopnosti

                                list_of_specials_choosing.pop(int(choose_special))
                                #smaže vybranou schopnost z nakopírovaného seznamu
                        except ValueError:
                            #zjistí, jestli bylo vložen špatný datový typ
                            print("\nThat is not a valid option. Try again.")
                            continue
                        else:
                            break 
                            #kontroluje zdali nebyla zmáčknuta špatná klávesa

    def choose_item(self):
        #stejné jako u speciálek
        list_of_items_choosing = list_of_items[:]
        list_of_item_length = int(len(list_of_items_choosing))
        list_of_item_length = list_of_item_length - 1

        print("\n\n\nChoose which items your Warriors will have.")

        
        for i, warrior in enumerate(list_of_warriors):
            if i < 3:
                while True:
                        try:
                            print("\nChoose item for " + warrior.name + ".")
                            for j in range(len(list_of_items_choosing)-1):            
                                j += 1
                                print(f"({j}) {list_of_items_choosing[j]}", end="  ")   
                            choose_item = input("\n\n> ")             
                            if 1 > int(choose_item) or int(choose_item) > int(list_of_item_length)-i:
                                print("\nThat is not a valid option. Try again.") 
                                continue
                            else:
                                if list_of_items_choosing[int(choose_item)] == list_of_items[1]:
                                    warrior.item= 1
                                elif list_of_items_choosing[int(choose_item)] == list_of_items[2]:
                                    warrior.item = 2
                                elif list_of_items_choosing[int(choose_item)] == list_of_items[3]:
                                    warrior.item = 3
                                elif list_of_items_choosing[int(choose_item)] == list_of_items[4]:
                                    warrior.item = 4

                                list_of_items_choosing.pop(int(choose_item))
                        except ValueError:
                            print("\nThat is not a valid option. Try again.")
                            continue
                        else:
                            break 
            

    def test1(self):
        print("skill issue")
        #toto není využíváno

    
    def choose_special_cpu(self):
        #stejné jako u hráče ale výběr je dělán počítačem
        list_of_specials_cpu = list_of_specials[:]
        list_of_special_length = int(len(list_of_specials_cpu))
        list_of_special_length -= 1

        for i, enemy in enumerate(list_of_enemy_warriors):
            if i < 3:
                choose_special = random.randint(1,4-i)    
        
                if list_of_specials_cpu[int(choose_special)] == list_of_specials[1]:
                    enemy.special= 1
                    enemy.specialmem = 1
                elif list_of_specials_cpu[int(choose_special)] == list_of_specials[2]:
                    enemy.special = 2
                    enemy.specialmem = 1
                elif list_of_specials_cpu[int(choose_special)] == list_of_specials[3]:
                    enemy.special = 3
                    enemy.specialmem = 1
                elif list_of_specials_cpu[int(choose_special)] == list_of_specials[4]:
                    enemy.special = 4
                    enemy.specialmem = 1

                list_of_specials_cpu.pop(int(choose_special))


    def choose_item_cpu(self):
        #stejné jako u speciálek
        list_of_items_cpu = list_of_items[:]
        list_of_item_length = int(len(list_of_items_cpu))
        list_of_item_length = list_of_item_length - 1
        
        for i, warrior in enumerate(list_of_warriors):
            if i < 3:     
                choose_item = random.randint(1,4-i) 

                if list_of_items_cpu[int(choose_item)] == list_of_items[1]:
                    warrior.item= 1
                elif list_of_items_cpu[int(choose_item)] == list_of_items[2]:
                    warrior.item = 2
                elif list_of_items_cpu[int(choose_item)] == list_of_items[3]:
                    warrior.item = 3
                elif list_of_items_cpu[int(choose_item)] == list_of_items[4]:
                    warrior.item = 4

                list_of_items_cpu.pop(int(choose_item))


    def specials(self, warrior):
        #do této funkce je přesměrován bojovník když chce využít speciálku
        #víc o bojovém výběru ve funkci battle_menu
        if warrior.special == 1 or warrior.special == 3:
            #1 a 3 jsou útočné speciálky
            while True:
                try:
                    print(f'\n{warrior.name} has the Special "{list_of_specials[warrior.special]}".')
                    if self.leaderX == False:
                        choice = int(input("\nAttack who?\n" + "(1)" + enemy_warrior_1.name + "   (2)" + enemy_warrior_2.name + "   (3)" + enemy_warrior_3.name + "\n\n> "))
                    else:
                        choice = int(input("\nAttack who?\n" + "(1)" + enemy_warrior_1.name + "   (2)" + enemy_warrior_2.name + "   (3)" + enemy_warrior_3.name + "   (4)" + enemy_leader_1.name + "\n\n> "))
                    
                    if choice == 1:
                        if enemy_warrior_1.hp == 0:
                            print("\n There is no point attacking the dead.")
                            continue
                        else:
                            warrior.attack = 1
                            print("\n" + warrior.name + " will attack " + enemy_warrior_1.name , "with", '"' + list_of_specials[int(warrior.special)] + '"' + "!")
                    elif choice == 2:
                        if enemy_warrior_2.hp == 0:
                            print("\n There is no point attacking the dead.")
                            continue
                        else:
                            warrior.attack = 2
                            print("\n" + warrior.name + " will attack " + enemy_warrior_2.name , "with", '"' + list_of_specials[int(warrior.special)] + '"' + "!")
                    elif choice == 3:
                        if enemy_warrior_3.hp == 0:
                            print("\n There is no point attacking the dead.")
                            continue
                        else:
                            warrior.attack = 3
                            print("\n" + warrior.name + " will attack " + enemy_warrior_3.name , "with", '"' + list_of_specials[int(warrior.special)] + '"' + "!")
                    elif self.leaderX == True and choice == 4:
                        if enemy_leader_1.hp == 0:
                            print("\n There is no point attacking the dead.")
                            continue
                        else:
                            warrior.attack = 4
                            print("\n" + warrior.name + " will attack " + enemy_leader_1.name , 'with','"' + list_of_specials[int(warrior.special)] + '"' +"!")
                    else:
                        print("\nThat is not a valid option. Try again.") 
                        continue
                except ValueError:
                    print("\nThat is not a valid option. Try again.")
                    continue
                else:
                    break  

        elif warrior.special == 2 or warrior.special == 4:
            #obranné schopnosti
            print(f'\n{warrior.name} has the Special "{list_of_specials[int(warrior.special)]}".')
            print(f'\n{warrior.name} will use "{list_of_specials[int(warrior.special)]}"!')       



    def battle_menu(self):
        for i, warrior in enumerate(list_of_warriors):
            if self.leader == False and i == 3:
                #přeskočí kapitána, pokud není vyvolán
                continue
            if warrior.hp > 0:
                if warrior.defence == 2 and warrior.item != 2 or int(warrior.defence) == 3 and warrior.item == 2:
                    #počítá dosažení limitu bránění
                    warrior.maxsh = True
                else:
                    warrior.maxsh = False
                while True:
                    try:
                        if warrior.special == 0:
                            #ukazuje menu bez speciálky pokud již byla využita
                            choice = int(input("\nWhat will "+ warrior.name +" do?\n" + "(1)Attack   (2)Block\n\n> ")) 
                        else:
                            choice = int(input("\nWhat will "+ warrior.name +" do?\n" + "(1)Attack   (2)Block   (3)Special\n\n> "))  
                        if int(choice) == 1: 
                            #útok
                                warrior.using_special = 0
                                #když útočí bojovník tak nevyužívá speciálku
                                if warrior.defence != 5:
                                    #defence je pět když byla využita speciálka Lasting Shield
                                    warrior.defence = 0
                                if self.leaderX == False:
                                    #menu cílema s a bez kapitána nepřátel
                                    choice = int(input("\nAttack who?\n" + "(1)" + enemy_warrior_1.name + "   (2)" + enemy_warrior_2.name + "   (3)" + enemy_warrior_3.name + "\n\n> "))
                                else:
                                    choice = int(input("\nAttack who?\n" + "(1)" + enemy_warrior_1.name + "   (2)" + enemy_warrior_2.name + "   (3)" + enemy_warrior_3.name + "   (4)" + enemy_leader_1.name + "\n\n> "))
                                
                                if choice == 1:
                                    if enemy_warrior_1.hp == 0:
                                        #útočit na mrtvého je zbytečné
                                        print("\n There is no point attacking the dead.")
                                        continue
                                    else:
                                        warrior.attack = 1
                                        print("\n" + warrior.name + " will attack " + enemy_warrior_1.name + "!")
                                elif choice == 2:
                                    if enemy_warrior_2.hp == 0:
                                        print("\n There is no point attacking the dead.")
                                        continue
                                    else:
                                        warrior.attack = 2
                                        print("\n" + warrior.name + " will attack " + enemy_warrior_2.name + "!")
                                elif choice == 3:
                                    if enemy_warrior_3.hp == 0:
                                        print("\n There is no point attacking the dead.")
                                        continue
                                    else:
                                        warrior.attack = 3
                                        print("\n" + warrior.name + " will attack " + enemy_warrior_3.name + "!")
                                elif self.leaderX == True and choice == 4:
                                    if enemy_leader_1.hp == 0:
                                        print("\n There is no point attacking the dead.")
                                        continue
                                    else:
                                        warrior.attack = 4
                                        print("\n" + warrior.name + " will attack " + enemy_leader_1.name + "!")
                                else:
                                    print("\nThat is not a valid option. Try again.") 
                                    continue
                                    
                        elif choice == 2:
                            #bránění
                            warrior.using_special = 0
                            if warrior.defence == 5:
                                #nelze mít dva štíty
                                print("\n"+ warrior.name + " already has a shield!")
                                continue
                            
                            if int(warrior.defence) == 3 and warrior.item != 2 or int(warrior.defence) == 4 and warrior.item == 2:
                                #dosažen limit
                                print("\n" + warrior.name + " has used their shield too many times in a row!")
                                continue
                            else:
                                warrior.defence = int(warrior.defence) + 1
                                print("\n" + warrior.name + " will defend!")
                        
                        elif choice == 3:
                            #specilka
                            if warrior.special == 0:
                                #není speciál
                                print("\nThat is not a valid option. Try again.") 
                                continue
                            else:
                                if warrior.specialmem == 0:
                                    #speciál už byl využit
                                    print("\n" + warrior.name + " has already used their special!")
                                    continue
                                else:
                                    warrior.specialmem = 0
                                    warrior.using_special = 1
                                    warrior.defence = 0
                                    self.specials(warrior) 
                                    #přesměrování
                        else:
                            print("\nThat is not a valid option. Try again.") 
                            continue

                    except ValueError:
                        print("\nThat is not a valid option. Try again.")
                        continue
                    else:
                        break


    def battle_menu_info(self):
        self.round += 1
        #průběžný výpis dat 

        print("\nIt's round No. "+ str(self.round)+ "!\n") 
        print("   ____________________________________________________________________________________")
        print("  /  Your Team   /                        BATTLE                        \\  Enemy Team  \\")
        print(" /______________/________________________________________________________\\______________\\")

        if self.leader == True and self.leaderX == False:
            print(" | " + leader_1.name + "\\    HP: " + str(leader_1.hp) + "   \\                              /            /              |")
            print(" |_______________\\____________\\____________________________/____________/_______________|")

        if self.leader == False and self.leaderX ==True:
            print(" |              \\            \\                              /   HP: " + str(enemy_leader_1.hp) + "    / " + enemy_leader_1.name + " |")
            print(" |_______________\\____________\\____________________________/____________/_______________|")

        if self.leader == True and self.leaderX == True:
            print(" | " + leader_1.name + "\\    HP: " + str(leader_1.hp) + "   \\                              /   HP: " + str(enemy_leader_1.hp) + "    / " + enemy_leader_1.name + " |")
            print(" |_______________\\____________\\____________________________/____________/_______________|")

        print(" | " + str(warrior_1.name) + " | HP: " + str(warrior_1.hp) + " | Special: " + str(warrior_1.specialmem) + " |" + "=" + Fore.RED +" __" + Fore.RESET +" ====" + Fore.RED +" _______" + Fore.RESET +" ==" + "| " + str(enemy_warrior_1.name) + " | HP: " + str(enemy_warrior_1.hp) + " | Special: " + str(enemy_warrior_1.specialmem) + " |")
        print(" |-----------|-------|------------|-" + Fore.RED + " \\ \\ "+ Fore.RESET +"--" + Fore.RED + " / / ____|" + Fore.RESET +" -|-----------|-------|------------|")
        print(" | " + str(warrior_2.name) + " | HP: " + str(warrior_2.hp) + " | Special: " + str(warrior_2.specialmem) + " |" + "==" + Fore.RED +" \\ \\  / / (___" + Fore.RESET +" ===" + "| " + str(enemy_warrior_2.name) + " | HP: " + str(enemy_warrior_2.hp) + " | Special: " + str(enemy_warrior_2.specialmem) + " |")
        print(" |-----------|-------|------------|---" + Fore.RED + " \\ \\/ / \\___ \\ " + Fore.RESET + "--|-----------|-------|------------|")
        print(" | " + str(warrior_3.name) + " | HP: " + str(warrior_3.hp) + " | Special: " + str(warrior_3.specialmem) + " |" + "==== " + Fore.RED + "\\  /  ____) | " + Fore.RESET + "=" + "| " + str(enemy_warrior_3.name) + " | HP: " + str(enemy_warrior_3.hp) + " | Special: " + str(enemy_warrior_3.specialmem) + " |")
        print(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾" + Fore.RED +"\\/" + Fore.RESET + "‾‾" + Fore.RED +"|_____/" + Fore.RESET + "‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
    

    def choose_cpu(self):
        self.cpu = random.randint(1,4)
        #výběr obtížnosti

    def cpu_battle_logic(self):
        choice_cpu = 1
        print("\nCalculating Turn...")
        for i, enemy in enumerate(list_of_enemy_warriors):
            if self.leaderX == False and i == 3:
                continue
            if enemy.hp > 0:
                while True:
                    if int(self.cpu) == 1:
                        if enemy.name == enemy_leader_1.name:
                            choice_cpu = random.randint(1,2)
                        else:
                            choice_cpu = random.randint(1,3)
                            

                    elif int(self.cpu) == 2:
                        if enemy.name == enemy_leader_1.name:
                            choice_cpu = random.randint(5,7)
                        else:
                            if enemy.hp >= 2:
                                choice_cpu = random.randint(1,6)
                            elif enemy.hp == 1:
                                choice_cpu = random.randint(2,8)
                            #počítač se snaží bránit když má málo životů

                    elif int(self.cpu) == 3 or int(self.cpu) == 4:
                        if enemy.name == enemy_leader_1.name:
                            decision = random.randint(0,1)
                            if decision == 0:
                                choice_cpu = random.randint(2,7)
                                if int(choice_cpu) == 3:
                                    choice_cpu = 4
                                    #kapitán nemůže využívat speciálku

                            else:
                                choice_cpu = 2
                        else:
                            decision = random.randint(0,1)
                            #počítač má na výběr ze dvou stylů každý tah

                            if enemy.hp == 3:
                                if decision == 0:
                                    choice_cpu = 1
                                else:
                                    choice_cpu = random.randint(1,5)
                            elif enemy.hp == 2:
                                if decision == 0:
                                    choice_cpu = random.randint(1,6)
                                else:
                                    choice_cpu = random.randint(5,8)
                            elif enemy.hp == 1:
                                if decision == 0:
                                    choice_cpu = random.randint(2,8)
                                else:
                                    choice_cpu = random.randint(7,8)

                        if leader_1.maxsh == True:
                            enemy.attack = 4
                            break
                        elif warrior_1.maxsh == True:
                            enemy.attack = 1
                            break
                        elif warrior_2.maxsh == True:
                            enemy.attack = 2
                            break
                        elif warrior_3.maxsh == True:
                            enemy.attack = 3
                            break
                        #počítač útočí když je dosažen limit bránění u nás

                        if int(self.cpu) == 4:
                            decision = random.randint(0,1)
                            if enemy.defence != 3:
                                if decision == 1:
                                    if enemy.name == enemy_warrior_1.name:
                                        if warrior_1.attack == 1 or warrior_2.attack== 1 or warrior_3.attack == 1 or leader_1.attack == 1:
                                            choice_cpu = 2
                                    elif enemy.name == enemy_warrior_2.name:
                                        if warrior_1.attack == 2 or warrior_2.attack== 2 or warrior_3.attack == 2 or leader_1.attack == 2:
                                            choice_cpu = 2
                                    elif enemy.name == enemy_warrior_3.name:
                                        if warrior_1.attack == 3 or warrior_2.attack== 3 or warrior_3.attack == 3 or leader_1.attack == 3:
                                            choice_cpu = 2
                                    elif enemy.name == enemy_leader_1.name:
                                        if warrior_1.attack == 4 or warrior_2.attack== 4 or warrior_3.attack == 4 or leader_1.attack == 4:
                                            choice_cpu = 2
                            #počítač může podvádět tím, že zjistí na koho se útočí


                    if choice_cpu == 1 or choice_cpu == 4 or choice_cpu == 5:
                        #útok

                        enemy.using_special = 0
                        enemy.defence = 0
                        while True:
                            if self.leader == False:
                                enemy.attack = random.randint(1,3)
                            else:
                                enemy.attack = random.randint(1,4)

                            if int(self.cpu) == 2 or int(self.cpu) == 3:

                                if leader_1.hp == 1 and self.leader == True:
                                    enemy.attack = 4
                                elif warrior_1.hp == 1:
                                    enemy.attack = 1
                                elif warrior_2.hp == 1:
                                    enemy.attack = 2
                                elif warrior_3.hp == 1:
                                    enemy.attack = 3
                                    #počítač útočí na slabé bojovníky

                            if warrior_1.hp == 0 and enemy.attack == 1:     
                                continue
                            if warrior_2.hp == 0 and enemy.attack == 2:                               
                                continue
                            if warrior_3.hp == 0 and enemy.attack == 3:
                                continue
                            if self.leader == True and leader_1.hp == 0 and enemy.attack == 4:
                                continue
                            else:
                                break
                            #počítač neútočí na mrtvé

                        break
                    elif choice_cpu == 2 or choice_cpu == 6 or choice_cpu == 7:
                        #bránění

                        enemy.using_special = 0
                        if int(enemy.defence) == 2:                     
                            continue
                        else:
                            enemy.defence += 1
                            break
                    else:
                        #specialka
                        if enemy.specialmem == 0:
                            continue
                        else:
                            enemy.specialmem = 0
                            enemy.using_special = 1
                            enemy.defence = 0
                            if enemy.special == 1 or enemy.special == 3:
                                    while True:
                                        if self.leader == False:
                                            enemy.attack = random.randint(1,3)
                                        else:
                                            enemy.attack = random.randint(1,4)
                                        #výběr

                                        if warrior_1.hp == 0 and enemy.attack == 1:     
                                            continue
                                        if warrior_2.hp == 0 and enemy.attack == 2:                               
                                            continue
                                        if warrior_3.hp == 0 and enemy.attack == 3:
                                            continue
                                        if self.leader == True and leader_1.hp == 0 and enemy.attack == 4:
                                            continue
                                        else:
                                            break
                                        
                            break
          


    def battle_calculation(self): 
        #bojový výpočet

        warrior_name_1 = "" 
        enemy_name_1 = ""

        warrior_name_2 = ""
        enemy_name_2 = ""

        print("\nCalculating Turn...")      


        # První fáze: obranné schopnosti.

        for i, warrior in enumerate(list_of_warriors):
            #bojovníci

            if warrior.using_special == 1:

                if warrior.special == 2:
                    warrior.defence = 5
                    print(f'\n{warrior.name} defended using "Lasting Shield".')
                    #druhá speciálka

                elif warrior.special == 4:
                    warrior.hp += 1
                    print(f'\n{warrior.name} gained HP with "Regenerate".')
                    #čtvrtá speciálka

        for i, enemy in enumerate(list_of_enemy_warriors): 
            #nepřátelé

            if enemy.using_special == 1:

                if enemy.special == 2:
                    enemy.defence = 5
                    print(f'\n{enemy.name} defended using "Lasting Shield".')

                elif enemy.special == 4:
                    enemy.hp += 1
                    print(f'\n{enemy.name} gained HP with "Regenerate".')

        # druhá fáze: útok

        for i, warrior in enumerate(list_of_warriors):

            if warrior.attack != 0: 
                j = (warrior.attack - 1) 
                #zjistí kdo ůtočil na aktuálně vybraného bojovníka

                if list_of_enemy_warriors[j].attack != i+1:

                    if list_of_enemy_warriors[j].defence != 0:
                        #zjistí jestli se nepřítel brání

                        if warrior.special == 3 and warrior.using_special == 1:
                            #zjistí pokud používáme níčič stítu

                            if list_of_enemy_warriors[j].item == 3 and warrior.hp <= 0 and list_of_enemy_warriors[j].attack != (i + 1):
                                list_of_enemy_warriors[j].quick_boots = True
                                #pomocný předmět potřebuje přepočet později

                            else:
                                list_of_enemy_warriors[j].hp -= 1
                                print(f'\n{warrior.name} hit {list_of_enemy_warriors[j].name} with "Shield Break"!')
                                #2. speciálka níčí štít

                                if list_of_enemy_warriors[j].item == 4:
                                    decision =  random.randint(1,5)
                                    #4. předmět odráží útok 20% doby

                                    if decision == 1:
                                        warrior.hp -= 1
                                        print(f'\n{list_of_enemy_warriors[j].name} reflected the attack using "{list_of_items[4]}"!')
                                        print(f'{warrior.name} lost 1 HP!')

                                if list_of_enemy_warriors[j].defence == 5:
                                    list_of_enemy_warriors[j].defence = 0 
                                    print(f'{warrior.name} broke {list_of_enemy_warriors[j].name}s "Lasting Shield"!')
                                    #zníčen lasting shield

                                print(f'{list_of_enemy_warriors[j].name} lost 1 HP!')

                        elif list_of_enemy_warriors[j].defence == 5:
                            list_of_enemy_warriors[j].defence = 0
                            print(f'\n{warrior.name} broke {list_of_enemy_warriors[j].name}s "Lasting Shield"!')

                            if list_of_enemy_warriors[j].item == 4:
                                decision =  random.randint(1,5)

                                if decision == 1:
                                    warrior.hp -= 1
                                    print(f'\n{list_of_enemy_warriors[j].name} reflected the attack using "{list_of_items[4]}"!')
                                    print(f'{warrior.name} lost 1 HP!')

                        else:
                            print(f'\n{list_of_enemy_warriors[j].name} blocked {warrior.name}s attack!') 
                            #nebyl využit níčič štítu a nepřítel nemá lasting shield

                            if list_of_enemy_warriors[j].item == 4:
                                decision =  random.randint(1,5)

                                if decision == 1:
                                    warrior.hp -= 1
                                    print(f'\n{list_of_enemy_warriors[j].name} reflected the attack using "{list_of_items[4]}"!')
                                    print(f'{warrior.name} lost 1 HP!')

                    else:

                        if list_of_enemy_warriors[j].item == 3 and warrior.hp <= 0 and list_of_enemy_warriors[j].attack != (i + 1):
                                list_of_enemy_warriors[j].quick_boots = True

                        else:

                            if warrior.special == 1 and warrior.using_special == 1:
                                list_of_enemy_warriors[j].hp -= 2
                                print(f'\n{warrior.name} hit {list_of_enemy_warriors[j].name} with "Doubled Attack"!')
                                print(f'{list_of_enemy_warriors[j].name} lost 2 HP!')
                                #využita speciálka dvojtý útok

                            else:
                                list_of_enemy_warriors[j].hp -= 1
                                print(f'\n{warrior.name} hit {list_of_enemy_warriors[j].name}!')
                                print(f'{list_of_enemy_warriors[j].name} lost 1 HP!') 
                                #normální úder

                else:
                    #duel (dva bojovníci na sebe útočí)
                    if warrior.item == 1 and list_of_enemy_warriors[j].item != 1:
                        decision = random.randint(2, 10)
                        #pomocný předmět pro převahu

                    elif list_of_enemy_warriors[j].item == 1 and warrior.item != 1:
                        decision = random.randint(11, 19)

                    else:
                        decision = random.randint(0, 1)
                        #nemá předmět nebo oba mají

                    if decision == 0 or (decision <= 6 and decision != 1) or decision > 15:
                        #výsledek duelu

                        if list_of_enemy_warriors[j].item != 3:

                            if warrior.special == 1 and warrior.using_special == 1:
                                list_of_enemy_warriors[j].hp -= 2
                                print(f'\n{warrior.name} hit {list_of_enemy_warriors[j].name} with "Doubled Attack"!')
                                print(f'{list_of_enemy_warriors[j].name} lost 2 HP!')

                            else:
                                list_of_enemy_warriors[j].hp -= 1
                                print(f'\n{warrior.name} hit {list_of_enemy_warriors[j].name}!')
                                print(f'{list_of_enemy_warriors[j].name} lost 1 HP!')
                        
                        else:
                            list_of_enemy_warriors[j].quick_boots = True
                        
                    else:

                        if warrior.item != 3:

                            if list_of_enemy_warriors[j].special == 1 and list_of_enemy_warriors[j].using_special == 1:
                                warrior.hp -= 2
                                print(f'\n{warrior.name} was hit by {list_of_enemy_warriors[j].name} with "Doubled Attack"!')
                                print(f'{warrior.name} lost 2 HP!')

                            else:
                                warrior.hp -= 1
                                print(f'\n{warrior.name} was hit by {list_of_enemy_warriors[j].name}!')
                                print(f'{warrior.name} lost 1 HP!')
                        
                        else:
                            warrior.quick_boots = True


     
        for i, enemy in enumerate(list_of_enemy_warriors): 
            #stejné jako předtím ale pro přátele ale bez duelu
            if enemy.attack != 0: 
                j = (enemy.attack - 1)

                if list_of_warriors[j].attack != i+1:                               

                    if list_of_warriors[j].defence != 0:

                        if enemy.special == 3 and enemy.using_special == 1:
                            if list_of_warriors[j].item == 3 and enemy.hp <= 0 and list_of_warriors[j].attack != (i + 1):
                                print(f'\n{list_of_warriors[j].name} dodged {enemy.name} using "Quick Boots"!')

                            else:
                                list_of_warriors[j].hp -= 1
                                print(f'\n{list_of_warriors[j].name} was hit by {enemy.name} using "Shield Break"!')

                                if list_of_warriors[j].item == 4:
                                    decision =  random.randint(1,5)

                                    if decision == 1:
                                        enemy.hp -= 1
                                        print(f'\n{list_of_warriors[j].name} reflected the attack using "{list_of_items[4]}"!')
                                        print(f'{enemy.name} lost 1 HP!')

                                if list_of_warriors[j].defence == 5:
                                    list_of_warriors[j].defence = 0 
                                    print(f'{list_of_warriors[j].name}s "Lasting Shield" was broken by {enemy.name}!') 

                                print(f'{list_of_warriors[j].name} lost 1 HP!')

                        elif list_of_warriors[j].defence == 5:
                            list_of_warriors[j].defence = 0 
                            print(f'\n{list_of_warriors[j].name}s "Lasting Shield" was broken by {enemy.name}!')

                        else:
                            print(f'\n{enemy.name} was blocked by {list_of_warriors[j].name}!')

                            if list_of_warriors[j].item == 4:
                                decision =  random.randint(1,5)

                                if decision == 1:
                                    enemy.hp -= 1
                                    print(f'\n{list_of_warriors[j].name} reflected the attack using "{list_of_items[4]}"!')
                                    print(f'{enemy.name} lost 1 HP!')

                    else:

                        if list_of_warriors[j].item == 3 and enemy.hp <= 0 and list_of_warriors[j].attack != (i + 1):
                            print(f'\n{list_of_warriors[j].name} dodged {enemy.name} using "Quick Boots"!')

                        else:

                            if enemy.special == 1 and enemy.using_special == 1:
                                list_of_warriors[j].hp -= 2
                                print(f'\n{list_of_warriors[j].name} was hit by {enemy.name} with "Doubled Attack"!')
                                print(f'{list_of_warriors[j].name} lost 2 HP!')
                                
                            else:
                                list_of_warriors[j].hp -= 1
                                print(f'\n{list_of_warriors[j].name} was hit by {enemy.name}!')
                                print(f'{list_of_warriors[j].name} lost 1 HP!')

        #třetí fáze: přepočet

        for i, enemy in enumerate(list_of_enemy_warriors):
            j = (enemy.attack - 1)

            if j < 3:

                if list_of_warriors_2[j].quick_boots == True:

                    if enemy.hp <= 0:
                        print(f'{list_of_warriors_2[j]} dodged using "Quick Boots"!')
                        #pokud nepřítel v tomto kole umřel, bojovník unikne trefě
                        
                    else:

                        if enemy.special == 1 and enemy.using_special == 1:
                            list_of_warriors_2[j].hp -= 2
                            print(f'\n{list_of_warriors_2[j].name} was hit by {enemy.name} with "Doubled Attack"!')
                            print(f'{list_of_warriors_2[j].name} lost 2 HP!')

                        else:
                            list_of_warriors_2[j].hp -= 1
                            print(f'\n{list_of_warriors_2[j].name} was hit by {enemy.name}!')
                            print(f'{list_of_warriors_2[j].name} lost 1 HP!')
        
        for i, warrior in enumerate(list_of_warriors):

            j = (warrior.attack - 1)

            if j < 3:

                if list_of_enemy_warriors_2[j].quick_boots == True:

                    if warrior.hp <= 0:
                        print(f'{list_of_enemy_warriors_2[j]} dodged using "Quick Boots"!')
                        
                    else:
                        #přepočet, jelikož kvůli schopnosti toto bylo přeskočeno
                        if list_of_enemy_warriors[j].defence != 0:

                            if warrior.special == 3 and warrior.using_special == 1:
                                list_of_enemy_warriors[j].hp -= 1
                                print(f'\n{warrior.name} hit {list_of_enemy_warriors[j].name} with "Shield Break"!')

                                if list_of_enemy_warriors[j].item == 4:
                                    decision =  random.randint(1,5)

                                    if decision == 1:
                                        warrior.hp -= 1
                                        print(f'\n{list_of_enemy_warriors[j].name} reflected the attack using "{list_of_items[4]}"!')
                                        print(f'{warrior.name} lost 1 HP!')

                                if list_of_enemy_warriors[j].defence == 5:
                                    list_of_enemy_warriors[j].defence = 0 
                                    print(f'{warrior.name} broke {list_of_enemy_warriors[j].name}s "Lasting Shield"!')

                                print(f'{list_of_enemy_warriors[j].name} lost 1 HP!')

                            elif list_of_enemy_warriors[j].defence == 5:
                                list_of_enemy_warriors[j].defence = 0
                                print(f'\n{warrior.name} broke {list_of_enemy_warriors[j].name}s "Lasting Shield"!')

                                if list_of_enemy_warriors[j].item == 4:
                                    decision =  random.randint(1,5)

                                    if decision == 1:
                                        warrior.hp -= 1
                                        print(f'\n{list_of_enemy_warriors[j].name} reflected the attack using "{list_of_items[4]}"!')
                                        print(f'{warrior.name} lost 1 HP!')

                            else:
                                print(f'\n{list_of_enemy_warriors[j].name} blocked {warrior.name}s attack!') 

                                if list_of_enemy_warriors[j].item == 4:
                                    decision =  random.randint(1,5)

                                    if decision == 1:
                                        warrior.hp -= 1
                                        print(f'\n{list_of_enemy_warriors[j].name} reflected the attack using "{list_of_items[4]}"!')
                                        print(f'{warrior.name} lost 1 HP!')

                        else:

                            if warrior.special == 1 and warrior.using_special == 1:
                                list_of_enemy_warriors[j].hp -= 2
                                print(f'\n{warrior.name} hit {list_of_enemy_warriors[j].name} with "Doubled Attack"!')
                                print(f'{list_of_enemy_warriors[j].name} lost 2 HP!')

                            else:
                                list_of_enemy_warriors[j].hp -= 1
                                print(f'\n{warrior.name} hit {list_of_enemy_warriors[j].name}!')
                                print(f'{list_of_enemy_warriors[j].name} lost 1 HP!') 

        
            
    def warrior_check(self):
        #kontrola živých

        warriors = 0
        enemy_warriors = 0

        for i, warrior in enumerate(list_of_warriors_2):
            if warrior.hp > 0:
                warriors += 1
        if warriors <= 1 and leader_1.hp > 0:
            self.leader = True
            warriors += 1
            #pokud se kapitán přidá do bitvy tak se s ním také počítá

        self.warriors_total = warriors

        for i, enemy in enumerate(list_of_enemy_warriors_2):
            if enemy.hp > 0:
                enemy_warriors += 1
        if enemy_warriors <= 1 and enemy_leader_1.hp > 0:
            self.leaderX = True
            enemy_warriors += 1

        self.enemy_warriors_total = enemy_warriors


    def final_edit(self):
        for i, warrior in enumerate(list_of_warriors):            
            if int(warrior.hp)<1 and warrior.dead == False:
                #pokud bojovník umřel toto kole bude zde prohlášen za mrtvého

                print(f'\n{warrior.name} died!')
                warrior.hp = 0
                warrior.dead = True
                if warrior.name == leader_1.name:
                    warrior.name = "    Dead     "
                    #aby se jméno vešlo do tabulky a neníčilo jí
                else:
                    warrior.name = "  Dead   "
                warrior.specialmem = 0
                self.warriors_total -= 1

            warrior.attack = 0 
            warrior.using_special = 0
            warrior.quick_boots = False
            #vynulování určitých údajů
        
        for i, enemy in enumerate(list_of_enemy_warriors):  
            #stejné jako u bojovníků
            if int(enemy.hp)<1 and enemy.dead == False:
                print(f'\n{enemy.name} died!')
                enemy.hp = 0
                enemy.dead = True
                if enemy.name == enemy_leader_1.name:
                    enemy.name = "    Dead    "
                else:
                    enemy.name = "  Dead   "
                enemy.specialmem = 0
                self.enemy_warriors_total -= 1

            enemy.attack = 0  
            enemy.using_special = 0
            enemy.quick_boots = False

  

class Game:
    def __init__(self):
        self.quit = False
        #jsetli True tak se ukončí hra
        self.win_streak = 0
    

    def main_menu(self):
        title_text = r"""
 ___      ___ ________  ___       ________  ________  ________  ___  ___  ________      
|\  \    /  /|\   __  \|\  \     |\   __  \|\   __  \|\   __  \|\  \|\  \|\   ____\     
\ \  \  /  / | \  \|\  \ \  \    \ \  \|\  \ \  \|\  \ \  \|\  \ \  \\\  \ \  \___|_    
 \ \  \/  / / \ \   __  \ \  \    \ \  \\\  \ \   _  _\ \  \\\  \ \  \\\  \ \_____  \   
  \ \    / /   \ \  \ \  \ \  \____\ \  \\\  \ \  \\  \\ \  \\\  \ \  \\\  \|____|\  \  
   \ \__/ /     \ \__\ \__\ \_______\ \_______\ \__\\ _\\ \_______\ \_______\____\_\  \ 
    \|__|/       \|__|\|__|\|_______|\|_______|\|__|\|__|\|_______|\|_______|\_________\
 ________  ___  __    ___  ________  _____ ______   ___  ________  ___  ___ \|_________|
|\   ____\|\  \|\  \ |\  \|\   __  \|\   _ \  _   \|\  \|\   ____\|\  \|\  \    
\ \  \___|\ \  \/  /|\ \  \ \  \|\  \ \  \\\__\ \  \ \  \ \  \___|\ \  \\\  \   
 \ \_____  \ \   ___  \ \  \ \   _  _\ \  \\|__| \  \ \  \ \_____  \ \   __  \  
  \|____|\  \ \  \\ \  \ \  \ \  \\  \\ \  \    \ \  \ \  \|____|\  \ \  \ \  \ 
    ____\_\  \ \__\\ \__\ \__\ \__\\ _\\ \__\    \ \__\ \__\____\_\  \ \__\ \__\
   |\_________\|__| \|__|\|__|\|__|\|__|\|__|     \|__|\|__|\_________\|__|\|__|
   \|_________|==============Valorous=Skirmish=============\|_________|     
        """
        #logo

        version = 1.0
        info = '\nHow to play the game?\n=====================\n\nPress buttons on your input device to pick options that were presented to you. When a ">" symbol is on the last row, an input is required to proceed. \n\nThere are 6 warriors on the battlefield at the beginning of the battle. 3 are on your side and 3 are against you. Every warrior can either attack, defend or use their Special.\nSpecials are versitile abilities that can be used once per battle. Specials are chosen for each warrior before the battle.\nWarriors also hold items, which help them throughout the battle. Those are also chosen before the battle.\nWhen only 1 warrior is left the leader will come out as a last resort backup.\nThe battle ends when there are no warriors left on one of the sides.'
        #údaje o hře

        with open('win_streak.py', 'r+') as f:
            self.win_streak = f.read()   
        #čtení výherní série

        print(f"{'Version ' +  str(version): >85}")
        print(f'{title_text}')
        print(f'{"Win streak: " + str(self.win_streak): >17}')
        while True:
            try:
                print('\n')
                the_choice = input(f'{"(1)    Battle" : ^70}\n{"(2)   Options" : ^70}\n{"(3)      Info" : ^70}\n{"(4)      Quit" : ^70}\n\n> ')
                if int(the_choice) == 1:
                    self.battle_sequence()
                elif int(the_choice) == 2:
                    options = input(f'\n Coming soon...\n\n> ')
                    continue
                elif int(the_choice) == 3:
                    options = input(
                        f"{info}\n\n\n\nVersion {version} - Finally done.\n\nCreated by Honza Pudil\n\n> "
                        )
                    continue
                elif int(the_choice) == 4:
                    exit()
                else:
                    print("\nThat is not a valid option. Try again.")
                    continue
            except ValueError:
                print("\nThat is not a valid option. Try again.")
                continue
            else:
                break  
        #hlavní menu a možnosti jsou tisknuty zde 
        
    def win_streak_write(self, win):
        with open('win_streak.py', 'w') as f:
            if win is True:
                f.write(str(int(self.win_streak) + 1))
            else:
                f.write('0')
        #psaní série výher
        
        


    def battle_sequence(self):
        #herní sekvence
        while not self.quit:
            battle = Battle()
            battle.declare_warriors()
            battle.choose_cpu()
            battle.choose_special()
            battle.choose_special_cpu()
            battle.choose_item()
            battle.choose_item_cpu()
            battle.warrior_check()
            #příprava bojovníků a počítače
            print(f'\nThe battle begins!\n')

            while battle.warriors_total > 0 and battle.enemy_warriors_total > 0:
                battle.battle_menu_info()
                battle.battle_menu()
                battle.cpu_battle_logic()
                battle.battle_calculation()
                battle.final_edit()
                battle.warrior_check()
            #bitva

            if battle.warriors_total > 0:
                self.win_streak_write(True)
                print(f'\n\n\nYour team won!')
            #výhra

            elif battle.enemy_warriors_total > 0:
                self.win_streak_write(False)
                print(f'\n\n\nYour team lost!')
            #prohra
                
            with open('win_streak.py', 'r+') as f:
                self.win_streak = f.read()   

            print(f'\n Current win streak: {self.win_streak}')
            #aktuální výherní série

            while True:
                try:
                    final_choice = input(f'\n (1)   Next Battle   (2) Quit\n\n> ')
                    if final_choice < 1 or final_choice > 2:
                        print("\nThat is not a valid option. Try again.")
                        continue
                        
                except ValueError:
                    print("\nThat is not a valid option. Try again.")
                    continue
                else:
                    break

            if int(final_choice) == 2:
                self.quit = True
                #ukončí herní smyčku



#spustí hru:
game = Game()
game.main_menu()
sys.exit()
# ukončí program

#__      _______ 
#\ \    / / ____|
# \ \  / / (___  
#  \ \/ / \___ \ 
#   \  /  ____) | very ascii art, such wow
#    \/  |_____/ 
