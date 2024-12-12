def calculate_bmi(height, weight):
    """
    this function returns the Body Mass Index (BMI)
    """
    BMI=round(weight / (height ** 2), 2)
    return BMI



def calculate_bmr(height, weight, age, gender):
    """
    this function returns the Basal Metabolic Rate (BMR) using the Harris-Benedict equation
    """

    if gender.lower() == 'male':
        BMR= round(88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age), 2)
        return BMR
    
    elif gender.lower() == 'female':
        BMR= round(447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age), 2)
        return BMR

