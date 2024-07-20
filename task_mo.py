
days_of_week = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]


user_input = int(input("Enter a number (1-7): "))


if 1 <= user_input <= 7:

    print(days_of_week[user_input - 1])# انا هنا عملها بال index
else:
    
    print("the num is Invalid. Please enter a number between 1 and 7.")