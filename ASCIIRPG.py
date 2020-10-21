import random
import os
import sys
import img
import spell
from spell import spelllevel
import quests
import time
import shop
from classes import class_init

p_class = random.randint(0,8)

p_class_p = class_init(p_class)

p_skill_name = [
"Warrior's Valor - Critical hits are more likely",
"Elemental Talent - Learns Flame at LVL 1",
"Passive Heal - Heals 5% Damage every turn",
"Looter - Earn 150% the amount of gold from defeating monsters",
"First Bullet Strike - begins a battle with a weak attack on the monster",
"All In - Every attack from both sides does 150%",
"Reanimate - Reanimates a corpse to aid in damage dealt",
"Spiders - Reanimates spiders to deal damage",
"Good Deal - Costs 50% less to buy a shop and stocks",
"Instrumentalist - Can earn money in the guild via song"]






days = 365
diff_days = [999,365,90,9999999999]
max_gold = 49999

print("""
1.Easy   - 999 days
2.Normal - 365 days
3.Hard   - 90  days
4.Endless
""")
difficultyinput = input("")
try:
    difficultyinput = int(difficultyinput)
    difficultyinput -= 1
except ValueError:
    difficultyinput = 1
days = diff_days[difficultyinput]
if difficultyinput != 3:
    print(f""" 
        _     ___    ___ ___ ___   ___ ___  ___ 
       /_\   / __|  / __|_ _|_ _| | _ | _ \/ __|
      / _ \  \__ \ | (__ | | | |  |   |  _| (_ |
     /_/ \_\ |___/  \___|___|___| |_|_|_|  \___|

    you have {days} days to earn 50,000 gold.                                        
                                                        """)
else:
    print(f""" 
        _     ___    ___ ___ ___   ___ ___  ___ 
       /_\   / __|  / __|_ _|_ _| | _ | _ \/ __|
      / _ \  \__ \ | (__ | | | |  |   |  _| (_ |
     /_/ \_\ |___/  \___|___|___| |_|_|_|  \___|

                                     
                                                        """)

time.sleep(3)
os.system('cls')
shop_on = False

def passtime():
    global days
    global gold
    days -= 1
    if gold > max_gold:
        input("Congrats! You win!")
        sys.exit()
    elif days == 0:
        input("Times up. The debt collectors have caught you.")
    else:
        input(f"{days} days left. {(max_gold+1)-gold} gold left!")

hp = 1

#SAVES
def save():
  global lvl
  global mhp
  global atk
  global defence
  global spd
  global gold
  global equip
  global inventory
  global exp
  global days
  global questlvl
  f = open("save.txt","w+")
  f.write(str(lvl)+"\n")
  f.write(str(mhp)+"\n")
  f.write(str(atk)+"\n")
  f.write(str(defence)+"\n")
  f.write(str(spd)+"\n")
  f.write(str(gold)+"\n")
  f.write(str(equip)+"\n")
  f.write(str(exp)+"\n")
  f.write(str(questlvl)+"\n")
  f.write(str(days)+"\n")
  f.write(str(p_class)+"\n")
  inven = "".join(inventory)
  f.write(str(inven))
  f.close()

def load():
  global lvl
  global mhp
  global atk
  global defence
  global spd
  global gold
  global equip
  global inventory
  global exp
  global days
  global questlvl
  global p_class
  global p_class_p
  global c_id
  f = open("save.txt","r")
  lvl = int(f.readline())
  mhp = int(f.readline())
  atk = int(f.readline())
  defence = int(f.readline())
  spd = int(f.readline())
  gold = int(f.readline())
  equip = int(f.readline())
  exp = int(f.readline())
  questlvl = int(f.readline())
  days = int(f.readline())
  p_class = int(f.readline())
  p_class_p = class_init(p_class)
  c_id = p_class_p[5]
  inven = f.readline()
  inven2 = inven.split()
  inventory = []
  for i in range(0,len(inven2)):
    inventory.append(int(inven2[i]))


#WEAPONS
weapon_name = ["Short Sword","Lumber Axe","Spear","Short-Bow","Rapier","Hammer","Ceremonial Lance","LongBow"]
weapon_atk = [5,9,6,4,7,13,10,6]
weapon_spd = [5,2,4,6,8,3,5,8]
weapon_acc = [80,70,80,85,90,70,87,93]
weapon_price = [350,400,450,480,800,750,820,900]

