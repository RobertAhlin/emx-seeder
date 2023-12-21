import streamlit as st
import pandas as pd
from app_pages.multipage import MultiPage
from app_pages import riders_ranking, seeding_riders, fun_facts, page_summary, page_about
from app_pages.page_klass_plots import plot_all_klass_plots

# Load your data here
@st.cache_data  # Add caching for faster reloads
def load_data():
    # Load Data into a DataFrame
    data = pd.read_csv('ranked/ranked.csv')
    return data

# Load the data
ranked_dataframe = load_data()

app = MultiPage(app_name="Ranks and Seeding")

app.add_page("About", page_about.readme_sections)
app.add_page("Project Summary", page_summary.page_summary_body)
app.add_page("Seeding Riders", lambda: seeding_riders.main(ranked_dataframe))
app.add_page("Riders rank 2023", lambda: riders_ranking.select_and_plot_rankings(ranked_dataframe))
app.add_page("Brand DNF Chance", fun_facts.show_dnf_chance)
app.add_page("Class Plots", lambda: st.pyplot(plot_all_klass_plots(ranked_dataframe)))

app.run()
