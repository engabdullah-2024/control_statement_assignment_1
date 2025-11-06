# 1.Write a Python program that asks the user to enter a number
# and prints whether the number is positive, negative, or zero.

# # This program asks the user to enter a number
# Then it checks whether the number is positive, negative, or zero.

# Step 1: Ask the user to enter a number
number = float(input("Enter a number: "))

# Step 2: Check if the number is positive
if number > 0:
    print("The number is positive.")

# Step 3: Check if the number is negative
elif number < 0:
    print("The number is negative.")

# Step 4: If the number is not positive or negative, it must be zero
else:
    print("The number is zero.")











# 2. Write a Python program that asks the user for their exam score
# (0–100) and prints their grade based on the following scale:
# 90–100 → "A“
# 80–89 → "B“
# 70–79 → "C“
# 60–69 → "D“
# 0–59 → "F“

grade = int(input('Enter grade : '))

if grade >= 90 :
    print('A')
elif grade >= 80:
    print('B')
elif grade >= 70 :
    print('C')
elif grade >=60 :
    print('D')

else:
    print('F')
