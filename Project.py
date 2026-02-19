# 1.
num = float(input("Enter a number: "))
if num > 0:
    print("The number is positive")
else:
    print("The number is negative")

# 2.
num = float(input("Enter a number: "))
if num > 0:
    print("The number is positive")
elif num < 0:
    print("The number is negative")
else:
    print("The number is zero")

# 3.
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")

# 4.
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))
max_num = a
if b > max_num:
    max_num = b
if c > max_num:
    max_num = c
print("The largest number is:", max_num)

# 5.
day_num = int(input("Enter a number (1-7) for weekdays: "))
days = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
if 1 <= day_num <= 7:
    print("Weekday:", days[day_num - 1])
else:
    print("Invalid number!")

# 6.
day_name = input("Enter the name of the weekday: ")
day_name = day_name.strip()
days_lower = [d.lower() for d in days]
if day_name.lower() in days_lower:
    print("Day number:", days_lower.index(day_name.lower()) + 1)
else:
    print("Invalid weekday name!")

# 7.
score = float(input("Enter student's score: "))
if 14 <= score < 16:
    print("Grade: C")
elif 16 <= score < 18:
    print("Grade: B")
elif 18 <= score <= 20:
    print("Grade: A")
else:
    print("Score is undifined!")

"""Group-2"""

# 1.
n = int(input("Enter your number : "))
for i in range(n):
    print(i)

# 2.
n = int(input("Enter your number : "))
for i in range(1, n+1):
    if n % i == 0:
        print(i)

# 3.
n = int(input("Enter your number : "))
if n % 2 != 0:
    print("number is odd")
else:
    print("number is even")

# 4.
n = int(input("Enter your number : "))
for i in range (n):
    if i % 2 == 0:
        print(i)

# 5.
n = int(input("Enter your number : "))
for i in range (n):
    if i % 2 != 0:
        print(i)

# 6.
n = int(input("Enter your number : "))
for i in range (10,n):
    if i % 2 == 0 and i < 100:
        print(i)

# 7.
a = int(input("Enter your first number : "))
b = int(input("Enter your second number : "))
for i in range(1, min(a,b)+1):
    if a % i == 0 and b % i == 0:
        print(i)

# 8.
a = int(input("Enter your first number : "))
b = int(input("Enter your second number : "))
select = input("Please select even or odd?")
for i in range(a, b+1):
    if select == "even" and i % 2 == 0:
        print(i)
    elif select == "odd" and i % 2 != 0:
        print(i)

# 9.
total = 0
max_number = 0
while True:
    n = int(input("Enter the number (press 0 for stop!) : "))
    total += n
    if n == 0:
        break
if n > max_number:
    max_number = n
    print(f"Total is : {total}")
    print(f"The Max is : {max_number}")

# 10.
n = int(input("Decimal Number : "))
result = ""
while n > 0:
    result = str(n % 2) + result
    n //= 2
    print(result)
b = input("Binary Number : ")
decimal_digit = 0
for i in b:
        decimal_digit = decimal_digit * 2 + int(i)
        print(decimal_digit)


