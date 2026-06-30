import pandas as pd
import glob

# Saari teen CSV files ek saath padhna
files = glob.glob("data/daily_sales_data_*.csv")

all_data = []

for file in files:
    df = pd.read_csv(file)
    
    # Sirf "pink morsel" wale rows rakhna
    df = df[df["product"] == "pink morsel"]
    
    # Price ka $ sign hatana aur number mein convert karna
    df["price"] = df["price"].str.replace("$", "", regex=False).astype(float)
    
    # Sales column banana = price * quantity
    df["Sales"] = df["price"] * df["quantity"]
    
    # Sirf required columns rakhna, naam capitalize karna
    df = df[["Sales", "date", "region"]]
    df.columns = ["Sales", "Date", "Region"]
    
    all_data.append(df)

# Sab files ko combine karna
final_df = pd.concat(all_data, ignore_index=True)

# Output CSV banana
final_df.to_csv("data/formatted_sales_data.csv", index=False)

print("Done! Output file ban gayi: data/formatted_sales_data.csv")
print(final_df.head())