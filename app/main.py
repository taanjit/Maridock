import pandas as pd
from maridoc_agent import generate_drydock_specification

# Load the Excel file
file_path = "app/Consolidated_Drydock_Specifications_Index_Final.xlsx"

try:
    df = pd.read_excel(file_path)
    print("🧾 Column Headers:")
    for i, col in enumerate(df.columns, start=1):
        print(f"{i}. {col}")

    # Loop through the first 10 specification items
    for item in df['Specification Item'].dropna().head(10):
        print(f"📄 Generating specification for: {item}")
        generate_drydock_specification(item)

except FileNotFoundError:
    print(f"❌ File not found: {file_path}")
except Exception as e:
    print(f"⚠️ An error occurred: {e}")
