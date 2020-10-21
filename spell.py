import random

p_mag_class_id = [1, 2, 6, 7]
p_spell_mod = [0, -5, -2]

white_venom = 5


def spellsload(lvl,atk,c_id,enemy_def):
  spells = []
  spells_desc = []
  spells_dmg = []
  fire_spell = False
  thunder_spell = False
  death_spell = False
  if c_id in p_mag_class_id:

      print("--------------------------------------------------------")
      if lvl > 5 or c_id == 1:
        spells_desc.append("Flame - deals 8 dmg to enemy")
        spells.append("Flame")
        spells_dmg.append(8)
      if lvl > 15:
        spells_desc.append("Thunderstrike - deals 15 dmg to enemy")
        spells.append("Thunderstrike")
        spells_dmg.append(15)
      if c_id == 6:
        spells_desc.append("Death - deals 5 dmg to enemy, low chance of instant death")
        spells.append("Death")
        spells_dmg.append(5)
      if c_id == 2:
        spells_desc.append("Lightning Knuckles - deals 8 dmg to enemy")
        spells.append("Lightning Knuckles")
        spells_dmg.append(8)
      if c_id == 1 and lvl > 10:
        spells_desc.append("FlashFire - deals 13 dmg to enemy")
        spells.append("FlashFire")
        spells_dmg.append(13)
      if c_id == 7:
        spells_desc.append("Arachna - deals 10 dmg to enemy")
        spells.append("Arachna")
        spells_dmg.append(10)
      if c_id == 7 and lvl > 7:
        spells_desc.append("White Venom - deals 5 dmg to enemy, increases with each use")
        spells.append("White Venom")
        white_venom += 1
        spells_dmg.append(white_venom)
      if c_id == 2 and lvl > 16:
        spells_desc.append("Vital Strike - deals 14 dmg to enemy, low chance of instant death")
        spells.append("Vital Strike")
        spells_dmg.append(14)
      if c_id == 6 and lvl > 10:
        spells_desc.append("Soul Burn - deals 10 dmg to enemy, medium chance of instant death")
        spells.append("Soul Burn")
        spells_dmg.append(8)
      if len(spells) == 0:
        input("No spells learnt yet")
        return 0
      for i in range(0,len(spells)):
        print(f"{i}.{spells_desc[i]}")
      try:
        spellinput = int(input(""))
      except ValueError:
        spellinput = 0
      try:
        input(f"{spells[spellinput]} did {spells_dmg[spellinput]-(enemy_def/2)} damage")
      except IndexError:
        spellinput = 0
        input(f"{spells[spellinput]} did {spells_dmg[spellinput]-(enemy_def/2)} damage")
      if spells[spellinput] == "Death":
        death = random.randint(0,101)
        if death > 80:
          input("Death has activated")
          return 999
        else:
          return spells_dmg[spellinput] + atk
      elif spells[spellinput] == "Vital Strike":
        death = random.randint(0,101)
        if death > 90:
          input("Vital Strike has activated")
          return 999
        else:
          return spells_dmg[spellinput] + atk
      elif spells[spellinput] == "Soul Burn":
        death = random.randint(0,101)
        if death > 55:
          input("Soul Burn has activated")
          return 999
        else:
          return spells_dmg[spellinput] + atk
      else:
        return spells_dmg[spellinput]
      
  
def spelllevel(lvl,c_id):
  if c_id in p_mag_class_id:
      if lvl == 6:
        input("You learned Flame! Use it in spells")
      if lvl == 16:
        input("You learned Thunderstrike!")
      if lvl == 26:
        input("You learned Death!")
