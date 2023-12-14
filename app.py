import streamlit as st
from app_pages.page_rankings import display_rankings_page
from app_pages.page_summary import page_summary_body
from app_pages.multipage import MultiPage

def page_rankings_body(dataframe):
    display_rankings_page(dataframe)

app = MultiPage(app_name="Ranks and Seeding")

# Add pages
app.add_page("Quick Project Summary", page_summary_body)
# Add other pages...
app.add_page("Rankings by Klubb", page_rankings_body)

# Display some text to check functionality
app.add_page("Test Page", lambda: st.write("This is a test page. App is working!"))

app.run()