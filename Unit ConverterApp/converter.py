import streamlit as st
import pandas as pd

st.set_page_config(page_title="World Unit Converter 🌎", page_icon="🌎")

# Custom CSS for styling
st.markdown("""
    <style>
    .main {
        background-color: #f0f2f6;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        border-radius: 10px;
    }
    .stSelectbox {
        border-radius: 10px;
    }
    </style>
""", unsafe_allow_html=True)

st.title(" 🌎 World Unit Converter ❤️")
st.write("Convert between different units from around the world!")

# Create conversion categories
conversion_category = st.selectbox(
    "Select Conversion Category",
    ["Length 📏", "Weight ⚖️", "Temperature 🌡️", "Currency 💰"]
)

if conversion_category == "Length 📏":
    units = ["Meters", "Kilometers", "Miles", "Feet", "Inches"]
    input_unit = st.selectbox("From:", units)
    output_unit = st.selectbox("To:", units)
    value = st.number_input("Enter Value:", value=0.0)
    
    # Length conversion logic
    conversion_factors = {
        "Meters": 1,
        "Kilometers": 1000,
        "Miles": 1609.34,
        "Feet": 0.3048,
        "Inches": 0.0254
    }
    
    if st.button("Convert"):
        # Convert to meters first
        meters = value * conversion_factors[input_unit]
        # Convert from meters to target unit
        result = meters / conversion_factors[output_unit]
        st.success(f"{value} {input_unit} = {result:.2f} {output_unit}")

elif conversion_category == "Weight ⚖️":
    units = ["Kilograms", "Pounds", "Ounces", "Grams"]
    input_unit = st.selectbox("From:", units)
    output_unit = st.selectbox("To:", units)
    value = st.number_input("Enter Value:", value=0.0)
    
    # Weight conversion logic
    conversion_factors = {
        "Kilograms": 1,
        "Pounds": 0.453592,
        "Ounces": 0.0283495,
        "Grams": 0.001
    }
    
    if st.button("Convert"):
        # Convert to kilograms first
        kg = value * conversion_factors[input_unit]
        # Convert from kg to target unit
        result = kg / conversion_factors[output_unit]
        st.success(f"{value} {input_unit} = {result:.2f} {output_unit}")

elif conversion_category == "Temperature 🌡️":
    units = ["Celsius", "Fahrenheit", "Kelvin"]
    input_unit = st.selectbox("From:", units)
    output_unit = st.selectbox("To:", units)
    value = st.number_input("Enter Value:", value=0.0)
    
    if st.button("Convert"):
        # Temperature conversion logic
        if input_unit == output_unit:
            result = value
        else:
            # Convert to Celsius first
            if input_unit == "Fahrenheit":
                celsius = (value - 32) * 5/9
            elif input_unit == "Kelvin":
                celsius = value - 273.15
            else:
                celsius = value
                
            # Convert from Celsius to target unit
            if output_unit == "Fahrenheit":
                result = (celsius * 9/5) + 32
            elif output_unit == "Kelvin":
                result = celsius + 273.15
            else:
                result = celsius
                
        st.success(f"{value} {input_unit} = {result:.2f} {output_unit}")

elif conversion_category == "Currency 💰":
    currencies = ["USD 🇺🇸", "EUR 🇪🇺", "GBP 🇬🇧", "JPY 🇯🇵", "INR 🇮🇳"]
    input_currency = st.selectbox("From:", currencies)
    output_currency = st.selectbox("To:", currencies)
    amount = st.number_input("Enter Amount:", value=0.0)
    
    # Sample exchange rates (you would need to use a real API for live rates)
    exchange_rates = {
        "USD 🇺🇸": 1,
        "EUR 🇪🇺": 0.85,
        "GBP 🇬🇧": 0.73,
        "JPY 🇯🇵": 110.0,
        "INR 🇮🇳": 74.5
    }
    
    if st.button("Convert"):
        # Convert to USD first
        usd = amount / exchange_rates[input_currency]
        # Convert from USD to target currency
        result = usd * exchange_rates[output_currency]
        st.success(f"{amount} {input_currency} = {result:.2f} {output_currency}")

# Footer
st.markdown("---")
st.markdown("### How to use:")
st.write("1. Select the conversion category")
st.write("2. Choose the units to convert from and to")
st.write("3. Enter the value")
st.write("4. Click the Convert button")

# Add some spacing
st.markdown("<br>", unsafe_allow_html=True)

# Add a nice footer
st.markdown("""
    <div style='text-align: center; color: gray;'>
        Made with ❤️ using Streamlit
    </div>
""", unsafe_allow_html=True)
