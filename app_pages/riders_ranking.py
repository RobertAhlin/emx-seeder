import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

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
        fig, axes = plt.subplots(nrows=2, ncols=1, figsize=(10, 12))

        # Plot rankings for selected riders
        plot_rankings(selected_data, selected_riders, axes[0])

        # Plot average ranks for selected riders
        selected_ranks = selected_data[selected_data['Namn'].isin(selected_riders)]
        avg_ranks = selected_ranks.groupby('Namn')['AvgRank'].mean().sort_values()
        axes[1].bar(avg_ranks.index, avg_ranks.values)
        axes[1].set_xlabel('Rider')
        axes[1].set_ylabel('Average Rank')
        axes[1].set_title('Average Rank for Selected Riders')
        axes[1].tick_params(axis='x', rotation=90)

        # Adjust vertical spacing between subplots
        plt.subplots_adjust(hspace=2)  
        
        st.pyplot(fig)

# Function to plot rankings for specific riders
def plot_rankings(dataframe, rider_names, ax):
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

    ax.set_xlabel('')
    ax.set_ylabel('Rank')
    ax.set_title('Rankings for Riders')
    ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.7), fancybox=True, shadow=True, ncol=4)  # Position the legend below
    ax.grid(True)  # Add grid lines
    ax.set_xticks(range(1, len(ranking_columns) + 1))  # Set x-ticks for the ranking columns
    ax.set_xticklabels(ranking_columns, rotation=90)  # Set x-tick labels and rotate them by 90 degrees