import pandas as pd

# Overfitting is when a model matches the training data almost perfectly, 
# but does poorly in validation and other new data

# Underfitting is when a model fails to capture important distinctions
# and patterns in the data, so it performs poorly even in training data 

# Overfitting: capturing spurious patterns that won't recur in the future, leading to less accurate predictions
# Underfitting: failing to capture relevant patterns, again leading to less accurate predictions

# We use max_leaf_nodes in order to control this decision tree branching

# Use a utility function to help compare MAE scores from different values for max_leaf_nodes:

from sklearn.metrics import mean_absolute_error
from sklearn.tree import DecisionTreeRegressor

def get_mae(max_leaf_nodes, train_X, val_X, train_y, val_y):
    model = DecisionTreeRegressor(max_leaf_nodes=max_leaf_nodes, random_state=0)
    model.fit(train_X, train_y)
    preds_val = model.predict(val_X)
    mae = mean_absolute_error(val_y, preds_val)
    return(mae)


# Load data
melbourne_file_path = 'melb_data.csv'
melbourne_data = pd.read_csv(melbourne_file_path) 
# Filter rows with missing values
filtered_melbourne_data = melbourne_data.dropna(axis=0)
# Choose target and features
y = filtered_melbourne_data.Price
melbourne_features = ['Rooms', 'Bathroom', 'Landsize', 'BuildingArea', 
                        'YearBuilt', 'Lattitude', 'Longtitude']
X = filtered_melbourne_data[melbourne_features]

from sklearn.model_selection import train_test_split

# split data into training and validation data, for both features and target
train_X, val_X, train_y, val_y = train_test_split(X, y,random_state = 0)

mae_values = {}

# compare MAE with differing values of max_leaf_nodes
for tree_size in [5, 50, 500, 5000]:
    my_mae = get_mae(tree_size, train_X, val_X, train_y, val_y)
    print("Tree Size: %d  \t\t Mean Absolute Error:  %d" %(tree_size, my_mae))

    mae_values[tree_size] = my_mae

# if you want to find the leaf node with the lowest Mean Absolute Error, then you have to:
best_tree_size = min(mae_values, key=mae_values.get)
print(best_tree_size)

# The best tree size is one with the smallest corresponding MAE, so we do key=mae_values.get
# so that we can see the values of the keys in the mae_values dictionary

# Now, we fit the model using all the data, we dont need to use the validation data anymore

final_model = DecisionTreeRegressor(max_leaf_nodes=best_tree_size, random_state=0)

final_model.fit(X,y)
