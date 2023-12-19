import streamlit as st
import pandas as pd

def show_dnf_chance():
    st.title('Brand DNF Chance')
    st.write("Based on historical data from 2023 races where riders Did Not Finish (DNF)")
    st.write("Calculating what brand the riders use you can see the likeluhood of getting a DNF.")

    # Load the dnf_brands.csv file containing brand DNF information
    dnf_brands_data = pd.read_csv('dnf_brands/dnf_brands.csv')

    # Load the brands.csv file containing available brands
    brands_data = pd.read_csv('dnf_brands/brands.csv')

    # Display a selectbox for brand selection without any default selection
    selected_brand = st.selectbox('Select a brand:', [None] + list(brands_data['Brand']))


    # Check if the selected brand exists in the dnf_brands data
    if selected_brand in dnf_brands_data['Brand'].values:
        # Get the DNF chance for the selected brand
        dnf_chance = dnf_brands_data[dnf_brands_data['Brand'] == selected_brand]['Percentage_DNF'].values[0]
        # Modify the line where likelihood is displayed to round to two decimal places
        st.write(f"The likelihood of {selected_brand} getting a DNF is approximately:")
        st.markdown(f"**{round(dnf_chance, 2)}%**")

    else:
        st.write(f"{selected_brand} information not found in DNF data.")
