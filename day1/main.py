left_numbers=[]
right_numbers=[]
with open("day1\input.txt") as file:
    for line in file:
         # Split the line into two numbers
        numbers = line.split()
        if len(numbers) == 2:
            left_numbers.append(int(numbers[0]))
            right_numbers.append(int(numbers[1]))

#sort the arrays
left_numbers.sort()
right_numbers.sort()
print(left_numbers)
# calculate the difference between the arrays in same index
diff = [abs(left_numbers[i] - right_numbers[i]) for i in range(len(left_numbers))]

#sum of diff array
sum_diff = sum(diff)

print(sum_diff)