#ENEMIES
enemies = ["Slime","Warthog","Wolf","Bat","Red Slime","Silver Wolf","Bandit","Bat Nest","Green Slime","Wyvern"]

enemies_atk = [12,13,12,2,13,14,12,8,8,14]
enemies_atk_growth = [1,2,1,2,1,1,1,2,1,3]
enemies_spd = [3,2,3,8,4,3,4,10,8,10]
enemies_spd_growth = [2,0,2,7,2,2,1,10,8,5]
enemies_def = [7,8,7,6,8,8,5,4,7,4]
enemies_def_growth = [2,2,3,1,2,3,1,4,2,2]
enemies_hp = [10,20,15,5,11,16,20,30,35,50]
enemies_hp_growth = [2,4,3,0,2,3,2,0,3,2]
enemies_acc = [95,50,90,100,95,90,85,80,70,75]
enemies_expfloor = [25,55,20,10,20,50,80,70,65,99]
enemies_goldceiling = [80,130,100,30,140,250,500,150,180,750]
"""
input(len(enemies))
input(len(enemies_atk))
input(len(enemies_atk_growth))
input(len(enemies_spd))
input(len(enemies_spd_growth))
input(len(enemies_def))
input(len(enemies_def_growth))
input(len(enemies_hp))
input(len(enemies_hp_growth))
input(len(enemies_acc))
input(len(enemies_expfloor))
input("done")
"""

#PLAYER STATS
p_class_p = class_init(p_class)

atk = 7 + p_class_p[1]
spd = 7 + p_class_p[2]
defence = 7 + p_class_p[3]
mhp = 18 + p_class_p[4]
c_id = p_class_p[5]
lvl = 1
exp = 0
gold = 500
statpoints = 0
statadd = 3
equip = 0
questlvl = 0

#ITEMS
inventory = []
itemnames = ["Elixir","Elixir+","ElixirX"]
itemheals = [5,10,50]
itemprices = [100,300,500]

def statallocate():
  global atk
  global spd
  global defence
  global mhp
  global statpoints
  totalstatpoints = statpoints
  while statpoints > 0:
    os.system('cls')
    img.town_img(5)
    print(f"""
1.attack:{atk}
2.speed:{spd}
3.defence:{defence}
4.mhp:{mhp}
5.exit
----------------------
stat points left:{statpoints}""")
    statinput = input("")
    if statinput == "1":
      atk += 1
      statpoints -= 1
    if statinput == "2":
      spd += 1
      statpoints -= 1
    if statinput == "3":
      defence += 1
      statpoints -= 1
    if statinput == "4":
      mhp += 2
      statpoints -= 1
    if statinput == "5":
      break


def home():
  global atk
  global spd
  global defence
  global mhp
  global statpoints
  global gold
  global equip
  global inventory
  global exp
  global shop_on
  while True:
    os.system('cls')
    img.town_img(0)
    if gold <= 0:
      input("You ran out of money. GAME OVER")
      sys.exit(0)
    print(f"""
  1.Adventure's guild         {gold} Gold
  2.Go Hunting                {days} Days
  3.Stats
  4.Save
  5.Load
  6.Shop
  """)
    homeinput = input("")
    if homeinput == "1":
      guild()
      passtime()
    elif homeinput == "2":
      hunt(-1,0)#-1 is a random encounter. 0 allows gaining of gold
      passtime()
    elif homeinput == "4":
      save()
    elif homeinput == "5":
      load()
    elif homeinput == "6":
      passtime()
      if shop_on == False:
        if c_id == 8: #Business Man Skill
            shop_oninput = input("Buy a shop for 1500 gold?(y/n)")
            if shop_oninput == "y" and gold > 1500:
                shop_on = True
                gold -= 1500
        else:
            shop_oninput = input("Buy a shop for 3000 gold?(y/n)")
            if shop_oninput == "y" and gold > 3000:
                shop_on = True
                gold -= 3000
      if shop_on == True:
        gold = shop.shop(gold,c_id)
    else:
      os.system('cls')
      img.town_img(4)
      print(f"""
  _______________________
  class: {p_class_p[0]}
  attack:{atk}
  speed:{spd}
  defence:{defence}
  mhp:{mhp}
  equipped: {weapon_name[equip]}
  lvl:{lvl}
  exp until lvl up:{100-exp}
  -----------------------
  Inventory:""")
      for i in range(0,len(inventory)):
        print(f"  {itemnames[inventory[i]]}")
      input("")

