import random

c_quest_name = [
  "Collect herbs",
  "Bring a Silver wolf corpse",
  "Bring a red slime core"
]
c_quest_price = [
  100,
  400,
  550
]
c_quest_enemy_num = [
  -1,
  5,
  4,
]
b_quest_name = [
  "Escort a Merchant",
  "Destroy a bat's nest",
  "Bring a green slime core"
]
b_quest_price = [
  1000,
  1300,
  900
]
b_quest_enemy_num = [
  6,
  7,
  8
]


a_quest_name = [
  "Kill a Wyvern terrorizing a town",
  "Destroy a bandit group",
  "Escort a rich Merchant"
]

a_quest_price = [
  8000,
  5000,
  6000
]

merchant = 0

a_quest_enemy_num = [
  9,
  6,
  merchant
]
def quests(q):
  merchant = random.randint(3,6)
  global questlvl
  questlvl = q
  questlvl += 1
  if questlvl == 5:
    input("You are now B rank")
  if questlvl == 10:
    input("You are now A rank")
  if questlvl < 5:
    for i in range(0,len(c_quest_name)):
      print(str(i+1) + ". " + c_quest_name[i] +  " - " + str(c_quest_price[i]))
  if questlvl < 10 and questlvl > 4:
    for i in range(0,len(b_quest_name)):
      print(str(i+1) + ". " + b_quest_name[i] +  " - " + str(b_quest_price[i]))
  if questlvl > 9:
    for i in range(0,len(a_quest_name)):
      print(str(i+1) + ". " + a_quest_name[i] +  " - " + str(a_quest_price[i]))
  if questlvl < 10:
    print(f"Quests until guild rank A: {10-questlvl}")
  questinput = input("")
  try:
    questinput = int(questinput)
  except ValueError:
    questlist = [0,-1]
    questlist.append(questlvl)
    return questlist
  questinput -= 1
  questlist = []
  try:
    if questlvl < 5:
      questlist.append(c_quest_price[questinput])
      questlist.append(c_quest_enemy_num[questinput])
    if questlvl > 9:
      questlist.append(a_quest_price[questinput])
      questlist.append(a_quest_enemy_num[questinput])
    if questlvl < 10 and questlvl > 4:
      questlist.append(b_quest_price[questinput])
      questlist.append(b_quest_enemy_num[questinput])
  except IndexError:
    questlist = [0,-1]
  questlist.append(questlvl)
  return questlist
