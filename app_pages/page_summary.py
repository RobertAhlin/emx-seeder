import streamlit as st

# Define the function that represents the body of the "Quick Project Summary" page
def page_summary_body():
    st.title("Quick Project Summary")

    st.header("Summary")
    st.write("This is a summary of your project.")

    st.header("Data Overview")
    # Display information or visualizations related to your data

    st.header("Conclusions")
    st.markdown("Here are some conclusions based on the project analysis.")
