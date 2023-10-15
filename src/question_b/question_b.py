#write functions here, don't add input('') statements here!
def get_miles_per_hour(km, mins):
    if km < 0 or mins < 0:
        return "Invalid arguments"
    hr = mins / 60.0
    mph = km * hr * .621371
    return mph

print(get_miles_per_hour(32,60))