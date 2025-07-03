# Take a string "My name is mairaj and i am 22 years old"
# and print from it int and strings separate
# for example:
# if string character found then show its 
# ("The character abc is string")
# if character is int then first convert in into int from string
# and print ("The character abc is number")
text = "My name is mairaj and i am 22 years old"

for character in text:
    if character.isdigit():
        print(f"The character {int(character)} is int")
    else:
        print(f"The character {character} is string")

