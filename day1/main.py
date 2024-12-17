
right_numbers = []
left_numbers = []

# Read and process the input file
with open("day1/input.txt", "r") as file:
    for line in file:
        # Split the line into two numbers
        numbers = line.split()
        if len(numbers) == 2:
            left_numbers.append(int(numbers[0]))
            right_numbers.append(int(numbers[1]))

# Sort the arrays
left_numbers.sort()
right_numbers.sort()

# Calculate the difference between the arrays at the same index
diff = [abs(left_numbers[i] - right_numbers[i]) for i in range(len(left_numbers))]

# Sum of diff array
sum_diff = sum(diff)

print("Total distance between the lists:", sum_diff)

#part 2 list left * occureancy in list right
# Create a dictionary to store the counts of each number in the right list
right_counts = {}
for number in right_numbers:
    right_counts[number] = right_counts.get(number, 0) + 1

# Calculate the similarity score
similarity_score = 0
for number in left_numbers:
    similarity_score += number * right_counts.get(number, 0)

print("Total similarity score:", similarity_score)