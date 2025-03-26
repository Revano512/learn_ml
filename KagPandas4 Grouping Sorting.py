import pandas as pd

reviews = pd.read_csv("../input/wine-reviews/winemag-data-130k-v2.csv", index_col=0)
pd.set_option("display.max_rows", 5)

reviews.groupby('points').points.count()
# groupby() creates a group of reviews which allotted the same point values to the given wines

# To get the cheapest wine in each point value category, do:
reviews.groupby('points').price.min()

# One way of selecting the name of the first wine reviewed from each winery in the dataset:
reviews.groupby('winery').apply(lambda df: df.title.iloc[0])

# (Fine grained control) To pick out the best wine by country and province:
reviews.groupby(['country', 'province']).apply(lambda df: df.loc[df.points.idxmax()])

# Another groupby method agg(), to run a bunch of different functions on your DataFrame
# simultaneously.
# To generate a simple statistical summary of the dataset:
reviews.groupby(['country']).price.agg([len,min,max])

# The multi-index method you will use most often is the one for converting back to a 
# regular index
#countries_reviewed.reset_index()

#
# Sorting
#

# To sort the data based on the len
#countries_reviewed = countries_reviewed.reset_index()
#countries_reviewed.sort_values(by='len')

# sort_values() defaults to an ascending sort, where the lowest values go first
# To make the higher numbers go first, we do:
#countries_reviewed.sort_values(by='len', ascending=False)

# To sort by index values, use the companion method sort_index()
#countries_reviewed.sort_index()

# To sort by more than 1 column at a time:
#countries_reviewed.sort_values(by=['country', 'len'])

reviews.groupby('points').points.count()        # count wines in each points group
reviews.groupby('points').price.min()           # finds the minimum price in each points group

