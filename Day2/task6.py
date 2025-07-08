# Take a string and count how many strings are in it ,
# how many int in string
# and show the final count
 
text = "my name is mairaj i am 22 years old"
count = 0
for character in text:
    if character.isdigit():
        print(f"the character {character} is a integer and appears {len(character)} times")
    
    else:
        print(f"the character {character} is a string and appears {len(character)} times")
    count += 1
    
print(count)