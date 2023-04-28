import pandas as pd
import os

file_path = '/Users/fernando/Desktop/Code/Education/UT Austin/Artificial Intelligence Post Graduate Program/Sources/Wine.csv'
if os.path.exists(file_path):
    df = pd.read_csv(file_path)
    print("DataFrame loaded from file:", file_path)
else:
    print("File not found:", file_path)

# print(df.head())

def edit_col(col):
    col = col*2 + 10
    return col

# df.describe()

# df['alcalinity_of_ash'].mean()

# df.malic_acid.apply(edit_col)

# df.sort_values(by='total_phenols')

# df.info()

output_path = "/Users/fernando/Desktop/Code/Education/UT Austin/Artificial Intelligence Post Graduate Program/Outputs/winedf.csv"

if not os.path.exists(output_path):
    df.to_csv(output_path, index=True)
    print("DataFrame saved to file:", output_path)
else:
    print("File already exists did not load to a new csv:", output_path)
