import pandas as pd

excel_path = r"D:\Vihaan's download\challenge.xlsx"
df = pd.read_excel(excel_path)

print("Column headers:", df.columns.tolist())
print("\nFirst row data:")
print(df.iloc[0])
