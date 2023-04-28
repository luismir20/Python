import difflib
import csv

file1_path = "/Users/fernando/Desktop/Code/Python/ChatbotGUI.py"
file2_path = "/Users/fernando/Desktop/Code/Python/ChatbotGUI2.py"
csv_file_path = "/Users/fernando/Desktop/Code/Output/FileDifferencesScan.csv"

with open(file1_path, 'r') as file1:
    script1 = file1.readlines()
with open(file2_path, 'r') as file2:
    script2 = file2.readlines()

diff = list(difflib.unified_diff(script1, script2, fromfile=file1_path, tofile=file2_path))

with open(csv_file_path, mode='w') as csv_file:
    writer = csv.writer(csv_file)
    for line in diff:
        writer.writerow([line])
