def generate_profile(age : int) -> str:
    if 0 <= age <= 12:
        return "Child"
    elif 13 <= age <= 19:
        return "Teenager"
    else:
        return "Adult"


user_name = input("Enter your full name: ")

birth_year_str = input("Enter your birth year: ")

birth_year = int(birth_year_str)

current_age = 2025 - birth_year

hobbies = []

while True:
    hobby = input("Enter a favorite hobby or type 'stop' to finish: ")
    if hobby.lower() == "stop":
        break
    else:
        hobbies.append(hobby)


life_stage = generate_profile(age=current_age)

user_profile = {
    "name": user_name,
    "age": current_age,
    "stage": life_stage,
    "hobbies": hobbies
}


user_hobbies = user_profile.get("hobbies")

print("\n---")
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