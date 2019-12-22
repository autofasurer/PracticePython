#! /usr/bin/env python3

from datetime import datetime

def main():

    #FUNCTION TAKES AGE OF USER AND CALCULATES YEAR HE/SHE TURNS 100 USING
    #THE CURRENT YEAR AS REFERENCE.
    def whenhundred(age):
        thisyear = datetime.now().year
        hundredinyear = 100 - age + thisyear
        return(hundredinyear)


    def getage():
        try:
            age = int(input("What's your age?\n"))
            return age
        except:
            print("Please type a number for your age!\n")
            return getage()


    #ASK THE NAME AND THE AGE:
    name = input("What's your name?\n")
    age = getage()

    #PRINT WELCOME MESSAGE AND CALCULATE WHEN THE USER WILL TURN 100
    print(f"Hi, {name}, you are currently {age} years old...")
    hundred = whenhundred(age)
    print(f"You'll turn hundred years old in the year {hundred}!")


if __name__ == '__main__':
    main()
