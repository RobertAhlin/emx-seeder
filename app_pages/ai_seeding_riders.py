import streamlit as st
import os
import datetime
import pandas as pd

def process_uploaded_files(dataframe, ai_ranked_dataframe):
    success_msg = False
    download_button = False
    seeded_df = None

    try:
        # Merge or lookup operation to find the Rank from ai_ranked_dataframe for each row in unseeded_dataframe
        seeded_df = dataframe.merge(
            ai_ranked_dataframe[['Namn', 'Klubb', 'Rank']],
            on=['Namn', 'Klubb'],
            how='left'
        )

        # Rename the 'Rank' column to 'Seeding'
        seeded_df.rename(columns={'Rank': 'Seeding'}, inplace=True)

        # Find the maximum AvgRank from ai_ranked_dataframe
        max_avg_rank = ai_ranked_dataframe['Rank'].max()

        # Fill missing Seeding values with the maximum AvgRank plus 1
        seeded_df['Seeding'].fillna(max_avg_rank + 1, inplace=True)

        # Sort by Seeding column
        seeded_df = seeded_df.sort_values(by='Seeding')

        # Assign seeding based on row number
        seeded_df['Seeding'] = seeded_df.reset_index(drop=True).index + 1

        # Remove the 'Unnamed: 5' column if present
        if 'Unnamed: 5' in seeded_df.columns:
            seeded_df.drop(columns='Unnamed: 5', inplace=True)

        # Save the DataFrame to a CSV file
        folder_name = 'seeded'
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)
        
        current_time = datetime.datetime.now().strftime("ai_%Y-%m-%d_%H%M")
        file_name = f"src/seeded/{current_time}.csv"
        
        seeded_df.to_csv(file_name, index=False, encoding='cp1252')  # Windows-1252 encoding

        success_msg = True
        download_button = True
        st.success(f"File processed and saved successfully to '{file_name}'")

    except Exception as e:
        st.error(f"Error processing file: {e}")

    if success_msg and download_button:
        with open(file_name, 'rb') as file:
            btn = st.download_button(label="Download Processed File", data=file, file_name=file_name, mime='text/csv')

    # Display processed file content if available
    if seeded_df is not None:
        st.write("Processed File Contents:")
        st.write(seeded_df)  # Display the DataFrame content after processing

def main(ai_ranked_dataframe):
    st.write("## Seeding Riders")
    st.write("This page will solve the Business requirement 1.")
    st.write("On this page you can upload a CSV with information to seed them for an upcoming event.\n"
             "File columns must be: 'Place of event,Year,#(StarNo.),Namn(Name),Klubb(Club),Märke(Brand),Klass(Class),'")

    # File uploader
    uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])

    if st.button("Process File"):
        if uploaded_file is not None:
            try:
                unseeded_dataframe = pd.read_csv(uploaded_file, encoding='cp1252', header=0)
                process_uploaded_files(unseeded_dataframe, ai_ranked_dataframe)
            except Exception as e:
                st.error(f"Error processing file: {e}")
        else:
            st.warning("Please upload a CSV file.")
    st.write("---")
    # Button for using system data
    st.write("""If no CSV file is available for uploading.  
             Use this button to use preexisting data for testing the seeding function.""")

    if st.button("Use system data"):
        existing_file_path = 'src/unseeded/unseeded.csv'  # Replace with your file path
        try:
            if os.path.exists(existing_file_path):
                existing_data = pd.read_csv(existing_file_path, encoding='cp1252')
                process_uploaded_files(existing_data, ai_ranked_dataframe)
            else:
                st.error("System data file not found.")
        except Exception as e:
            st.error(f"Error processing system data: {e}")

if __name__ == "__main__":
    # Load your data here
    ai_ranked_dataframe = pd.read_csv('src/ranked/ai_ranked.csv')

    main(ai_ranked_dataframe)
