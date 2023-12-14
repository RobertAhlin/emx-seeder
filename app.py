import streamlit as st
from app_pages.multipage import MultiPage
from app_pages.page_summary import page_summary_body  # Import the function

app = MultiPage(app_name="Ranks and Seeding")

# Add the "Project Summary" page using page_summary_body function
app.add_page("Project Summary", page_summary_body)

# Display some text to check functionality
app.add_page("About", lambda: st.write("This is the About page."))

app.run()
