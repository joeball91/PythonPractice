from os import system

bids = {}

def add_bid(name, price):
    new_bid = {}
    new_bid[name] = price
    bids.update(new_bid)

notFinished = False
while not notFinished:
    name = input("What is your name? ")
    price = int(input("How much do you bid? "))
    add_bid(name,price) 
    
    finish = input("Is there another bid? Type 'yes' or 'no': ")
    if finish == 'yes':
        system("clear")
    else: 
        notFinished = True
        system("clear")

high = 0
for bidder in bids:
    if bids[bidder] > high:
        high = bids[bidder]
        winner = bidder

print(f"The winner is {winner}!")