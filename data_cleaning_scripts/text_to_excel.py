import os
import pandas as pd
from pathlib import Path

def text_files_to_excel(input_dir, output_dir):
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    # Get all text files from the input directory
    text_files = list(Path(input_dir).glob('*.txt'))
    
    if not text_files:
        print(f"No text files found in {input_dir}")
        return
    
    # Process each text file
    for file_path in text_files:
        try:
            with open(file_path, 'r', encoding='latin-1') as file:
                # Read lines and remove empty lines
                lines = [line.strip() for line in file.readlines() if line.strip()]
                
            # Create DataFrame with each line as a separate row
            df = pd.DataFrame({'content': lines})
            
            # Create output filename (replace .txt with .xlsx)
            output_filename = file_path.stem + '.xlsx'
            output_path = os.path.join(output_dir, output_filename)
            
            # Save to Excel
            df.to_excel(output_path, index=False)
            print(f"Created Excel file: {output_filename}")
            
        except UnicodeDecodeError as e:
            # Read the file in binary mode to get the problematic line
            with open(file_path, 'rb') as file:
                file.seek(e.start)
                problematic_line = file.read(100)  # Read 100 bytes around the error
                print(f"Error in file {file_path}:")
                print(f"Problematic line (in bytes): {problematic_line}")
                print(f"Error position: {e.start}")
                print(f"Error details: {str(e)}")
        except Exception as e:
            print(f"Error processing {file_path}: {str(e)}")

if __name__ == "__main__":
    input_directory = "/Users/warchief/Desktop/repos/radiation_logger/raw/HIMAC_Radiation_Logs_06.04.2025"
    output_directory = "/Users/warchief/Desktop/repos/radiation_logger/processed_data/HIMAC_06.04.2025"
    text_files_to_excel(input_directory, output_directory)  