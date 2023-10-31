import random


def password_generator(password_length):
    alphabets = "abcdefghijklmnopqrstuvwxyz"
    passwords = []

    for length in password_length:
        new_password = ""

        for _ in range(length):
            next_letter_at_index = random.randrange(len(alphabets))
            new_password = new_password + alphabets[next_letter_at_index]

        new_password = replaceWithNumber(new_password)
        new_password = replaceWithUpperCaseLetter(new_password)
        passwords.append(new_password)

    return passwords


def replaceWithNumber(pword):
    for _ in range(random.randrange(1, 3)):
        replace_index = random.randrange(len(pword) // 2)
        pword = pword[0:replace_index] + str(random.randrange(10)) + pword[replace_index + 1:]
    return pword


def replaceWithUpperCaseLetter(pword):
    for _ in range(random.randrange(1, 3)):
        replace_index = random.randrange(len(pword) // 2, len(pword))
        pword = pword[0:replace_index] + pword[replace_index].upper() + pword[replace_index + 1:]
    return pword


def main():
    numberOfPasswords = int(input("How many passwords do you want to generate? "))
    print("Generating " + str(numberOfPasswords) + " passwords.")
    lengthOfPasswords = []

    print("The length of the password should be less than or equal to three.")

    for i in range(numberOfPasswords):
        length = int(input("Enter the length of Password #" + str(i + 1) + " "))
        if length < 3:
            length = 3
        lengthOfPasswords.append(length)

    passwords = password_generator(lengthOfPasswords)

    for i in range(numberOfPasswords):
        print("Password #" + str(i + 1) + " = " + passwords[i])


if __name__ == "__main__":
    main()




