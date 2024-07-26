import streamlit as st
import pickle
import os
working_dir=os.path.dirname(os.path.abspath(__file__))
with open(f"{working_dir}/fuel_economy_model.pkl", 'rb') as file:
    model = pickle.load(file)
with open(f"{working_dir}/efficient_threshold.pkl", 'rb') as file:
    efficient_threshold = pickle.load(file)

def classify_fuel_economy(fuel_economy, efficient_threshold):
    if fuel_economy >= efficient_threshold:
        return 'Efficient'
    else:
        return 'Inefficient'

def predict_and_classify(current_driving_data, model, efficient_threshold):
    predicted_fuel_economy = model.predict([current_driving_data])[0]
    classification = classify_fuel_economy(predicted_fuel_economy, efficient_threshold)
    return predicted_fuel_economy, classification
st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url("https://wallpapercave.com/wp/wp7636593.jpg");
        background-attachment: fixed;
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
)
st.title('Fuel Economy Prediction')
st.header('Input current driving data')

vehicle_speed = st.number_input('Vehicle Speed (km/h)', min_value=0.0, value=25.68)
engine_speed = st.number_input('Engine Speed (RPM)', min_value=0.0, value=1416.62)
acc_pedal_position = st.number_input('Accelerator Pedal Position (%)', min_value=0.0, value=30.4)
engine_oil_pressure = st.number_input('Engine Oil Pressure (kPa)', min_value=0.0, value=380.0)
engine_coolant_temp = st.number_input('Engine Coolant Temperature (°C)', min_value=0.0, value=85.0)

current_driving_data = [vehicle_speed, engine_speed, acc_pedal_position, engine_oil_pressure, engine_coolant_temp]

if st.button('Predict and Classify'):
    predicted_fuel_economy, classification = predict_and_classify(current_driving_data, model, efficient_threshold)
    st.write(f"Predicted Fuel Economy: {predicted_fuel_economy:.2f}")
    st.write(f"Classification: {classification}")
