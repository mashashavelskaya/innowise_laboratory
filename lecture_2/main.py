def generate_profile(age : int) -> str:
    if 0 <= age <= 12:
        return "Child"
    elif 13 <= age <= 19:
        return "Teenager"
    else:
        return "Adult"



def get_birth_year_str() -> str | None:
    while True:
        birth_year_string = input("Enter your birth year: ")
        if not birth_year_string.isdigit():
            print("Your birth year should be a number!")
            continue

        if int(birth_year_string) < 1900 or int(birth_year_string) > 2025:
            print("Your birth year should not be greater 2025 or less than 1900. Enter correct birth year.")
        else:
            return birth_year_string



def get_hobbies_list(hobbies_list : list):
    while True:
        hobby = input("Enter a favorite hobby or type 'stop' to finish: ")
        if hobby.lower() == "stop":
            break
        else:
            hobbies_list.append(hobby)
    return hobbies_list

# ------- Main ----------
user_name = input("Enter your full name: ")

birth_year_str = get_birth_year_str()

birth_year = int(birth_year_str)

current_age = 2025 - birth_year

hobbies = []

hobbies = get_hobbies_list(hobbies_list=hobbies)

life_stage = generate_profile(age=current_age)

user_profile = {
    "name": user_name,
    "age": current_age,
    "stage": life_stage,
    "hobbies": hobbies
}

user_hobbies = user_profile.get("hobbies")

print("\n\n---")
print("Profile Summary:")
print(f"Name: {user_profile.get('name')}")
print(f"Age: {user_profile.get('age')}")
print(f"Life Stage: {user_profile.get('stage')}")

if not user_hobbies:
    print("You didn't mention any hobbies.")
else:
    print(f"Favorite Hobbies ({len(user_hobbies)}):")
    for hobby in user_hobbies:
        print(f"- {hobby}")

print("---")