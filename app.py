import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from app_pages.multipage import MultiPage
from app_pages import riders_ranking

# Load your data here
@st.cache_data  # Add caching for faster reloads
def load_data():
    # Load Data into a DataFrame
    data = pd.read_csv('ranked/ranked.csv')
    return data

# Load the data
ranked_dataframe = load_data()

app = MultiPage(app_name="Ranks and Seeding")

app.add_page("Project Summary", lambda: st.write("This is the Project Summary page."))
app.add_page("Riders rank 2023", lambda: riders_ranking.select_and_plot_rankings(ranked_dataframe))
app.add_page("About", lambda: st.write("This is the About page."))


app.run()