# Each day, the monkey eats one more banana than the previous day, starting with 
# 2 bananas on Monday.
# Calculate how many bananas it eats over 7 days also print each days banana.

# Example expected output: Total bananas eaten in 7 days: 35 
# (or whatever the correct calculation is)



count = 1
total_count = 0

for i in range(7):
    count += 1 
    total_count += count
print("Total bananas eaten in a week: ", total_count)