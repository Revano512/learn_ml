import pandas as pd
pd.set_option('display.max_rows', 5)
import numpy as np
reviews = pd.read_csv("../input/wine-reviews/winemag-data-130k-v2.csv", index_col=0)

reviews.points.describe()

reviews.points.mean()

# To see a list of unique values we can use the unique() function
reviews.taster_name.unique()

# To see a list of unique values and how often they occur in the dataset, we can use the 
# value_counts() method:
reviews.taster_name.value_counts()

#
# Maps: function that takes one set of values and "maps" them to another set of values
#
review_points_mean = reviews.points.mean()
reviews.points.map(lambda p: p - review_points_mean)

# the function you pass to map() should expect a single value from Series (a point value)
# and return a transformed version of that value. map() returns a new Series where all
# the values have been transformed by your function

# apply() is the equivalent method if we want to transform a whole DataFrame by calling a 
# custom method on each row

def remean_points(row):
    row.points = row.points - review_points_mean
    return row

reviews.apply(remean_points, axis='columns')

# idxmax()
# For a Series, idxmax() returns the index label where the maximum value occours
# For a DataFrame, you can specify the axis (axis=0 for columns or axis=1 for rows)
# to find the index of column label with the maximum value along that axis

