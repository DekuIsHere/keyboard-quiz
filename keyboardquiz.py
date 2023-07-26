#keyboard quiz
import time, colorama, sys, replit
from colorama import Fore, Back
loading = 1
while loading<100:
  print("{}%".format(loading))
  loading+=1
  time.sleep(0.05)
  replit.clear(); 
#title screen 
print (Fore.BLUE + """  _              _                         _               _     
 | |            | |                       | |             (_)    
 | | _____ _   _| |__   ___   __ _ _ __ __| |   __ _ _   _ _ ____
 | |/ / _ \ | | | '_ \ / _ \ / _` | '__/ _` |  / _` | | | | |_  /
 |   <  __/ |_| | |_) | (_) | (_| | | | (_| | | (_| | |_| | |/ / 
 |_|\_\___|\__, |_.__/ \___/ \__,_|_|  \__,_|  \__, |\__,_|_/___|
            __/ |                                 | |            
           |___/                                  |_|            """ + Fore.RESET)
print(Fore.RED + Back.WHITE + ". -------------------------------------------------------------------.\n  [Esc] [F1][F2][F3][F4][F5][F6][F7][F8][F9][F0][F10][F11][F12] o o o \n                                                                      \n  [`][1][2][3][4][5][6][7][8][9][0][-][=][_<_] [I][H][U] [N][/][*][-] \n  [|-][Q][W][E][R][T][Y][U][I][O][P][{][}] | | [D][E][D] [7][8][9]|+| \n  [CAP][A][S][D][F][G][H][J][K][L][;]['][#]|_|           [4][5][6]|_| \n  [^][\][Z][X][C][V][B][N][M][,][.][/] [__^__]    [^]    [1][2][3]| | \n  [ctrl][a][________________________][a][ctrl] [<][V][>] [ 0  ][.]|_| \n`--------------------------------------------------------------------." + Fore.RESET + Back.RESET)
time.sleep(1)
#asks for name
name = input (Fore.GREEN +"whats your name " + Fore.RESET)
time.sleep(1)
print("hi " + name)

#question 1
time.sleep(1)
print("question 1")
time.sleep(0.5)
score = 0
#repeats question until you choose one of the answers
correct_answer = False
while correct_answer == False:
  print(Fore.GREEN +"what is the best switch on a keyboard" + Fore.RESET)
  time.sleep(0.5)
  q = input ("clicky(A) tactile(B) linear(C)").lower()
  if q == "c":
    correct_answer = True
    print("correct you have good tastes " + name)
    score = score + 1
  
  elif q == "a":
    correct_answer = True
    print("wrong it is banned in offices for a reason they are loud and annoying")
  
  elif q == "b":
    correct_answer = True
    print ("wrong your only slightly better than someone that chose clicky switches")

time.sleep(0.5)
print ("next question")
time.sleep(0.5)
#question 2
correct_answer = False
while correct_answer == False:
  print(Fore.GREEN +"what is the most important thing you need when building a keyboard" + Fore.RESET)
  time.sleep(0.5)

  q2 = input("pcb(A) case(B) switches(C) keycaps(D)").lower()

  if q2 == "a":
    correct_answer = True
    print("correct it is the most important part of a keyboard because you need it ")
    score = score + 1

  elif q2 == "b":
    correct_answer = True
    print("wrong the pcb is the most important part of a keyboard because if you had everything else exept the pcb then the  wouldnt work ")
  elif q2 == "c":
    correct_answer = True
    print("wrong the pcb is the most important part of a keyboard because if you       had everything else exept the pcb then the keyboard wouldnt work")
  elif q2 == "d":
    correct_answer = True
    print("wrong the pcb is the most important part of a keyboard because if you had everything else exept the pcb then the  wouldnt work")
#question 3
time.sleep(0.5)
correct_answer = False
while correct_answer == False:
  print(Fore.GREEN +"can you mod a keyboard" + Fore.RESET)
  time.sleep(0.5)
  q3 = input("yes(A) No(B)").lower()

  if q3 == "a":
    correct_answer = True
    print("correct theres are loads of mods you can do to you keyboard like tape mod or bandaid mod ect")
    score = score + 1

  elif q3 == "b":
   correct_answer = True
   print("wrong theres are loads of mods you can do to you keyboard like tape mod or bandaid mod ect")

