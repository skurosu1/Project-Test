import pandas as pd

# Set pandas display options to show all rows AND all columns
pd.set_option('display.max_rows', None)  # Show all rows
pd.set_option('display.max_columns', None)  # Show all columns
pd.set_option('display.width', None)  # Expand display width to show all columns
pd.set_option('display.expand_frame_repr', False)  # Don't wrap to multiple lines
pd.set_option('display.max_colwidth', None)  # Show full content of each cell

# URL of the CSV file
url = r"C:\Users\shawn\OneDrive\Desktop\Lighthouse\projects\SQL-PROJECT-07-07-2025\data\sales_report.csv"
df = pd.read_csv(url, usecols=['productSKU', 'name', 'ratio', 'stockLevel'])

# Create a new column with the concatenated values
df['combined'] = df['productSKU'].astype(str).str.strip() + '--' + df['name'].astype(str).str.strip()

selected_columns = ['combined', 'ratio', 'stockLevel'] 
df_selected = df[selected_columns]

# Display the DataFrame
print(df_selected)