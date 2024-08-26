import streamlit as st
import pickle 
# Set up the Streamlit app
st.set_page_config(page_title="Diabetes Prediction App", layout="centered")

# Title and description
st.title("Diabetes Prediction App")
st.write("Fill in the details below to predict the likelihood of diabetes.")

# User-friendly input form with side-by-side layout
col1, col2 = st.columns(2)

with col1:
    pregnancies = st.number_input("Number of Pregnancies", min_value=0, max_value=20, step=1, value=1)
    glucose = st.number_input("Glucose Level", min_value=0, max_value=200, step=1, value=100)
    blood_pressure = st.number_input("Blood Pressure (mm Hg)", min_value=0, max_value=122, step=1, value=70)
    skin_thickness = st.number_input("Skin Thickness (mm)", min_value=0, max_value=100, step=1, value=20)

with col2:
    insulin = st.number_input("Insulin Level (mu U/ml)", min_value=0, max_value=846, step=1, value=30)
    bmi = st.number_input("BMI (Body Mass Index)", min_value=0.0, max_value=67.1, step=0.1, value=25.0)
    diabetes_pedigree_function = st.number_input("Diabetes Pedigree Function", min_value=0.0, max_value=2.5, step=0.01, value=0.5)
    age = st.number_input("Age", min_value=21, max_value=81, step=1, value=30)

# Predict button
if st.button("Predict"):
    # Prepare the input data
    user_data = pd.DataFrame({
        'Pregnancies': [pregnancies],
        'Glucose': [glucose],
        'BloodPressure': [blood_pressure],
        'SkinThickness': [skin_thickness],
        'Insulin': [insulin],
        'BMI': [bmi],
        'DiabetesPedigreeFunction': [diabetes_pedigree_function],
        'Age': [age]
    })

    # Scale the input data
    user_data_scaled = scaler.transform(user_data)

    # Make a prediction
    prediction = model.predict(user_data_scaled)

    # Display the result
    if prediction[0] == 1:
        st.error("The model predicts that you **have diabetes**. Please consult a healthcare professional.")
    else:
        st.success("The model predicts that you **do not have diabetes**. Keep up the healthy lifestyle!")

# Footer
st.markdown("""
    <hr>
    <p style='text-align: center;'>
    This app is for educational purposes only. Always consult a healthcare professional for medical advice.
    </p>
    """, unsafe_allow_html=True)
