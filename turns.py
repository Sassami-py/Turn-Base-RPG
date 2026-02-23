import random
#just to explain the variable names: 'p' is for Player and 'e' is for Enemy
hp_p, hp_e = int(100), int(100)
cure_p, cure_e = int(10), int(10)
def_p, def_e = int(10), int(10)
#atk it's Attack, 'b' for basic and 'c' for critical
atk_b, atk_c = int(20), int(30)

#just for fun, here we get the name of player and Enemy!
player = input("Insert a hero name: ").upper()
enemy = input("\nInsert the villain name: ").upper()

shield_p, shield_e = False, False

print ("Battle Start!\n")
#Start the loop, while no one was defeated, the battle continues!
while hp_p > 0 and hp_e > 0:
  #Defining the order of attack
  if random.randint(1, 10) > 5:
      first, second = "Player", "Enemy"
  else:
      first, second = "Enemy", "Player"
  
  order = [first, second]

  for turn in order:
    if hp_p <= 0 or hp_e <= 0:
      break
    #Now, we start with the actions that player can do!
    if turn == "Player":
      #reset the shield!
      shield_p = False
      print (player,"turn!\n")
      act = input("\nChose your action: ATK, DEF, CURE: ").upper()
      #first action, when he tried to attack!
      if act == "ATK":
        #in this case, enemy have a shield!
        if shield_e == True:
          print ( enemy, "is protected!\n")
        else:
          #if don't have shield, you can attack him!
          atk = random.randint(atk_b, atk_c)
          hp_e -= atk
          print ("Your attack deal", atk, "damage! The enemy life is", hp_e,"\n")
      #if you choose to defend yourself!
      elif act == "DEF":
        if def_p > 0:
         shield_p = True
         def_p -= 1
         print (player,"is protected! You have",def_p,"shields left!\n")
        else:
          print (player,"can't defend!\n")
          continue
      elif act == "CURE":
        if cure_p >= 0:
          hp_p += cure_p
          cure_p -= 1
          print (player,"use cure! The new life is",hp_p,"\n")
      else:
        #just for don't break if your not choose some valid action!
        print ("Invalid action!\n")
        continue
    else:
      #now enemy's turn!
      print (enemy,"Turn!\n")
      shield_e = False
      #Here a system that, he have a chance to use a shield or attack!
      if hp_e >= 20:
        act_e = random.randint(1, 10)
        if act_e > 5:
          atk = random.randint(atk_b, atk_c)
          if shield_p == True:
            print (enemy,"attack!",player,"is protected!\n")
          else:
           hp_p -= atk
           print (enemy,"attack!",player,"'s new life is:",hp_p,"\n")
        else:
          if def_e > 0:
            shield_e = True
            def_e -= 1
            print (enemy,"is protected! He have",def_e,"shilds left!\n")
          else:
            print (enemy,"can't defend!\n")
            continue
      else:
        #a classic, wen the life it's about to end, he cure!
        if cure_e > 0:
          hp_e += cure_e
          cure_e -= 1
          print (enemy,"use cure! The new life is",hp_e,"\n")
if hp_e <= 0:
  #just a victory menssage!
  print (player,"Victory!")
elif hp_p <= 0:
  print (enemy,"Victory!")
