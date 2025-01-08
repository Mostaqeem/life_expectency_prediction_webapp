def bmi_calculation(weight, height_cm):
    """
    Calculate the Body Mass Index (BMI).
    
    Parameters:
    weight (float): Weight of the person in kilograms.
    height (float): Height of the person in meters.

    Returns:
    float: The calculated BMI.
    """
    height = height_cm / 100
    
    if height <= 0:
        raise ValueError("Height must be greater than zero.")
    if weight <= 0:
        raise ValueError("Weight must be greater than zero.")
    
    bmi = weight / (height ** 2)
    return round(bmi, 2)
