import os
import pandas as pd
from pathlib import Path

def count_digits(text):
    """Count the number of digits in a string."""
    if pd.isna(text):  # Handle NaN values
        return 0
    return sum(c.isdigit() for c in str(text))

def process_excel_files(input_dir, output_dir, target_column='content'):
    """
    Process Excel files in the input directory and add a column showing digit counts.
    
    Args:
        input_dir (str): Directory containing input Excel files
        output_dir (str): Directory where processed Excel files will be saved
        target_column (str): Name of the column to count digits in
    """
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    # Get all Excel files from the input directory
    excel_files = list(Path(input_dir).glob('*.xlsx'))
    
    if not excel_files:
        print(f"No Excel files found in {input_dir}")
        return
    
    # Process each Excel file
    for file_path in excel_files:
        try:
            # Read the Excel file
            df = pd.read_excel(file_path)
            
            # Check if target column exists
            if target_column not in df.columns:
                print(f"Warning: Column '{target_column}' not found in {file_path.name}")
                continue
            
            # Add new column with digit counts
            digit_count_column = f'{target_column}_digit_count'
            df[digit_count_column] = df[target_column].apply(count_digits)
            
            # Create output filename
            output_filename = file_path.stem + '_processed.xlsx'
            output_path = os.path.join(output_dir, output_filename)
            
            # Save to Excel
            df.to_excel(output_path, index=False)
            print(f"Processed file: {output_filename}")
            
        except Exception as e:
            print(f"Error processing {file_path}: {str(e)}")

if __name__ == "__main__":
    input_directory = "/Users/warchief/Desktop/repos/radiation_logger/processed_data/HIMAC_06.03.2025"
    output_directory = "/Users/warchief/Desktop/repos/radiation_logger/processed_data/HIMAC_06.03.2025_filtered"
    process_excel_files(input_directory, output_directory) 