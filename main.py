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

# numb1 = int(input("Please enter first number: "))
# numb2 = int(input("Please enter second number: "))
# if numb1 != numb2 and numb1 < numb2:
#    print(str(numb1) + " " + str(numb2))
#
# elif numb1 != numb2 and numb1 > numb2:
#    print(str(numb2) + " " + str(numb1))
#
# elif numb1 == numb2:
#    print("\nThe numbers are equal. Try again.")

print(f"Hello. \nPlease enter 2 numbers, and choose what you want to do with it.")

numb1 = int(input("First number: "))
numb2 = int(input("Second number: "))

try:
     print("1- Addition\n2- Subtraction\n3- Multiplication\n4- Division\n5- Exit")
     user_select = int(input("Enter what you want to do with the numbers: "))

     if user_select == 1:
         print(f"Result: {numb1 + numb2}")
     elif user_select == 2:
         print(f"Result: {numb1 - numb2}")
     elif user_select == 3:
         print(f"Result: {numb1 * numb2}")
     elif user_select == 4:
         print(f"Result: {numb1 / numb2}")
     elif user_select == 5:
         print("See you later, goodbye.")
     else:
         print("Looks like you made the wrong choice. \nTry again.")
except Exception as e:
        print(f"Error: {e}")
except ZeroDivisionError as error:
        print(f"ZeroDivisionError occurred: {error}")
except ValueError as error:
    print("Please enter only integers!")
    print(f"ValueError: {error}")
except Exception as error:
    print(f"Exception occurred: {error}")
finally:
    print("Glad to have been of help, look forward to seeing you again.\n Goodbye.")