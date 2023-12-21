import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

def plot_1(ranked_dataframe):
    sorted_df = ranked_dataframe.sort_values('AvgRank', ascending=False)
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.bar(sorted_df['Klass'], sorted_df['AvgRank'])
    ax.set_xlabel('Klass')
    ax.set_ylabel('Average Rank')
    ax.set_title('Average Rank by Class (Sorted)')
    ax.tick_params(axis='x', rotation=90)
    return fig

def plot_2(ranked_dataframe):
    rank_columns = [col for col in ranked_dataframe.columns if 'Rank' in col]
    fig, ax = plt.subplots(figsize=(8, 6))
    for column in rank_columns:
        ax.scatter(range(len(ranked_dataframe)), ranked_dataframe[column], label=column)
    ax.set_xlabel('Index')
    ax.set_ylabel('Rank')
    ax.set_title('Scatterplot of Rank Columns')
    ax.legend()
    return fig

def plot_3(ranked_dataframe):
    klass_values = ranked_dataframe['Klass']
    bins = np.arange(len(klass_values.unique()) + 1) - 0.5
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.hist(klass_values, bins=bins, rwidth=0.8)
    ax.set_xticks(range(len(klass_values.unique())))
    ax.set_xticklabels(klass_values.unique(), rotation=90)
    ax.set_xlabel('Klass')
    ax.set_ylabel('Frequency')
    ax.set_title('Frequency Distribution of Klass')
    return fig

def plot_4(ranked_dataframe):
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.boxplot(x='Klass', y='AvgRank', data=ranked_dataframe, ax=ax)
    ax.set_title('Box Plot of AvgRank by Klass')
    ax.tick_params(axis='x', rotation=90)
    return fig

def plot_all_klass_plots(ranked_dataframe):
    st.write("## Toggle Visibility of Plots")

    # Description for Plot 1
    plot_1_description = """
    ### Average Rank by Class (Sorted)
    This bar plot visualizes the average rank for different classes in descending order.
    - Each bar represents a class, with bar length indicating its average rank.
    - Classes are sorted from highest to lowest average rank for easy comparison.
    """

    # Description for Plot 2
    plot_2_description = """
    ### Scatterplot of Rank Columns
    This plot showcases multiple scatterplots, each representing a column containing 'Rank' in the DataFrame. 
    - The x-axis shows DataFrame indices, while the y-axis displays rank values.
    - Each scatterplot visualizes the distribution of ranks across different columns.
    """

    # Description for Plot 3
    plot_3_description = """
    ### Frequency Distribution of Klass
    It displays a histogram indicating the frequency distribution of various classes ('Klass') in the dataset.
    - The x-axis represents classes, and bar heights show the frequency of each class.
    - Each bar corresponds to a unique class and its occurrence frequency.
    """

    # Description for Plot 4
    plot_4_description = """
    ### Box Plot of AvgRank by Klass
    This plot illustrates the distribution of average ranks across different classes ('Klass').
    - Each box represents the interquartile range (IQR) for a class, with the median displayed inside the box.
    - It allows comparison of average rank distributions among classes.
    """

    # Create radio buttons to select a single plot
    plot_selection = st.radio("Select a Plot to Display", [
        "Average Rank by Class",
        "Scatterplot of Rank",
        "Frequency Distribution of Klass",
        "Box Plot of AvgRank by Klass"
    ])

    # Display the selected plot based on radio button selection
    if plot_selection == "Average Rank by Class":
        st.write(plot_1_description)
        plot_1(ranked_dataframe)

    elif plot_selection == "Scatterplot of Rank":
        st.write(plot_2_description)
        plot_2(ranked_dataframe)

    elif plot_selection == "Frequency Distribution of Klass":
        st.write(plot_3_description)
        plot_3(ranked_dataframe)

    elif plot_selection == "Box Plot of AvgRank by Klass":
        st.write(plot_4_description)
        plot_4(ranked_dataframe)
