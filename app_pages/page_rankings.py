import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

# Function to display rankings by Klubb
def display_rankings_page(ranked_dataframe):
    st.title("Rankings by Klubb")

    # Get unique Klubb values
    unique_klubbs = ranked_dataframe['Klubb'].unique()
    selected_klubb = st.selectbox("Select a Klubb", unique_klubbs)

    klubb_data = ranked_dataframe[ranked_dataframe['Klubb'] == selected_klubb]

    namn_values = klubb_data['Namn'].tolist()
    rank_columns = [f'Rank_{i}' for i in range(1, 7)]

    st.markdown(f"### Rankings for {selected_klubb}")
    plt.figure(figsize=(10, 6))

    for namn in namn_values:
        rider_data = klubb_data[klubb_data['Namn'] == namn][rank_columns].values.flatten()
        plt.plot(rank_columns, rider_data, marker='o', label=namn)

    plt.xlabel('Ranking Columns')
    plt.ylabel('Ranking')
    plt.title(f'Rankings for {selected_klubb}')
    plt.legend()
    plt.xticks(rank_columns)

    st.pyplot()