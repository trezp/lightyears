__author__ = 'treasureporth'


import random

#chooses a number at random between 10 and 100 in steps of 10.
def random_card():
    rand_num = random.randrange(10, 100, 10)
    return rand_num

print "Welcome to Light Years, or Mille Bornes in SPAAAAAACE! \n" \
      "You're 5 billion years into the future and the sun is about to explode. \n" \
      "Quick, travel 1,000 light years into space before something terrible happens!" \

#When the user types "go", takes random number, adds to a count up to 1,000.
miles = 0

while miles < 1000:
    rando = random.randrange(33,333)
    light_years = random_card()
    miles = light_years + miles
    answer = raw_input("Type 'GO' to draw a mileage card. Type 'QUIT' to give up \n >> ")
    asteroid = "Uh oh, you've hit an asteroid! You're dead. But you traveled %d light years. Good job." % miles
    aliens = "Uh oh, you've been captured and enslaved by aliens. You're dead. But you traveled %d light years. Good job." % miles
    fuel = "Uh oh, you ran out of fuel, languished in empty space for several weeks, and died. But you traveled %d light years. Good job." % miles
    #throws up random roadblocks
    if rando % 15 == 0:
        print asteroid
        break
    elif rando % 25 == 0:
        print aliens
        break
    elif rando % 12 == 0:
        print fuel
        break
    #go button
    if answer.lower() == "go":
        print "You've traveled %d light years, for a total of %d light years!" % (light_years, miles)
    #checks for valid input
    elif answer.lower() != "go":
        print "This is serious, you're about to die!"
    elif answer.lower() == "quit":
        break
    elif miles >= 1000:
        print "Congratulations! You've made it to safety! Well done."
        break