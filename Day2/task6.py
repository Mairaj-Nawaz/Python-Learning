# Take a string and count how many strings are in it ,
# how many int in string
# and show the final count
 
text = "my name is mairaj i am 22 years old"
string_count = 0
int_count = 0
for character in text:
    if character.isdigit():
        print(f"the character {character} is a integer and appears {len(character)} times")
        int_count+=1
    
    else:
        print(f"the character {character} is a string and appears {len(character)} times")
        string_count+=1
    # count += 1

print("String count is ", string_count)    
print("Int count is ", int_count)    