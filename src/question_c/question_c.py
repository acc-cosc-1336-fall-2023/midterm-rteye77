#write functions here, don't add input('') statements here!
def get_day_of_week(num):
    if int(num) < 1 or int(num) > 7:
        return ("Invalid number")
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    return days[num-1]