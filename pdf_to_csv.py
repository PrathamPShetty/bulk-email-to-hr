import camelot
import pandas as pd

# Read PDF
tables = camelot.read_pdf("hr_emails.pdf", pages="all")

# Combine all tables
all_tables = [table.df for table in tables]   # each table.df is a pandas DataFrame
merged_df = pd.concat(all_tables, ignore_index=True)

# Save to one CSV
merged_df.to_csv("hr_emails.csv", index=False)

print("Combined into hr_emails.csv")
