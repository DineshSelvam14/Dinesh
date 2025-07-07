age = int(input("Enter your age: "))

if age < 18: 
    print(f"You are a minor since your age {age} is under 18 years.")
elif 18 <= age <= 60:
    print("You are an adult.")
else:
    print("You are a senior citizen.")

score = float(input("Enter your score: "))

if score >= 90:
    print("Grade: A")
elif score >= 75:
    print("Grade: B")
elif score >= 60:
    print("Grade: C")
else:
    print("Grade: F")