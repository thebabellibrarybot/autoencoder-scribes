import pandas as pd

def add_df_to_csv(df, filename):
    # Check if the CSV file already exists
    try:
        existing_df = pd.read_csv(filename)
    except FileNotFoundError:
        existing_df = pd.DataFrame()

    # Check if the input DataFrame is already in the CSV file
    is_in_csv = False
    if not existing_df.empty:
        # Compare the input DataFrame to each row in the CSV file
        for i, row in existing_df.iterrows():
            if row.equals(df):
                is_in_csv = True
                break
    
    # If the input DataFrame is not in the CSV file, append it to the CSV file
    if not is_in_csv:
        existing_df = pd.concat([existing_df, df], ignore_index=True)
        existing_df.to_csv(filename, index=False)