import streamlit as st
import os
import datetime
import pandas as pd

def process_uploaded_files(dataframe, ranked_dataframe):
    success_msg = False
    download_button = False
    seeded_df = None

    try:
        # Merge or lookup operation to find the AvgRank from ranked_dataframe for each row in unseeded_dataframe
        seeded_df = dataframe.merge(
            ranked_dataframe[['Namn', 'Klubb', 'AvgRank']],
            on=['Namn', 'Klubb'],
            how='left'
        )

        # Rename the 'AvgRank' column to 'Seeding'
        seeded_df.rename(columns={'AvgRank': 'Seeding'}, inplace=True)

        # Find the maximum AvgRank from ranked_dataframe
        max_avg_rank = ranked_dataframe['AvgRank'].max()

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
        
        current_time = datetime.datetime.now().strftime("%Y-%m-%d_%H%M")
        file_name = f"seeded/{current_time}.csv"
        
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

def main(ranked_dataframe):
    st.title("Seeding Riders")
    st.write("On this page you can upload a CSV with information to seed them for an upcoming event. File columns must be: 'Place of event,Year,Start Number,Name,Club,'")

    # File uploader
    uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])

    if st.button("Process File"):
        if uploaded_file is not None:
            try:
                unseeded_dataframe = pd.read_csv(uploaded_file, encoding='cp1252', header=0)
                process_uploaded_files(unseeded_dataframe, ranked_dataframe)
            except Exception as e:
                st.error(f"Error processing file: {e}")
        else:
            st.warning("Please upload a CSV file.")

    # Button for using system data
    if st.button("Use system data"):
        existing_file_path = 'unseeded/unseeded.csv'  # Replace with your file path
        try:
            if os.path.exists(existing_file_path):
                existing_data = pd.read_csv(existing_file_path, encoding='cp1252')
                process_uploaded_files(existing_data, ranked_dataframe)
            else:
                st.error("System data file not found.")
        except Exception as e:
            st.error(f"Error processing system data: {e}")

if __name__ == "__main__":
    # Load your data here
    ranked_dataframe = pd.read_csv('ranked/ranked.csv')

    main(ranked_dataframe)
