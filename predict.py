from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.pipeline import Pipeline
from joblib import load
import pandas as pd

def user_input_predict(user_data):
    # Initialize dictionaries to hold the models
    classification_models = {}
    disease_regressors = {}

    # Load classification models
    targets_classification = ['Diabetes', 'Heart Disease', 'Hypertension']  # Update this list with your actual target names
    for target in targets_classification:
        classification_models[target] = load(f"{target}_classification_model.joblib")

    # Load life expectancy model
    life_expectancy_model = load("life_expectancy_model.joblib")

    # Load disease-specific regressors
    for target in targets_classification:
        disease_regressors[target] = load(f"{target}_disease_regression_model.joblib")

    print("Models loaded successfully!")

    # Feature list used during training
    X = ['Height (cm)', 'Weight (kg)', 'Cholesterol Level (mg/dL)', 'BMI',
         'Blood Glucose Level (mg/dL)', 'Bone Density (g/cm²)',
         'Vision Sharpness', 'Hearing Ability (dB)', 'Cognitive Function',
         'Stress Levels', 'Pollution Exposure', 'Sun Exposure', 'Gender_Male',
         'Physical Activity Level_Low', 'Physical Activity Level_Moderate',
         'Smoking Status_Former', 'Smoking Status_Never',
         'Alcohol Consumption_Occasional', 'Diet_High-fat', 'Diet_Low-carb',
         'Diet_Vegetarian', 'Medication Use_Regular',
         'Family History_Heart Disease', 'Family History_Hypertension',
         'Mental Health Status_Fair', 'Mental Health Status_Good',
         'Mental Health Status_Poor', 'Sleep Patterns_Insomnia',
         'Sleep Patterns_Normal', 'Education Level_Postgraduate',
         'Education Level_Undergraduate', 'Income Level_Low',
         'Income Level_Medium']

    # Ensure user data matches the training data columns
    missing_cols = set(X) - set(user_data.columns)
    for col in missing_cols:
        user_data[col] = 0  # Fill missing columns with 0

    # Ensure user data contains all the necessary columns in the same order
    user_data = user_data[X]

    # Initialize predictions dictionary
    predictions = {}

    # Scale and predict for each model
    for target in targets_classification:
        # Extract the pipeline for this target
        pipeline = classification_models[target]
        
        # Extract the scaler from the pipeline
        scaler = pipeline.named_steps['scaler']
        
        # Scale user data with the specific scaler
        user_data_scaled = scaler.transform(user_data)
        
        # Debug: Show scaled input for each model
        print(f"\nUser Data After Scaling for {target}:")
        print(user_data_scaled)

        # Predict disease status
        disease_pred = pipeline.predict(user_data_scaled)[0]
        print(f"Debug Prediction for {target}: {disease_pred}")
        
        # Predict years if disease is present
        if disease_pred == 1:
            reg_pipeline = disease_regressors[target]
            reg_scaler = reg_pipeline.named_steps['scaler']
            user_data_reg_scaled = reg_scaler.transform(user_data)
            predicted_years = reg_pipeline.predict(user_data_reg_scaled)[0]
        else:
            predicted_years = 'N/A'
        
        predictions[target] = (disease_pred, predicted_years)

    # Predict life expectancy using its pipeline
    life_exp_scaler = life_expectancy_model.named_steps['scaler']
    user_data_life_scaled = life_exp_scaler.transform(user_data)
    predicted_life_expectancy = life_expectancy_model.predict(user_data_life_scaled)[0]

    # Return results
    return predictions, predicted_life_expectancy
