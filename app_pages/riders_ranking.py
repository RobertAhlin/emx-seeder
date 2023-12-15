import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

# Function to plot rankings for specific riders
def plot_rankings(dataframe, rider_names):
    fig, ax = plt.subplots(figsize=(10, 6))

    for rider_name in rider_names:
        # Filter data for the rider
        rider_data = dataframe[dataframe['Namn'] == rider_name]

        # Get ranking columns
        ranking_columns = [col for col in rider_data.columns if col.startswith('Rank')]

        # Convert columns to numeric using .loc to avoid SettingWithCopyWarning
        for col in ranking_columns:
            rider_data.loc[:, col] = pd.to_numeric(rider_data[col], errors='coerce')

        # Extract rider's rankings
        rankings = rider_data[ranking_columns].fillna(pd.NA).values.flatten().astype(float)

        # Plot rankings as a line chart for each rider
        ax.plot(range(1, len(rankings) + 1), rankings, marker='o', label=rider_name)

    ax.set_xlabel('Competition')
    ax.set_ylabel('Ranking')
    ax.set_title('Rankings for Riders')
    ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.1), fancybox=True, shadow=True, ncol=5)  # Position the legend above
    ax.grid(True)  # Add grid lines

    return fig

# Function to select riders and plot rankings
def select_and_plot_rankings(dataframe):
    st.title("Select Riders and View Rankings")

    available_klubbs = ['All'] + dataframe['Klubb'].unique().tolist()
    selected_klubb = st.selectbox('Select a Klubb:', available_klubbs)

    if selected_klubb == 'All':
        selected_data = dataframe
        default_riders = []
    else:
        selected_data = dataframe[dataframe['Klubb'] == selected_klubb]
        default_riders = selected_data['Namn'].unique().tolist()

    namn_values = selected_data['Namn'].unique().tolist()

    selected_riders = st.multiselect('Select riders:', namn_values, default=default_riders)

    if len(selected_riders) > 0:
        fig = plot_rankings(selected_data, selected_riders)
        st.pyplot(fig)
