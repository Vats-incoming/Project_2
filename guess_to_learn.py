import random
import emoji
import time
def reward():
  r=random.randint(11,20)
  time.sleep(5)
  print(f"The Multiplication table of {r}:\n")
  for i in range(1,11):
    print(f"{r} x {i} = {r*i}\n")
  print("I know you may have forgotten this so just a quick revision as a reward \U0001F3C6 \n ")
  print("===========================Thank You for playing=================================== \n \n \n ")
'''def correct_guess():
    if n==comp:
     print("Congratulations! You have guessed it right \U0001F60D 	")
def small_guess():
    if n>comp:
     print(f"Please select a smaller number than {n}\n")
def larg_guess():
    if n<comp:
     print(f"Please select a larger number than {n}\n")
def invalid_guess():'''
welcome_msg='''       =================== WELCOME ============================
            ========== GAME RULES ARE==========
      \U0001F449A number between 0 to 100 will be randomly choosen by the computer & You need to guess it
      \U0001F449Guess it as fast as you can to beat the highscore 
      \U0001F449Guess it correctly & get rewarded \U0001F3C6'''
print(welcome_msg)
comp=random.randint(0,100)
time.sleep(5)
print("\U0001F607 A number has been randomly selected by the computer \U0001F607")
print("Now its your turn")
count=0
while(True):
  count+=1
  n=int(input(" Please guess a number\n"))
  if n==comp:
    print("Congratulations! \U0001F973 You have guessed it right \U0001F973	 ")
    print(f"You took {count} chances to guess correctly")
    with open("hiscore_guess.txt","r") as f:
     cont=f.read()
    if count<int(cont):
     print("You have made a high score")
     with open("hiscore_guess.txt","w") as f:
      f.write(str(count))
      print("Your reward \U0001F3C6 is : \n")
      reward()
     exit()
    else:
     print("Oops! You did'nt beat the highscore but you will be rewarded \U0001F3C6 \n")
     reward()
     exit()
  elif n>comp:
    print(f" \U0001F61F Select a smaller number than {n} \U0001F61F  ")
  elif n<comp:
    print(f" \U0001F626 Select a larger number than {n} \U0001F626 ")
  else:
    print("Sorry! Invalid input")


