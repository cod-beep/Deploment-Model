
import streamlit as st
import numpy as np
import joblib
model = joblib.load("housing_Price_model.pkl")
st.title("House Prediction (lakhs)")
st.write("Enter the input ahd hit predict to get a estimated price for your house!")

#2

area_sqft = st.number_number("Area(Sqft)",min_value=200.0,max_value=10000.0,value=1200.0,step=50.0)
bedrooms = st.number_number("bedroom",min_value=1,max_value=10,value=1200.0,step=1)
bathrooms = st.number_number("bathrooms",min_value=1,max_value=10,value=1,step=1)
age_years = st.number_number("age of house(years)",min_value=0.0,max_value=100.0,value=10.0,step=1.0)
distance_city_km = st.number_number("distance",min_value=0.1,max_value=600.0,value=12.0,step=0.5)

#predict
if st.button("Predict price"):
    x=np.array((["area_sqft","bedrooms","bathrooms","age_years","distance_city_km"]))
    pred = model.predict(x)[0]
    st.success(f"Estimated price:{pred:2f} lakhs")
