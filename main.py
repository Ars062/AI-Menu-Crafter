import streamlit as st
import main_2
st.title("Restaurant Name and Menu Generator")
name=st.sidebar.selectbox("Select Food Type", ["Indian","Mexican", "Italian",  "Chinese", "Japanese", "French", "Thai", "Greek", "Spanish", "American"])

if name:
    result = main_2.generate_restaurant_name_and_menu_(name)
    st.header(result["restaurant_name"].strip())
    menu_items = result["menu_items"].split(", ")
    st.subheader("Menu Items:")
    for item in menu_items:
        st.write(f"- {item.strip()}")