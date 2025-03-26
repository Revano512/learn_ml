import pandas as pd
pd.set_option('display.max_rows', 5)
reviews = pd.read_csv("../input/wine-reviews/winemag-data-130k-v2.csv", index_col=0)

# Rename the points into score
reviews.rename(columns={'points': 'score'})

# rename() uses python dictionary input, like:
reviews.rename(index={0: 'firstEntry', 1: 'secondEntry'})

# To rename indexes, use set_index()
# Both the row index and the column index have their own attribute

# using concat(), join(), merge()

# concat() smushes elements together along an axis
canadian_youtube = pd.read_csv("../input/youtube-new/CAvideos.csv")
british_youtube = pd.read_csv("../input/youtube-new/GBvideos.csv")

pd.concat([canadian_youtube, british_youtube])

# join() lets you combine different DF objects which have an index in common
left = canadian_youtube.set_index(['title', 'trending_date'])
right = british_youtube.set_index(['title', 'trending_date'])

left.join(right, lsuffix='_CAN', rsuffix='_UK')

#
# Excercise
#
# To set the index name in the dataset to wines:
reviews.index.name = 'wines'

# or
reindexed = reviews.rename_axis('wines', axis='rows')
