#add import
import question_a

while True:
    num = input("Enter a number to find the sums of even and q to quit: ").lower()
    if num == "q":
        break
    answ = question_a.sum_even(int(num))
    print("Total of the sum of evens is", answ)