import pandas as pd     # Pandas is the primary tool data scientists use for exploring and manipulating data

'''
# save filepath to variable for easier access
melbourne_file_path = 'melb_data.csv'

# read the data and store data in DataFrame titled melbourne_data
melbourne_data = pd.read_csv(melbourne_file_path)

# print a summary of the data in melbourne_data
print(melbourne_data.describe())
'''

# 1. Load Data
# 2. ..._file_path = ...
# 3. read file into variable, data = pd.read_csv(..._file_path)
# 4. print summary statistics, summary = data.describe()
# 5. current_year = pd.Timestamp.now().year