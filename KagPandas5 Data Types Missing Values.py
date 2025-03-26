import pandas as pd

reviews = pd.read_csv("../input/wine-reviews/winemag-data-130k-v2.csv", index_col=0)
pd.set_option('display.max_rows', 5)

# use the dtype property to grab the type of a specific column
reviews.price.dtype

# to return the dtype of every column:
reviews.dtypes

# float64 means that it's using a 64-bit floating point number
# int64 means a similarly sized integer instead

#  note: columns consisting entirely of strings do not get their own type
# they are instead given the "object" type

# To convert a column of one type into another, use astype()
# Transform the points column from int64 to float64:

reviews.points.astype('float64')

reviews.index.dtype             # a DataFrame or Series index has its own dtype too

#
# Missing Data
#

# to select NaN entries you can use pd.isnull() or its companion pd.notnull()

reviews[pd.isnull(reviews.country)]

# Replace missing values with "Unknown"

reviews.region_2.fillna("Unknown")

# replace a non-null value
reviews.taster_twitter_handle.replace("@kerinokeefe", "@kerino")

#
# Excercise
#

# To count the number of null values, do:
n_missing_prices = reviews.price.isnull().sum()

# Important thing
reviews['region_1'] = reviews.region_1.fillna("Unknown")
a = reviews.region_1.value_counts()
reviews_per_region = a.sort_values(ascending=False)

# The above is the same as:
reviews_per_region = reviews.region_1.fillna('Unknown').value_counts().sort_values(ascending=False)
