from calculation import bmi_calculation
from predict import user_input_predict

from flask import Flask, request, render_template
import pandas as pd

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":

        # Collecting form data
        age = float(request.form.get('age'))
        height = float(request.form.get('height'))
        weight = float(request.form.get('weight'))
        cholesterol_level = float(request.form.get('cholesterol'))
        bmi = float(bmi_calculation(weight, height))
        blood_glucose_level = float(request.form.get('blood-glucose'))
        bone_density = float(request.form.get('bone-density'))
        vision_sharpness = float(request.form.get('vision'))
        hearing_ability = float(request.form.get('hearing'))
        physical_activity_level = int(request.form.get('activity'))
        smoking_status = int(request.form.get('smoking'))
        alcohol_consumption = int(request.form.get('alcohol'))
        diet_type = int(request.form.get('diet'))
        medication_use = int(request.form.get('medication'))
        family_history = int(request.form.get('family-history'))
        cognitive_function = float(request.form.get('cognitive'))
        mental_health_status = int(request.form.get('mental-health'))
        sleep_patterns = int(request.form.get('sleep'))
        stress_levels = float(request.form.get('stress'))
        pollution_exposure = float(request.form.get('pollution'))
        sun_exposure = float(request.form.get('sun-exposure'))
        education_level = int(request.form.get('education'))
        income_level = int(request.form.get('income'))

        
        # Create user_data dictionary
        user_data_dict = {
            'Age (years)': age, 'Height (cm)': height, 'Weight (kg)': weight,
            'Cholesterol Level (mg/dL)': cholesterol_level, 'BMI': bmi,
            'Blood Glucose Level (mg/dL)': blood_glucose_level, 'Bone Density (g/cm²)': bone_density,
            'Vision Sharpness (1.0 = normal)': vision_sharpness, 'Hearing Ability (dB)': hearing_ability,
            'Physical Activity Level_Low': 1 if physical_activity_level == 1 else 0,
            'Physical Activity Level_Moderate': 1 if physical_activity_level == 2 else 0,
            'Physical Activity Level_High': 1 if physical_activity_level == 0 else 0,
            'Smoking Status_Current': 1 if smoking_status == 0 else 0,
            'Smoking Status_Former': 1 if smoking_status == 1 else 0,
            'Smoking Status_Never': 1 if smoking_status == 2 else 0,
            'Alcohol Consumption_Frequent': 1 if alcohol_consumption == 0 else 0,
            'Alcohol Consumption_Occasional': 1 if alcohol_consumption == 1 else 0,
            'Alcohol Consumption_Never': 1 if alcohol_consumption == 2 else 0,
            'Diet_Balanced': 1 if diet_type == 0 else 0,
            'Diet_High-fat': 1 if diet_type == 1 else 0,
            'Diet_Low-carb': 1 if diet_type == 2 else 0,
            'Diet_Vegetarian': 1 if diet_type == 3 else 0,
            'Medication Use_Regular': 1 if medication_use == 2 else 0,
            'Family History_None': 1 if family_history == 0 else 0,
            'Family History_Diabetes': 1 if family_history == 1 else 0,
            'Family History_Heart Disease': 1 if family_history == 2 else 0,
            'Family History_Hypertension': 1 if family_history == 3 else 0,
            'Cognitive Function Score': cognitive_function,
            'Mental Health Status_Fair': 1 if mental_health_status == 1 else 0,
            'Mental Health Status_Good': 1 if mental_health_status == 2 else 0,
            'Mental Health Status_Poor': 1 if mental_health_status == 3 else 0,
            'Sleep Patterns_Insomnia': 1 if sleep_patterns == 1 else 0,
            'Sleep Patterns_Normal': 1 if sleep_patterns == 2 else 0,
            'Stress Levels': stress_levels, 'Pollution Exposure': pollution_exposure,
            'Sun Exposure': sun_exposure,
            'Education Level_Postgraduate': 1 if education_level == 3 else 0,
            'Education Level_Undergraduate': 1 if education_level == 2 else 0,
            'Income Level_Medium': 1 if income_level == 1 else 0,
            'Income Level_High': 1 if income_level == 2 else 0
        }

        # Convert to DataFrame
        user_data = pd.DataFrame([user_data_dict])


        # Debugging: Print user data to console
        print("User Data Received:", user_data)

        
        predictions, predicted_life_expectancy = user_input_predict(user_data)
        # You can process the data further or save it to a database
        return render_template(
        'results.html',
        predictions=predictions,
        predicted_life_expectancy = predicted_life_expectancy
    )
    
    
    # Render the HTML form (assuming form.html is the name of your HTML file)
    return render_template("index.html")




@app.route('/results')
def result():

    return render_template('results.html')

@app.route('/cost')
def cost_calculation():

    return render_template('cost_calculation.html')

if __name__ == "__main__":
    app.run(debug=True)
