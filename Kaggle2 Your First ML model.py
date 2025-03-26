import pandas as pd

melbourne_file_path = 'melb_data.csv'
melbourne_data = pd.read_csv(melbourne_file_path)

#print(melbourne_data.columns)

# The Melbourne data has some missing values (some houses for which some variables weren't recorded.)
# We'll learn to handle missing values in a later tutorial.  
# Your Iowa data doesn't have missing values in the columns you use. 
# So we will take the simplest option for now, and drop houses from our data. 
# Don't worry about this much for now, though the code is:

# dropna drops missing values (think of na as "not available")
# melbourne_data = melbourne_data.dropna(axis=0)

# There are 2 ways to subset data, 
# 1. Dot Notation, which we use to select the "prediction target"
# 2. Selecting with a column list, which we use to select the "features"

# Dot notation
y = melbourne_data.Price

# Choosing features
melbourne_features = ['Rooms', 'Bathroom', 'Landsize', 'Lattitude', 'Longtitude']
X = melbourne_data[melbourne_features]

# describe
summary = X.describe()
#print(summary)

# Checking the data
#print(X.head())


# Now, onto the ML model, import sklearn
from sklearn.tree import DecisionTreeRegressor

# ! Important: the steps to building a model are:
# 1. Define: What type of model will it be? A decision tree? Some other type of model? 
#            Some other parameters of the model type are specified too.
# 2. Fit: Capture patterns from provided data. This is the heart of modeling.
# 3. Predict: Just what it sounds like.
# 4. Evaluate: Determine how accurate the model's predictions are.

# Define model. Specify a number for random_state to ensure same results each run
melbourne_model = DecisionTreeRegressor(random_state=1)

# Fit model 
melbourne_model.fit(X,y)

# Make predictions
print("Making predictions for the following 5 houses:")
print(X.head())
print("The predictions are:")
print(melbourne_model.predict(X.head()))

