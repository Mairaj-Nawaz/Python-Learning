# Take a string from user "Ali love javeria and he love himself......"
# and check that love is in string or not if found print found
# and also show how many times love appears 

# hint:you can check directly from condition (if love in text:)



text = "ali loves javeria and he also loves himself ....."
count = 0

if "loves" in text:
        print("string loves is in the given text")
else:
        print("invalid text")

word_count = text.count("loves")
print(word_count)