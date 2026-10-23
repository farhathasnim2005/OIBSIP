
def calculate_bmi(weight, height):
    return weight / (height ** 2)


def get_bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal weight"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"


print("=" * 35)
print("       BMI CALCULATOR")
print("=" * 35)

try:
    weight = float(input("Enter your weight (kg): "))
    height_cm = float(input("Enter your height (cm): "))

    if weight <= 0 or height_cm <= 0:
        print("Error: Enter positive values only.")
    else:
        height_m = height_cm / 100
        bmi = calculate_bmi(weight, height_m)
        category = get_bmi_category(bmi)

        print("\n------ BMI RESULT ------")
        print(f"Weight   : {weight:.1f} kg")
        print(f"Height   : {height_cm:.1f} cm")
        print(f"BMI      : {bmi:.2f}")
        print(f"Category : {category}")
        print("------------------------")

except ValueError:
    print("Invalid input! Please enter numbers only.")
