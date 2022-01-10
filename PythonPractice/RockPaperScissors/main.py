#This rock paper scissors is introductory practice in python as I begin my programming journey. I am also using this as practice to push projects to my Github repository.

import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

ran = random.randint(0,2)
decision = input("\nWhat do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: ")

decision = int(decision)

if decision == 0:
    if ran == 0:
        print(f"\nDraw")
        print(f"\nYou chose rock {rock}")
        print(f"Computer chose rock {rock}\n")
    elif ran  == 1:
        print(f"\nYou lose!")
        print(f"\nYou chose rock {rock}")
        print(f"Computer chose paper {paper}\n")
    else:
        print(f"\nYou win!")
        print(f"\nYou chose rock {rock}")
        print(f"Computer chose scissors {scissors}\n")
elif decision == 1:
    if ran == 0:
        print(f"\nYou win!")
        print(f"\nYou chose paper {paper}")
        print(f"Computer chose rock {rock}\n")
    elif ran  == 1:
        print(f"\nDraw")
        print(f"\nYou chose paper {paper}")
        print(f"Computer chose paper {paper}\n")
    else:
        print(f"\nYou lose!")
        print(f"\nYou chose paper {paper}\n")
        print(f"Computer chose scissors {scissors}\n")
else:
    if ran == 0:
        print(f"\nYou lose!")
        print(f"\nYou chose scissors {scissors}")
        print(f"Computer chose rock {rock}\n")
    elif ran  == 1:
        print(f"\nYou win!")
        print(f"\nYou chose scissors {scissors}")
        print(f"Computer chose paper {paper}\n")
    else:
        print(f"\nDraw")
        print(f"\nYou chose scissors {scissors}")
        print(f"Computer chose scissors {scissors}\n")
