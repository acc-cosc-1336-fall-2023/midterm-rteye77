#add import
import question_c

while True:
    number = input("Enter a number between 1 and 7 and q to quit: ").lower()
    if number == "q":
        break
    else:
        print(question_c.get_day_of_week(int(number)))