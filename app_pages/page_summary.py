# page_summary.py

import streamlit as st

def page_summary_body():
    st.title("Quick Project Summary")

    st.header("Summary")
    st.write("The Streamlit app comprises multiple pages and functionalities, focusing on analyzing rider rankings, seeding riders based on uploaded data, and providing insights into brand DNF chances.")

    st.header("App Structure")
    st.write("- **app.py**: Defines the main app and its pages using the MultiPage class.\n"
             "- **multipage.py**: Implements a class to generate multiple Streamlit pages.\n"
             "- **seeding_riders.py**: Includes functions for processing uploaded CSV files, merging data with ranked rider information, assigning seeding based on rankings, and saving the processed file.\n"
             "- **riders_ranking.py**: Contains functions to select riders, view their rankings, and visualize rankings for selected riders.\n"
             "- **fun_facts.py**: Displays the likelihood of brands encountering a DNF based on historical race data.\n"
             "- **page_about.py**: Display specific sections from a README.md file, focusing on Business understanding, Data Preparation, and Business Requirements within the file.")
             

    st.header("Key Functionalities")
    st.write("- **Riders Rank 2023**: Allows users to select riders, view rankings, and visualize average ranks for selected riders.\n"
             "- **Seeding Riders**: Offers the ability to upload CSV files, process rider data, assign seeding based on rankings, and download the processed file.\n"
             "- **Brand DNF Chance**: Provides insights into the likelihood of a brand getting a DNF based on historical race data.\n"
             "- **About Page**: Information about this project with data text imported from the README.md.")

    st.header("Main Data Used")
    st.write("The main data source for the app is the 'ranked.csv' file, which contains ranked rider information.\n"
             "The ranked.csv data is collected from Swedish timing application at https://live.emx-timing.se then cleaned and sorted through ML.")

    st.header("Features")
    st.write("- **Data Visualization**: Utilizes Matplotlib for visualizing rider rankings and brand DNF chances.\n"
             "- **Data Processing**: Handles CSV file upload, data merging, seeding assignment, and file saving functionalities.")

    st.header("Future Steps")
    st.write("Further enhancements could involve refining visualizations, implementing additional analysis, or integrating more sophisticated machine learning models for predicting rider performances.")
