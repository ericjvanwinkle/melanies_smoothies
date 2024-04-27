# Import python packages
import streamlit as st
from snowflake.snowpark.functions import col

# Write directly to the app
st.title(":cup_with_straw: Customize Your Smoothie :cup_with_straw:")
st.write(
    """Choose the fruit you want in your custom smoothie!"""
)

name_on_order = st.text_input("Name on Smoothie")
if name_on_order:
    st.write("The name on your Smoothie will be: ", name_on_order)

cnx.connectiont("snowflake")
session = cnx.get_session()
my_dataframe = session.table("smoothies.public.fruit_options").select (col("FRUIT_NAME"))
ingredients_list = st.multiselect("Choose up to 5", my_dataframe)

if ingredients_list:
    st.write (ingredients_list)
    st.text (ingredients_list)

    ingredients_string = ''

    for fruit_chosen in ingredients_list:
        ingredients_string  += fruit_chosen + ' '

    my_insert_stmt = """ insert into smoothies.public.orders(name_on_order, ingredients)
            values ('""" + name_on_order + """', '""" + ingredients_string + """')"""

    st.write(my_insert_stmt)

    time_to_insert = st.button("Submit Order")
    if time_to_insert:
        session.sql(my_insert_stmt).collect()
        st.success('Your Smoothie is ordered!', icon="✅")

