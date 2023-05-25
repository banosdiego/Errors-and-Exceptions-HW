#Write a function that asks for an integer and prints the square of it. 
#Use a while loop with a try, except, else block to account for incorrect inputs.

def ask():
    while True:
        try:
            data = int(input("Please enter an integer: "))
            print (data**2)
        except:
            print("Please enter a number!")
        else:
            break


ask()