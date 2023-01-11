import random

def Pass_Generator(Length):
    character = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmnopqrstuvwxyz!@#$%^&*()"
    GeneratedPassword = []
    for x in range(Length):
        GeneratedPassword.append(random.choice(character))
    NewPassword = ''.join(map(str, GeneratedPassword))
    return NewPassword
        


print("Hello! Let's generate a password !")
Length = int(input("How long would you like your password to be? \n"))
password = Pass_Generator(8)
print("This is your new password: ", password)

