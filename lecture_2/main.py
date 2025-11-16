def generate_profile(age : int) -> str:
    if 0 <= age <= 12:
        return "Child"
    elif 13 <= age <= 19:
        return "Teenager"
    else:
        return "Adult"


user_name = input("Enter your full name: ")

while True:
    birth_year_str = input("Enter your birth year: ")

    current_age = 2025 - int(birth_year_str)

    if current_age > 150 or current_age < 0:
        print("Your age should not be greater than 150 or less than 0. Enter correct birth year.")
    else:
        break

hobbies = []

while True:
    hobby = input("Enter a favorite hobby or type 'stop' to finish: ")
    if hobby.lower() == "stop":
        break
    else:
        hobbies.append(hobby)
