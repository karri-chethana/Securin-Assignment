'''
Name: Karri Chethana
Register No. : 111620104065
Mail: karr20cs065@rmkcet.ac.in
College: RMK College of Engineering and Technology
'''

#Part 1 (Securein Assignment)

# 1. How many total combinations are possible? Show the math along with the code!

total_combinations = 6 ** 2
print(f"1) Total Combinations: {total_combinations}")
print()


'''2. Calculate and display the distribution of all possible combinations that can be
obtained when rolling both Die A and Die B together. Show the math along with
the code!'''

dice_combinations = [[0] * 6 for _ in range(6)]
distribution_matrix = [[0] * 6 for _ in range(6)]

for i in range(0,6):
    for j in range(0,6):
        dice_combinations[i][j] = (i+1,j+1)
        distribution_matrix[i][j] = i + j + 2  # +2 because faces are numbered from 1 to 6

# Display the All Dice Combinations
print("2) All Dice Combinations")
for row in dice_combinations:
    print(row)
print("\n")

# Display the distribution matrix
print("Distribution matrix of dice")
for row in distribution_matrix:
    print(row)
print("\n")


'''3. Calculate the Probability of all Possible Sums occurring among the number of
combinations from (2).'''

print("3) Probabilities of sums")
for i in range(2, 13):  # Sums can range from 2 to 12
    count = sum(row.count(i) for row in distribution_matrix)
    probability = count / total_combinations
    print(f"P(Sum = {i}) = {probability:.3f}")
