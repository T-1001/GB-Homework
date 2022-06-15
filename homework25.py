# Task 5

our_list = [7, 5, 4, 3, 2, 1]
print(f"Rating - {our_list}")
number = int(input("Enter number (Exit 88) "))
while number != 88:
    for el in range(len(our_list)):
        if our_list[el] == number:
            our_list.insert(el + 1, number)
            break
        elif our_list[0] < number:
            our_list.insert(0, number)
        elif our_list[-1] > number:
            our_list.append(number)
        elif our_list[el] > number and our_list[el + 1] < number:
            our_list.insert(el + 1, number)
    print(f"Current list - {our_list}")
    digit = int(input("Type your number "))

