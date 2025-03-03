import streamlit as st


# Define conversion factors for each category 
conversion_factors = {
    "Length": {
        "Kilometer": 0.001,
        "Meter": 1,
        "Centimeter": 100,
        "Millimeter": 1000,
        "Micrometer": 1e6,
        "Nanometer": 1e9,
        "Mile": 1 / 1609.34,
        "Yard": 1.09361,
        "Foot": 3.28084,
        "Inch": 39.3701,
        "Nautical Mile": 1 / 1852,
    },
    "Area": {
        "Square Kilometer": 1e-6,
        "Square Meter": 1,
        "Square Centimeter": 1e4,
        "Square Millimeter": 1e6,
        "Square Mile": 1 / 2.59e6,
        "Square Yard": 1.19599,
        "Square Foot": 10.7639,
        "Square Inch": 1550,
        "Acre": 1 / 4046.86,
        "Hectare": 1e-4,
    },
    "Mass": {
        "Kilogram": 1,
        "Gram": 1000,
        "Milligram": 1e6,
        "Microgram": 1e9,
        "Metric Ton": 1e-3,
        "Pound": 2.20462,
        "Ounce": 35.274,
        "Carat": 5000,
    },
    "Data Transform Rate": {
        "Bit per Second": 1,
        "Kilobit per Second": 1e-3,
        "Megabit per Second": 1e-6,
        "Gigabit per Second": 1e-9,
        "Terabit per Second": 1e-12,
        "Byte per Second": 1 / 8,
        "Kilobyte per Second": 1 / (8 * 1e3),
        "Megabyte per Second": 1 / (8 * 1e6),
        "Gigabyte per Second": 1 / (8 * 1e9),
        "Terabyte per Second": 1 / (8 * 1e12),
    },
    "Digital Storage": {
        "Bit": 1,
        "Byte": 1 / 8,
        "Kilobyte": 1 / (8 * 1e3),
        "Megabyte": 1 / (8 * 1e6),
        "Gigabyte": 1 / (8 * 1e9),
        "Terabyte": 1 / (8 * 1e12),
        "Petabyte": 1 / (8 * 1e15),
    },
    "Energy": {
        "Joule": 1,
        "Kilojoule": 1e-3,
        "Calorie": 0.239006,
        "Kilocalorie": 0.000239006,
        "Watt-hour": 1 / 3600,
        "Kilowatt-hour": 1 / 3.6e6,
        "Electronvolt": 6.242e18,
    },
    "Frequency": {
        "Hertz": 1,
        "Kilohertz": 1e-3,
        "Megahertz": 1e-6,
        "Gigahertz": 1e-9,
    },
    "Fuel Economy": {
        "Miles per Gallon": 1,
        "Kilometers per Liter": 0.425144,
        "Liters per 100 Kilometers": 235.215,
    },
    "Plane Angle": {
        "Degree": 1,
        "Radian": 57.2958,
        "Gradian": 1.11111,
    },
    "Pressure": {
        "Pascal": 1,
        "Kilopascal": 1e-3,
        "Bar": 1e-5,
        "Atmosphere": 9.86923e-6,
        "Torr": 0.00750062,
        "Pounds per Square Inch": 0.000145038,
    },
    "Speed": {
        "Meters per Second": 1,
        "Kilometers per Hour": 3.6,
        "Miles per Hour": 2.23694,
        "Knot": 1.94384,
        "Feet per Second": 3.28084,
    },
    "Time": {
        "Second": 1,
        "Millisecond": 1e3,
        "Microsecond": 1e6,
        "Minute": 1 / 60,
        "Hour": 1 / 3600,
        "Day": 1 / 86400,
        "Week": 1 / 604800,
        "Month": 1 / 2.628e6,
        "Year": 1 / 3.154e7,
    },
    "Volume": {
        "Cubic Meter": 1,
        "Liter": 1000,
        "Milliliter": 1e6,
        "Cubic Centimeter": 1e6,
        "Cubic Inch": 61023.7,
        "Cubic Foot": 35.3147,
        "Gallon": 264.172,
        "Quart": 1056.69,
        "Pint": 2113.38,
        "Fluid Ounce": 33814,
    },
}



# Page title
st.title(f"Universal Unit Converter 📏🌡️⚖️")


# Unit selection
unit_selection = st.selectbox("Select Unit",conversion_factors.keys())


option_from = st.selectbox(f"Convert {unit_selection} From", conversion_factors[unit_selection], index=None, placeholder="Pick the unit you want to convert from")
option_to = st.selectbox(f"Convert  {unit_selection} To", conversion_factors[unit_selection], index=None, placeholder="Pick the unit you want to convert to")


# Input field
number = st.number_input(f"Insert a number", value=None, placeholder="Type a number")



# Conversion logic
if st.button("Convert"):
    if number is not None and option_from and option_to:
        value_in_base = number / conversion_factors[unit_selection][option_from]
        converted_value = value_in_base * conversion_factors[unit_selection][option_to]
       # Display detailed conversion message
        st.success(
            f"**Conversion Result:**\n\n"
            f"**{number:.4f} {option_from}** is equal to **{converted_value:.4f} {option_to}**"
        )