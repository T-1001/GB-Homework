# Task 4

new_str = input("Type here smth:")
new_word = []
num = 1

for el in range(new_str.count(' ')+1):
    new_word = new_str.split(' ')
    if len(str(new_word)) <= 10:
        print(f" {num} {new_word [el]}")
        num += 1
    else:
        print(f" {num} {new_word [el] [0:10]}")


