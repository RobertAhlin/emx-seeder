import os
import datetime
import pandas as pd
import streamlit as st

def process_uploaded_files(uploaded_file, ranked_dataframe):
    if uploaded_file is not None:
        try:
            unseeded_dataframe = pd.read_csv(uploaded_file, encoding='cp1252', header=0)

            # Merge or lookup operation to find the AvgRank from ranked_dataframe for each row in unseeded_dataframe
            seeded_df = unseeded_dataframe.merge(
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

            # Save the DataFrame to a CSV file
            folder_name = 'seeded'
            if not os.path.exists(folder_name):
                os.makedirs(folder_name)
            
            current_time = datetime.datetime.now().strftime("%Y-%m-%d_%H%M")
            file_name = f"seeded/{current_time}.csv"
            
            seeded_df.to_csv(file_name, index=False, encoding='cp1252')  # Windows-1252 encoding

            st.success(f"File uploaded, processed, and saved successfully to '[{file_name}]({file_name})'")

            # Display contents of the saved file in a table
            if st.checkbox("Show Contents of Processed File"):
                seeded_df_contents = pd.read_csv(file_name)
                st.write(seeded_df_contents)
        except Exception as e:
            st.error(f"Error processing file: {e}")

def main(ranked_dataframe):
    st.title("Seeding Riders")

    # File uploader
    uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])

    if st.button("Process File"):
        process_uploaded_files(uploaded_file, ranked_dataframe)

if __name__ == "__main__":
    # Load your data here
    ranked_dataframe = pd.read_csv('ranked/ranked.csv')

    main(ranked_dataframe)