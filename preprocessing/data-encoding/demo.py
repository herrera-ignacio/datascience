import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.compose import ColumnTransformer

dataset = pd.read_csv('./Data.csv')

# We clean NaN values
X_clean = dataset.iloc[:, :-1].values
X_clean[:, 1:3] = SimpleImputer(missing_values = np.nan, strategy = "mean", fill_value=None, verbose=0, copy=True).fit_transform(X_clean[:, 1:3])

# X will be dataset used for the model
# y will be vector that we try to predict
# 20% will be used for testing

X_encoded = ColumnTransformer([("Country", OneHotEncoder(), [0])], remainder="passthrough").fit_transform(X_clean[:])

# We try to predict "Purchased", we'll call this "Y"
Y = LabelEncoder().fit_transform(dataset.iloc[:, 3].values)
 
X_train, X_test, Y_train, Y_test = train_test_split(X_encoded, Y, test_size = 0.2, random_state = 0)

# Scaling variables
from sklearn.preprocessing import StandardScaler

sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)
