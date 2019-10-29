TEMP = 1
while TEMP == 1:
    NOG = 0
    TEMP = 0
    STOP = 0
    NTG = int(input("Please enter your number Player One"))
    if NTG >= 1 and NTG <= 10:
        while NOG <= 5 and STOP == 0:
            G = int(input("Please enter your guess Player Two"))
            N = NOG
            NOG = N + 1
            if G == NTG:
                print("Your guess is correct")
                print("Player Two wins")
                STOP = 1
                T = int(input("Would you like to play another game? 1 for yes 2 for no"))
                if T == 1:
                    TEMP = 1
                else:
                    TEMP = 0
        if STOP == 0:
            print("You have had too many guesses")
            print("Player One wins")
            T = int(input("Would you like to play another game? 1 for yes 2 for no"))
        else:
            if T == 1:
                TEMP = 1
            else:
                TEMP = 0
    else:
        print("invalid number")
        T = int(input("Would you like to play another game? 1 for yes 2 for no"))
        if T == 1:
            TEMP = 1
        else:

            TEMP = 0
        
            
