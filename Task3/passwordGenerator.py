import random
import string
print("Welcome to our Random Password Generator")
def main():
    length=int(input("Enter the length of password you want:"))
    Lower_D = string.ascii_lowercase
    Upper_D = string.ascii_uppercase
    Digit_D = string.digits
    Symbols_D = string.punctuation
    Normal_D = string.ascii_letters
    combine=Lower_D + Upper_D + Digit_D + Symbols_D + Normal_D
    password=random.sample(combine,length)
    passWord = "".join(password)
    print(passWord)
    main()
main()

