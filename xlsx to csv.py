import pandas as pd
import numpy as np
import xarray as xr
import os

def main():
    # Load Excel file
    input_path = r"E:\Climpact\BMD\Sylhet.xlsx"
    output_path = "Sylhet_CLIMPACT2.txt"

    # Read the Excel file into a DataFrame
    df = pd.read_excel(input_path)
    
    # Export the DataFrame to a tab-separated .txt file
    df.to_csv(output_path, sep="\t", index=False, float_format="%.1f", header=False)
    
    print(f"Saved to {output_path}")

if __name__ == "__main__":
    main()
