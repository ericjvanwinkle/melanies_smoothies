import streamlit as st
#from snowflake.snowpark.context import get_active_session
from snowflake.snowpark.functions import col

# Write directly to the app
st.title(":green_salad: My Parents New Healthy Diner :cup_with_straw:")
st.write("""Breakfast Menu""")
st.write("Omega 3 & Blueberry Oatmeal")
st.write("Kale, Spinach & Rocket Smoothie")
st.write("Hard-Boiled Free Range Egg")
