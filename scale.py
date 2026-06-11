import streamlit as st
st.title("Temperature Converter")
temp = st.number_input("Enter Temperature", value=0.0)
from_unit = st.selectbox(
    "From",
    ["Celsius", "Fahrenheit", "Kelvin"]
)
to_unit = st.selectbox(
    "To",
    ["Celsius", "Fahrenheit", "Kelvin"]
)
def convert_temperature(temp, from_unit, to_unit):
    if from_unit == "Celsius":
        c = temp
    elif from_unit == "Fahrenheit":
        c = (temp - 32) * 5 / 9
    else:  # Kelvin
        c = temp - 273.15
    if to_unit == "Celsius":
        return c
    elif to_unit == "Fahrenheit":
        return (c * 9 / 5) + 32
    else:  # Kelvin
        return c + 273.15
result = convert_temperature(temp, from_unit, to_unit)

st.subheader("Result")
st.success(f"{temp:.2f} {from_unit} = {result:.2f} {to_unit}")
