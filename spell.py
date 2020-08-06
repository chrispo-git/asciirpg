import random

def spellsload(lvl,atk):
  fire_spell = False
  thunder_spell = False
  death_spell = False
  if lvl < 6:
    input("No spells")
    return 0
  print("--------------------------------------------------------")
  if lvl > 5:
    print("1.Flame - deals 10 dmg to enemy")
  if lvl > 15:
    print("2.Thunderstrike - deals 15 dmg to enemy")
  if lvl > 25:
    print("3.Death - deals 25 dmg to enemy, low chance of death")
  spellinput = input("")
  if spellinput == "1" and lvl > 5:
    input(f"Flame deals {10+atk}")
    return 10 + atk
  if spellinput == "2" and lvl > 15:
    input(f"Thunderstrike deals {15+atk}")
    return 15 + atk
  if spellinput == "3" and lvl > 25:
    input(f"Death deals {25+atk}")
    death = random.randint(0,101)
    if death > 90:
      return 999
    else:
      return 25 + atk
  else:
    return 0
  
def spelllevel(lvl):
  if lvl == 6:
    input("You learned Flame! Use it in spells")
  if lvl == 16:
    input("You learned Thunderstrike!")
  if lvl == 26:
    input("You learned Death!")
