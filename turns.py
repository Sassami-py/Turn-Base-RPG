import random

HPP, HPI = int(100), int(100)
cureP, cureI = int(10), int(10)
DefP, DefI = int(10), int(10)
Att1, Att2 = int(20), int(30)

StateP, StateI = False, False

print ("Battle Start!")

while HPP > 0 and HPI > 0:
  if random.randint(1, 10) > 5:
      first, second = "Player", "Enemy"
  else:
      first, second = "Enemy", "Player"
  
  order = [first, second]

  for turn in order:
    if HPP <= 0 or HPI <= 0:
      break
    
    if turn == "Player":
      StateP = False
      act = input("Chose your action: ATK, DEF, CURE: ")
      if act == "ATK":
        if StateI == True:
          print ("Enemy is protected!")
        else:
          atk = random.randint(Att1, Att2)
          HPI -= atk
          print ("Your attack deal", atk, "damage! The enemy life is", HPI)
      elif act == "DEF":
        if DefP >= 0:
         StateP = True
         DefP -= 1
         print ("Player is protected!")
        else:
          print ("Player can't defend!")
          continue
      elif act == "CURE":
        if cureP >= 0:
          HPP += cureP
          cureP -= 1
          print ("Player use cure! The new life is",HPP)
      else:
        print ("Invalid action!")
        continue
    else:
      print ("Enemy Turn!")
      StateI = False
      if HPI >= 20:
        actI = random.randint(1, 10)
        if actI > 5:
          atk = random.randint(Att1, Att2)
          if StateP == True:
            print ("Enemy attack! Player is protected!")
          else:
           HPP -= atk
           print ("Enemy attack! Player's new life is:",HPP)
        else:
          if DefI >= 0:
            StateI = True
            DefI -= 1
            print ("Enemy is protected!")
          else:
            print ("Enemy can't defend!")
            continue
      else:
        if cureI >= 0:
          HPI += cureI
          cureI -= 1
          print ("Enemy use cure! The new life is",HPI)
        else:
          actI = random.randint(1, 10)
        if actI > 5:
          atk = random.randint(Att1, Att2)
          if StateP == True:
            print ("Enemy attack! Player is protected!")
          else:
           HPP -= atk
           print ("Enemy attack! Player's new life is:",HPP)
        else:
          if DefI >= 0:
            StateI = True
            DefI -= 1
            print ("Enemy is protected!")
          else:
            print ("Enemy can't defend!")
            continue
if HPI <= 0:
  print ("Player Victory!")
elif HPP <= 0:
  print ("Enemy Victory!")