def guild():
  global inventory
  global itemnames
  global itemheals
  global itemprices
  global gold
  global weapon_name
  global weapon_atk
  global weapon_spd
  global weapon_acc
  global weapon_price
  global equip
  global questlvl
  os.system('cls')
  img.town_img(1)
  print("""
1.Buy Items
2.Take a quest
3.Buy Weapons""")
  if c_id == 9:
    print("4.Sing a Song")
  guildinput = input("")
  if guildinput == "1":
    os.system('cls')
    img.town_img(2)
    print(f"""
    ____________________          {gold} Gold
   1 Elixir  : 100 gold
   2 Elixir+ : 300 gold
   3 ElixirX : 500 gold""")
    shopinput = input("")
    if len(inventory) == 5:
      input("Your Inventory is full!")
      guild()
    try:
      shopinput = int(shopinput)
    except ValueError:
      input("Invalid")
      return
    max_quantity = 5 - len(inventory)
    quantityinput = input("Quantity:")
    try:
      quantityinput = int(quantityinput)
    except ValueError:
      input("Invalid")
      return
    try:
      bulk_price = itemprices[shopinput-1] * quantityinput
    except IndexError:
      input("Invalid")
      return
    if quantityinput > max_quantity:
      input("Not enough space in your inventory")
      return
    if gold >= bulk_price:
      for i in range(0,quantityinput):
        inventory.append(shopinput-1)
      gold -= bulk_price
    else:
      input("Not enough money")
  if guildinput == "2":
    battle = quests.quests(questlvl)
    pregold = gold
    if battle[1] != -1:
      hunt(battle[1],1)
    if pregold == gold:
      input("Quest complete!")
      gold += battle[0]
    else:
      input(f"Quest failed. Failure fee is {int(battle[0] / 2)} gold")
      gold -= int(battle[0] / 2)
    questlvl = battle[2]

  if guildinput == "3":
    os.system('cls')
    img.town_img(3)
    try:
      for i in range(1,len(weapon_name)):
        print(f"{i}.{weapon_name[i]}  {weapon_price[i]} gold")
        print("-----------------------------")
        print(f"{weapon_atk[i]} atk {weapon_spd[i]} spd {weapon_acc[i]} acc")
        print("")
      print(f"Equipped: {weapon_name[equip]}      {gold} Gold")
      weaponinput = input("")
      try:
        weaponinput = int(weaponinput)
      except ValueError:
        return
      if weaponinput == equip:
        input("You already own this")
        return

      if gold >= weapon_price[weaponinput]:
        input(f"Purchased {weapon_name[weaponinput]} and sold {weapon_name[equip]}")
        equip = weaponinput
        gold -= weapon_price[weaponinput]
      else:
        input("Not enough Money!")
    except IndexError:
      input("Invalid")
      return
  if guildinput == "4" and c_id == 9:
    os.system('cls')
    img.town_img(6)
    rnroll = random.randint(0,251)
    gold += rnroll
    print(f"You earnt {rnroll} gold in the tavern by singing")
    
      



def battleinit(chosen):
  global enemy_name
  global enemy_atk
  global enemy_def
  global enemy_spd
  global enemy_hp
  global enemy_lvl
  global enemy_acc
  global enemy_expfloor
  global chosen_enemy
  enemy_lvl = lvl - 1
  enemy_lvl_ceiling = int(lvl * 1.125)
  enemy_lvl_floor = int(lvl * 0.875)
  enemy_lvl = random.randint(enemy_lvl_floor,enemy_lvl_ceiling)
  chosen_enemy = chosen
  if chosen_enemy == -1:
    chosen_enemy = random.randint(0,3)
  else:
    chosen_enemy = chosen
  enemy_name = enemies[chosen_enemy]
  enemy_atk = enemies_atk[chosen_enemy]
  enemy_def = enemies_def[chosen_enemy]
  enemy_spd = enemies_spd[chosen_enemy]
  enemy_hp = enemies_hp[chosen_enemy]
  enemy_acc = enemies_acc[chosen_enemy]
  enemy_expfloor = enemies_expfloor[chosen_enemy]
  for i in range(0,enemy_lvl):
    enemy_atk += enemies_atk_growth[chosen_enemy]
  for i in range(0,enemy_lvl):
    enemy_spd += enemies_spd_growth[chosen_enemy]
  for i in range(0,enemy_lvl):
    enemy_def += enemies_def_growth[chosen_enemy]
  for i in range(0,enemy_lvl):
    enemy_hp += enemies_hp_growth[chosen_enemy]



