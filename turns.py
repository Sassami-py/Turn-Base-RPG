import random

class Character:
  def __init__(self, name, hp, cure, shield):
    self.name = name
    self.hp = hp
    self.cure = cure
    self.shield = shield
    self.block = False

  def attack(self,target):
    damage=random.randint(20,40)
    if target.block == True:
      print (f"{target.name} is protected!\n")
      target.block = False
    else:
      target.hp -= damage
      print (f"{self.name} attack! {target.name}'s new life is: {target.hp}\n")
  
  def defend(self):
    if self.shield > 0:
      self.block = True
      self.shield -= 1
      print (f"{self.name} used a shield! Are {self.shield} shields left!\n")
    else:
      print (f"{self.name} can't block!\n")
  
  def healing(self):
    if self.cure > 0:
      self.hp += 10
      self.cure -= 1
      print(f"{self.name} use a cure, the new hp is {self.hp}\n")
    else:
      print(f"{self.name} can't heal!\n")


player = input("Insert a hero name: ").upper()
enemy = input("\nInsert the villain name: \n").upper()

hero = Character(player, 100, 4, 4)
villain = Character(enemy, 100, 4, 4)

print ("Battle Start!\n")

while hero.hp > 0 and villain.hp > 0:

  if random.randint(1, 10) > 5:
      order = [hero, villain]
  else:
      order = [villain, hero]

  for turn in order:
    if hero.hp <= 0 or villain.hp <= 0:
      break

    print(f"--- {turn.name}'s turn ---\n")

    if turn == hero:
      action = input("Choose your action: [A] for attack, [D] for deffense or [H] for heal: \n").upper()
      if action == 'A':
        hero.attack(villain)
      elif action == 'D':
        hero.defend()
      elif action == 'H':
        hero.healing()
      else:
        print('Invalid action, use A, D or H!\n')
    else:
     if villain.hp > 20:
      action = random.randint (0,10)
      if action >= 3:
        villain.attack(hero)
      else:
        villain.defend()
     else:
      villain.healing()

if villain.hp <= 0:
  print (f"{hero.name} win!")
elif hero.hp <= 0:
  print (f"{villain.name} win!")
