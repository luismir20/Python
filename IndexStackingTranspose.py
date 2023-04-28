import os
import pandas as pd

input_path = '/Users/fernando/Desktop/Code/Sources/Sample.csv'
output_path_SSD = '/Volumes/Extreme SSD/Code Folder/OutputsSSD/Python Outputs/SampleOutputSSD.csv'
output_path_desktop = '/Users/fernando/Desktop/Code/Output/Sample.csv'

if os.path.isfile(input_path):
    df = pd.read_csv(input_path, encoding='ISO-8859-1')
    df = df.set_index(df.columns[0])
    df_transposed = df.T
    df_transposed = df_transposed.reset_index()
    df_unstacked = df_transposed.unstack()
    df_unstacked = df_unstacked.reset_index()
    df_unstacked = df_unstacked.rename(columns={'level_1': 'SortOrder', 0: 'Answer'})

    if os.path.isfile(output_path_SSD):
        print('Error: Output file already exists at', output_path_SSD)
    else:
        try:
            output_dir = os.path.dirname(output_path_SSD)
            if not os.path.exists(output_dir):
                os.makedirs(output_dir)
            df_unstacked.to_csv(output_path_SSD)
            print('Output saved to', output_path_SSD)
        except PermissionError:
            print('Error: Insufficient permissions to create output directory at', output_dir)

    if os.path.isfile(output_path_desktop):
        print('Error: Output file already exists at', output_path_desktop)
    else:
        df_unstacked.to_csv(output_path_desktop)
        print('Output saved to', output_path_desktop)

    print(df_unstacked)
    print('Process successful')

else:
    print('Error: Input file not found at', input_path)
