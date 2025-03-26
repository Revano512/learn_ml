import pandas as pd
reviews = pd.read_csv("../input/wine-reviews/winemag-data-130k-v2.csv", index_col=0)
pd.set_option('display.max_rows', 5)

# there is also a thing called a native python object

reviews.country         # country is the name of the column
reviews['country']      # if we have a python dictionary, we can access its values using the indexing [] operator

# There are 2 ways of selecting a specific Series out of a DataFrame
reviews['country'][0]

# Indexing in Pandas

# 1. Index based selection: selecting data based on its numerical position in the data, iloc
reviews.iloc[0]     # select the first row of data in a DataFrame

# Both loc and iloc are row-first, column-second

# To get a column with iloc, we can do the following:
reviews.iloc[:,0]

# To select the country column from just the first, second, and third row, 
# we would do:
reviews.iloc[:3,0]

# To select just the second and third entries, we would do:
reviews.iloc[1:3,0]

# It's also possible to pass a list:
reviews.iloc[[0,1,2],0]

# Negative numbers are used to start counting forwards from the end of the values
reviews.iloc[-5:]

#
# The second way for attribute selection is the one followed by the loc operator
# With this method, the data index value matters, not the position
#

# To get the first entry in reviews
reviews.loc[0,'country']

# It's usually easier to just use loc, since your dataset usually has meaningful indices
reviews.loc[:,['taster_name','taster_twitter_handle','points']]

# iloc 0:10 will select 0 to 9, but loc 0:10 will select 0 to 10

# Manipulating the index
# Use set_index to set a whole column as the index
reviews.set_index("title")

# Conditional Selection
reviews.country == 'Italy'      # True, False, False ,True, etc.

reviews.loc[(reviews.country == 'Italy') & (reviews.points >= 90)]
reviews.loc[(reviews.country == 'Italy') | (reviews.points >= 90)]

reviews.loc[reviews.country.isin(['Italy', 'France'])]      # Select wines only from Italy or France

reviews.loc[reviews.price.notnull()]                        # Highlight values which are (or are not) empty (NaN)

# Assigning Data

reviews['critic'] = 'everyone'

# Assign with an iterable of values
reviews['index_backwards'] = range(len(reviews),0,-1)


# (Excerise question) Create a DataFrame top_oceania_wines containing all reviews with at least 95 points for wines
# from Australia or New Zealand
top_oceania_wines = reviews.loc[(reviews.country.isin(['Australia','New Zealand'])) & 
                                (reviews.points >= 95)] 
