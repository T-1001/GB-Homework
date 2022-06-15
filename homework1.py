# task 1

number_1 = 3
number_2 = 5
number_3 = 7
print(number_1, number_2, number_3)


name = input("Please enter your name:")
surname = input("Please enter your surname:")
age = int(input("Please enter your age:"))
height = int(input("Please enter your height:"))


# or this way for age and height

age_1 = input("Please type your age:")
res = int(age_1)

height_1 = input("Please type your height:")
res_1 = int(height_1)



# Task 2

timereq = input('Please enter your time in seconds:')
res_2 = int(timereq)
h = res_2 // 3600
m = (res_2 - h * 3600) // 60
s = res_2 - (h * 3600 + m * 60)
print(f'{h} : {m} : {s}')


# Task 3

number_n = int(input('Please type your number:'))
result = (number_n + int(str(number_n) + str(number_n)) + int(str(number_n) + str(number_n)+ str(number_n)))
print("Total:", result)



# task 4

numbr = abs(int(input("Please enter your pos number ")))
max = numbr % 10
while numbr > 1:
    r = numbr // 10
    if r % 10 > max:
        max = r % 10
    if r > 9:
        continue
    else:
        print("Maximum number is ", max)
        break



# Task 5

profits = float(input("Please enter profits: "))
costs = float(input("Please enter costs: "))
if profits > costs:
    print(f"The LLC is operating at a profit. Return on revenue amounted to {profits / costs:.2f}")
    employees = int(input("Enter the number of LLC employees "))
    print(f"profit per employee was {profits / employees:.2f}")
elif profits == costs:
    print("The LLC is running at zero")
else:
    print("The LLC is operating at a loss")









