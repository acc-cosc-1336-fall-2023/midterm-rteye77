#add import
import question_b

km = int(input("Enter value for kilometers: "))
mins = int(input("Enter value for minutes: "))

mph = question_b.get_miles_per_hour(km,mins)
print("Value in miles per hour:", mph)