def hunt(enemy,quest):
  if enemy == -1:
    battleinit(-1)
  else:
    battleinit(enemy)
  hp = mhp
  global exp
  global lvl
  global gold
  global statpoints
  global enemy_name
  global enemy_atk
  global enemy_def
  global enemy_spd
  global enemy_hp
  global enemy_lvl
  global enemy_acc
  global inventory
  global itemnames
  global itemheals
  global enemy_expfloor
  global chosen_enemy

  #Passive rates for Classes
  if c_id == 0:
    critrate = 85
  else:
    critrate = 95
  if c_id == 3:
    gold_multiplier = 1.5
  else:
    gold_multiplier = 1
  
  if c_id == 5:
    dmg_multiplier = 1.5
  else:
    dmg_multiplier = 1
  
  #First Strikes for classes
  if c_id == 4:
    bullet_dmg = int(enemy_hp / 5) + 1
    input(f"First Bullet Strike deals {bullet_dmg} damage!")
    enemy_hp -= bullet_dmg
  
  guard_def = 0
  input(f"{enemy_name} draws near!")
  if spd <= enemy_spd:
    input(f"The {enemy_name} is faster than you!")
  while True:
    #Class Turn Passives
    if c_id == 2 and hp < mhp:
        healing = int(mhp / 20)
        if healing == 0:
            healing = 1
        hp += healing
        input(f"Healed {healing} hp")
    elif c_id == 7:
        spider_dmg = int(enemy_hp / 40) + 1
        input(f"Spiders deal {spider_dmg} damage")
        enemy_hp -= spider_dmg
    elif c_id == 6:
        undead_dmg = 10 - enemy_def
        if undead_dmg < 1:
            undead_dmg = 1
        input(f"The Undead deals {undead_dmg} damage")
        enemy_hp -= undead_dmg
    menu = f"""
you {hp}/{mhp}                           {enemy_hp} enemy
  1.Attack
  2.Guard
  3.Items
  4.Spells
  5.Skills
  6.Run"""
    os.system('cls')
    img.enemy_img(chosen_enemy)
    if spd > enemy_spd:
      #player phase
      guard_def = 0
      print(menu)
      command = input("")
      if command == "1":
        dmg = atk + weapon_atk[equip] - enemy_def
        if dmg <= 0:
          dmg = 1
        if spd + weapon_spd[equip] > enemy_spd + 6:
          dmg *= 2
          print("Attacked twice!")
        rnroll = random.randint(0,101)
        if rnroll <= weapon_acc[equip] - (enemy_spd / 2):
          rnroll = random.randint(0,101)
          if rnroll >= critrate:
            dmg *= 3
            print("Critical hit!")
          dmg = int(dmg * dmg_multiplier)
          input(f"Dealt {dmg} damage to the {enemy_name}")
          enemy_hp -= dmg
        else:
          input("Missed!")
      elif command == "2":
        guard_def = defence / 2
        input("Guarding.")
      elif command == "3":
        for i in range(0,len(inventory)):
          print(f"{i+1}. {itemnames[inventory[i]]}")
        iteminput = input("")
        iteminput = int(iteminput)
        inventory.pop(iteminput-1)
        hp += itemheals[iteminput-1]
        if hp > mhp:
          hp = mhp
        os.system('cls')
        img.enemy_img(chosen_enemy)
        print(menu)
        input(f"Healed {itemheals[iteminput]} hp")
      elif command == "4":
        enemy_hp -= spell.spellsload(lvl,atk,c_id,enemy_def) - (enemy_def/2)
      elif command == "5":
        input(p_skill_name[c_id])
      elif command == "6":  
        rnroll = random.randint(0,101)
        if rnroll <= 75:
          escapeloss = int(gold * 0.1)
          gold -= escapeloss
          input(f"Escaped successfully. Lost {escapeloss} gold...")
          break
        else:
          input("Failed to escape!")
      else:
        input("Skipping turn...")
      
      if enemy_hp <= 0:
        os.system('cls')
        img.enemy_img(chosen_enemy)
        print("You win! You earned:")
        rnroll = int(random.randint(0,enemies_goldceiling[chosen_enemy]+41) * gold_multiplier)
        if quest == 0:
          gold += rnroll
          print(f"{rnroll} gold")
        rnroll = random.randint(enemy_expfloor,100)
        exp += rnroll
        print(f"{rnroll} exp")
        input("")
        if exp >= 100:
          exp -= 100
          lvl += 1
          statpoints += statadd
          input("LEVEL UP")
          statallocate()
          spelllevel(lvl, c_id)
        break

      #enemy phase
      dmg = enemy_atk - guard_def - defence
      if dmg <= 0:
        dmg = 1
      if enemy_spd > spd + weapon_spd[equip] + 6:
        dmg *= 2
        print("Attacked twice!")
      rnroll = random.randint(0,101)
      if rnroll <= enemy_acc - (spd / 2):
        if rnroll >= 95:
            dmg *= 3
            print("Critical hit!")
        dmg = int(dmg * dmg_multiplier)
        hp -= dmg
        input(f"{enemy_name} dealt {dmg} damage")
      else:
        input(f"{enemy_name} missed!")
      
      if hp <= 0:
        input("GAME OVER")
        sys.exit()

    else:
      
      print("")
      #enemy phase
      dmg = enemy_atk - guard_def - defence
      if dmg <= 0:
        dmg = 1
      if enemy_spd > spd + weapon_spd[equip] + 6:
        dmg *= 2
        print("Attacked twice!")
      rnroll = random.randint(0,101)
      if rnroll <= enemy_acc - (spd / 2):
        if rnroll >= 95:
            dmg *= 3
            print("Critical hit!")
        dmg = int(dmg * dmg_multiplier)
        hp -= dmg
        input(f"{enemy_name} dealt {dmg} damage")
      else:
        input(f"{enemy_name} missed!")
      
      if hp <= 0:
        input("GAME OVER")
        sys.exit()
      
      menu = f"""
you {hp}/{mhp}                           {enemy_hp} enemy
  1.Attack
  2.Guard
  3.Items
  4.Spells
  5.Skills
  6.Run"""
      #player phase
      guard_def = 0
      print(menu)
      command = input("")
      if command == "1":
        dmg = atk + weapon_atk[equip] - enemy_def
        if dmg <= 0:
          dmg = 1
        if spd + weapon_spd[equip] > enemy_spd + 6:
          dmg *= 2
          print("Attacked twice!")
        rnroll = random.randint(0,101)
        if rnroll <= weapon_acc[equip] - (enemy_spd / 2):
          rnroll = random.randint(0,101)
          if rnroll >= critrate:
            dmg *= 3
            print("Critical hit!")
          dmg = int(dmg * dmg_multiplier)
          input(f"Dealt {dmg} damage to the {enemy_name}")
          enemy_hp -= dmg
        else:
          input("Missed!")
      elif command == "2":
        guard_def = defence / 2
        input("Guarding.")
      elif command == "3":
        for i in range(0,len(inventory)):
          print(f"{i+1}. {itemnames[inventory[i]]}")
        iteminput = input("")
        iteminput = int(iteminput)
        inventory.pop(iteminput-1)
        hp += itemheals[iteminput-1]
        if hp > mhp:
          hp = mhp
        os.system('cls')
        img.enemy_img(chosen_enemy)
        print(menu)
        input(f"Healed {itemheals[iteminput]} hp")
      elif command == "4":
        enemy_hp -= spell.spellsload(lvl,atk,c_id,enemy_def) - (enemy_def/2)
      elif command == "5":
        input(p_skill_name[c_id])
      elif command == "6":  
        rnroll = random.randint(0,101)
        if rnroll <= 75:
          escapeloss = int(gold * 0.1)
          gold -= escapeloss
          input(f"Escaped successfully. Lost {escapeloss} gold...")
          break
        else:
          input("Failed to escape!")
      else:
        input("Skipping turn...")
      
      if enemy_hp <= 0:
        os.system('cls')
        img.enemy_img(chosen_enemy)
        print("You win! You earned:")
        rnroll = int(random.randint(0,enemies_goldceiling[chosen_enemy]+41) * gold_multiplier)
        if quest == 0:
          gold += rnroll
          print(f"{rnroll} gold")
        rnroll = random.randint(enemy_expfloor,100)
        exp += rnroll
        print(f"{rnroll} exp")
        input("")
        if exp >= 100:
          exp -= 100
          lvl += 1
          statpoints += statadd
          input("LEVEL UP")
          statallocate()
          spelllevel(lvl, c_id)
        break


home()