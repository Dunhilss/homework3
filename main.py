# number = int(input("Enter the day of the week (1-7): "))
# if number == 1:
#     print("\nWeekday: monday")
# elif number == 2:
#     print("\nWeekday: tuesday")
# elif number ==3:
#     print("\nWeekday: wednesday")
# elif number == 4:
#     print("\nWeekday: thursday")
# elif number == 5:
#     print("\nWeekday: friday")
# elif number == 6:
#     print("\nWeekday: sunday")
# elif number == 7:
#     print("\nWeekday: saturday")
# else:
#     print("Incorrect day of the week entered, try again.")

numb1 = int(input("Please enter first number: "))
numb2 = int(input("Please enter second number: "))
if numb1 != numb2 and numb1 < numb2:
   print(str(numb1) + " " + str(numb2))

elif numb1 != numb2 and numb1 > numb2:
   print(str(numb2) + " " + str(numb1))

elif numb1 == numb2:
   print("\nThe numbers are equal. Try again.")