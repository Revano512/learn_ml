import pandas as pd

# There are 2 core objects in pandas: the DataFrame and the Series

# A DataFrame is a table. It contains an array of individual entries, each of which has a certain value.
# Each entry corresponds to a row (or record) and a column

yesno = pd.DataFrame({'Yes': [50,21], 'No': [131,2]})
print(yesno)    
# The "0, No" entry has the value of 131.
# The "0, Yes" entry has a value of 50
# The 0 and 1 are called indexes

bobsue = pd.DataFrame({'Bob': ['I liked it.', 'It was awful.'], 'Sue': ['Pretty Good.', 'Bland.']})
print(bobsue)
# The syntax for declaring a new one is a dictionary whose keys are the column names (Bob and Sue in this example), 
# and whose values are a list of entries

bobsueindex = pd.DataFrame({'Bob': ['I liked it.', 'It was awful.'], 
              'Sue': ['Pretty good.', 'Bland.']},
             index=['Product A', 'Product B'])
print(bobsueindex)

# A Series is a sequence of data values. If a DataFrame is a table, then Series is a list.
onetofive = pd.Series([1,2,3,4,5])
print(onetofive)

# A Series is basically a single column of a DataFrame. So a Series doesnt have a column name,
# it only has one overall name:

producta = pd.Series([30,35,40], index=['2015 Sales', '2016 Sales', '2017 Sales'], name='Product A')
print(producta)

wine_reviews = pd.read_csv("../input/wine-reviews/winemag-data-130k-v2.csv")
print(wine_reviews.shape)
print(wine_reviews.head())

wine_reviews = pd.read_csv("../input/wine-reviews/winemag-data-130k-v2.csv", index_col=0)
wine_reviews.head()
# When you use index_col=0, the first column becomes the index 

# To save a DataFrame to disk as a csv file, do:
# df.to_csv('name_of_file.csv')