import os
import shutil
from pathlib import Path

def transfer_excel_files(input_dir, output_dir):
    """
    Copy Excel files from input directory to output directory with '_log' appended to filename.
    
    Args:
        input_dir (str): Directory containing input Excel files
        output_dir (str): Directory where Excel files will be copied to
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
            # Create new filename with '_log' appended
            new_filename = file_path.stem + '_log.xlsx'
            output_path = os.path.join(output_dir, new_filename)
            
            # Copy the file
            shutil.copy2(file_path, output_path)
            print(f"Copied: {new_filename}")
            
        except Exception as e:
            print(f"Error copying {file_path}: {str(e)}")

if __name__ == "__main__":
    input_directory = "/Users/warchief/Desktop/repos/radiation_logger/raw/HIMAC_Radiation_Logs_06.04.2025"
    output_directory = "/Users/warchief/Desktop/repos/radiation_logger/processed_data/HIMAC_06.04.2025_filtered"
    transfer_excel_files(input_directory, output_directory) 