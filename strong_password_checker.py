#Function that check if a given password is strong or weak. Return True if strong, returns False if weak.
def strong_password(password):
    specialChar = ['!','@','#','$','%','*','&']
    numbers = ['0','1','2','3','4','5','6','7','8','9']
    numbersCount = 0
    specialCount = 0
    for x in password:
        if x in specialChar:
            specialCount += 1
            specialChar.pop(specialChar.index(x))
        if x in numbers:
            numbersCount += 1
            numbers.pop(numbers.index(x))
    if len(password) >= 10 and numbersCount >= 3 and specialCount >= 3:
        return True
    else:
        return False

def main():
    my_password = input("Test your password: ")
    if strong_password(my_password) == True:
        print("You got a strong password")
    else:
        print("You got at weak password")
if __name__ == "__main__":
    main()