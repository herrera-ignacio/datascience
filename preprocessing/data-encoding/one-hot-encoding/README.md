# One Hot Encoding

One Hot Encoding is a process of __converting categorical data variables__ so they can be provided to machine learning algorithms to improve predictions. _Is a crucial part of feature engineering for machine learning_.

With one-hot, we convert each categorical value into a new categorical column and assign a binary value of 1 or 0 to those columns. We __map each category to a vector that contains 1 and 0 denoting the presence or absence of the feature__.

This method produces a lot of columns that slows down the learning significantly if the number of the category is very high for the feature. Pandas has `get_dummies` function and Scikit-learn has `OneHotEncoder` for this purpose but it does not create an additional feature column.

> This approach can be adopted for any machine learning algorithm that looks at _all_ the features _at the same time_ during training. For example, support vector machines, neural networks, and clustering algorithms.

## Example

```python

import pandas as pd

# Dataset
data = {'Temperature': ['Hot', 'Cold', 'Very Hot', 'Warm', 'Hot', 'Warm', 'Warm', 'Hot', 'Hot', 'Cold'],
        'Color': ['Red', 'Yellow', 'Blue', 'Blue', 'Red', 'Yellow', 'Red', 'Yellow', 'Yellow', 'Yellow'],
        'Target': [1, 1, 1, 0, 1, 0, 1, 0, 1, 1]}

df = pd.DataFrame(data, columns = ['Temperature', 'Color', 'Target'])

# With Pandas
df = pd.get_dummies(df, prefix=['Temp'], columns=['Temperature'])

# With Scikit-learn
from sklearn.preprocessing import OneHotEncoder

ohc = OneHotEncoder()

ohe = ohc.fit_transform(df.Temperature.values.reshape(-1, 1)).toarray()

dfOneHot = pd.DataFrame(ohe, columns = ["Temp_" + str(ohc.categories_[0][i]) for i in range(len(ohc.categories_[0]))])

dfh = pd.concat([df, dfOneHot], axis=1)
```
