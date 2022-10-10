import time
    
def Ask_For_Last_Digit():
    """Asks the person for their phones last number until correct number
    given."""
    
    while True:
        try:
            last = int(input("\nEnter the last digit of your phone number: "))
            result = []
            for num in str(last):
                result.append(num)
            
        except ValueError:
            print("\nWhat kind of last number is that?!?")
            print("Here! Try again!")
            continue
        if len(result) > 1:
            print("\nThis number is too long to be a last digit.")
            print("Try Again! Enter only your last digit!")
            continue
        
        else:
            print("\nAWESOME!")
            print("Now I would need your birth year.")
            return last
            
def Ask_For_Birth_Year():
    """Asks the person for their birth year."""
    while True:
        try:
            birth = int(input("\nEnter the year you were born in: "))
            result = []
            for num in str(birth):
                result.append(num)
        except ValueError:
            print("\nThis is a very strange birth year.")
            print("Try Again!")
            continue
        if len(result) > 4 or birth > 2020:
            print("\nWOW! Were you born in the future?")
            print("Here! Try again!")
            continue
        elif len(result) < 4:
            print("\nYou must be dead by now if you were born in this year!")
            print("Why not give it another try?")
            continue
        elif birth <= 1898:
            print("\nYou are too old to be taking this age test!")
            print("Give it to another person who is younger than you!")
            print("Here! Try Again!")
            continue
        else:
            print("\nGREAT!")
            print("Now I can finally calculate your age.")
            return birth
        
def Calculation_Procedure(last_digit, birth_year):
    """Uses your last_digit to get your age."""
    multiply2 = last_digit * 2
    print("\nStep-1 ==> Multiplying your phone's last number by 2...")
    time.sleep(3)
    print("\nDone!")
    print("{} x 2 = {}".format(last_digit, multiply2))
    
    add5 = multiply2 + 5
    print("\nStep-2 ==> Adding 5 to the number we just got...")
    time.sleep(3)
    print("\nDone!")
    print("{} + 5 = {}".format(multiply2, add5))
    
    multiply50 = add5 * 50
    print("\nStep-3 ==> Multiplying the number we got with 50...")
    time.sleep(3)
    print("\nDone!")
    print("{} x 50 = {}".format(add5, multiply50))
    
    add1770 = multiply50 + 1770
    print("\nStep-4 ==> Adding 1770 to the number we just got...")
    time.sleep(3)
    print("\nDone!")
    print("{} + 1770 = {}".format(multiply50, add1770))
    
    final = add1770 - birth_year
    print("\nStep-5 ==> Subtracting your birth year from the number we got...")
    time.sleep(3)
    print("\nDone!")
    print("{} - {} = {}".format(add1770, birth_year, final))
    time.sleep(4)
    
    print("\nNow we got {} as our final number.".format(final))
    print("The number is 3 digits long!")
    final = str(final)
    print("\nThe first digit of {} is {}.".format(final, final[0]))
    print("This is your phones last number!!!")
    time.sleep(2)
    print("\nThe last two digits of {} are {}!".format(final, final[1:]))
    print("\n{} IS YOUR AGE!!!".format(final[1:]))
    time.sleep(3)
    
    print("\n")
    print("\n")
    print("\n")
    print("Thank You For Using Magic Age!!!")
          

def Magic_Age():
    """Tells your age using the last digit of your phone number."""
    last_digit = Ask_For_Last_Digit()
    birth_year = Ask_For_Birth_Year()
    Calculation_Procedure(last_digit, birth_year)
    
    time.sleep(60)
    
Magic_Age()
        
        
        
                     