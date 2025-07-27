def bmi(weight, height):
    bmi_calculated = weight / (height * height)
    if bmi_calculated <= 18.5:
        return "Underweight"
    elif bmi_calculated <= 25.0:
        return "Normal"
    elif bmi_calculated <= 30.0:
        return "Overweight"
    else:
        return "Obese"
