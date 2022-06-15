# Task 3

season_list = ['list: winter', 'list: spring', 'list: summer', 'list: autumn']
number_dict = {1 : 'dict: winter', 2 : 'dict: spring', 3 : 'dict: summer', 4 : 'dict: autumn'}
month = int(input("Please enter a month number:"))

if month ==12 or month == 1 or month == 2:
        print(number_dict.get(1))
        print(season_list[0])
elif month == 3 or month == 4 or month ==5:
    print(number_dict.get(2))
    print(season_list[1])
elif month == 6 or month == 7 or month == 8:
    print(number_dict.get(3))
    print(season_list[2])

elif month == 9 or month == 10 or month == 11:
    print(number_dict.get(4))
    print(season_list[3])
else:
        print("There is no such month")