time.sleep(1)
#question 4
correct_answer = False
while correct_answer == False:
  print(Fore.GREEN +"what does the pcb in a keyboard do" + Fore.RESET)
  time.sleep(0.5)

  q4 = input(" it makes the switches sound better (A) it register key presses (B)").lower()

  if q4 == "a":
   correct_answer = True
   print ("wrong ")

  elif q4 == "b":
   correct_answer = True
   print("correct")
  score = score + 1


time.sleep(1)
#question 5
correct_answer = False
while correct_answer == False:
  print(Fore.GREEN +"what is the actuation force of a chery mx red" + Fore.RESET)
  time.sleep(0.5)

  q5 = input(" 43(A) 68(B) 45(C)").lower()
  
  if q5 == "a":
    correct_answer = True
    print("wrong")

  elif q5 == "b":
    correct_answer = True
    print("wrong ")
  elif q5 == "c":
    correct_answer = True
    print("correct")
    score = score + 1

time.sleep(1)
#question 6
correct_answer = False
while correct_answer == False:
  print(Fore.GREEN +"what are stabilizers" + Fore.RESET)

  time.sleep (0.5)

  q6 = input("it stabliizes longer keys (A) its something to replace a switch (B)").lower()

  if q6 == "a":
    correct_answer = True
    print  ("correct it helps stabilises the longer keys because if you had a space bar without stabs then it would not be right")
    score = score + 1

  elif q6 == "b":
    correct_answer = True
    print ("wrong")
  
time.sleep(1)
#question 7
correct_answer = False
while correct_answer == False:
  print (Fore.GREEN +"how can you make a linear switch sound better " + Fore.RESET)
  time.sleep(0.5)
  q7 = input("\nlubing the switches (A)putting switch film inside the switch(B)\nall of the above (C)").lower()

  if q7 == "a":
    correct_answer = True
    print ("wrong while you can just lube the switches you can also add switch film inside of the switches it can also help reduce rattle from the stem of the switch")


  elif q7 == "b":
    correct_answer = True
    print ("wrong just adding switch film is good to add to your switch you should also lube the switch to make it smoother just dont over lube the switch ")

  elif q7 == "c":
    correct_answer = True
    print ("correct lubing and adding film to the switch makes it smoother and adding switch film reduce rattle it will also make the switch have a deeper press when you press the switch")
    score = score + 1
time.sleep(1)
#question 8
correct_answer = False
while correct_answer == False:
  print (Fore.GREEN +"how much keys are in a 60% keyboard" + Fore.RESET)
  time.sleep(0.5)
  q8 = input("62 (A) 69(B) 55(C)").lower()

  if q8 == "a":
    correct_answer = True
    print ("correct there are 62 keys on a 60% keyboard")
    score = score + 1
 
  elif q8 == "b":
    correct_answer = True
    print ("wrong there are 62 keys on a 60% keyboard")

  elif q8 == "c":
    correct_answer = True
    print ("wrong there are 62 keys on a 60% keyboard")

time.sleep(1)
#question 9
correct_answer = False
while correct_answer == False:
  print (Fore.GREEN +"who invented the QWERTY keyboard layout" + Fore.RESET)
  time.sleep(0.5)
  q9 = input("Linus Torvalds (A) Christopher Latham Sholes (B) Guido van Rossum(C)").lower()

  if q9 == "a":
    correct_answer = True
    print ("wrong he made linux (have you considered trying linux)")
  
  elif q9 == "b":
    correct_answer = True
    print ("correct it was used on typewriters and it was made july 1st 1874")
    score = score + 1
  elif q9 == "c":
    correct_answer = True
    print ("wrong he made python the language this quiz was made in")
  
time.sleep(1)
#question 10
correct_answer = False
while correct_answer == False:
  print (Fore.GREEN +"what is a tenkeyless (TKL) keyboard also known as" + Fore.RESET)
  time.sleep(0.5)
  q9 = input("75% (A) 60% (B) 80% (C)").lower()

  if q9 == "a":
    correct_answer = True
    print ("wrong")
  
  elif q9 == "b":
    correct_answer = True
    print ("wrong")
  
  elif q9 == "c":
    correct_answer = True
    print ("correct")
    score = score + 1
  
time.sleep(1)
#results
print ("your score on this quiz is " +str(score))
print("thanks for playing " + name)