# Mean Encoding

In _Mean Encoding_, also called _Target Encoding_, the feature label for each category is decided with the _mean value of the target variable_ on a training data.

This encoding method brings out the relation between similar categories, but the connections are _bounded within the categories and target itself_.

The advantages is that it _does not affect the volume of the data_ and helps in faster learning.

Usually, Mean Encoding is notorious for over-fitting, thus, a regularization with cross-validation or some other approach is a mus on most occasions.

1. Select a categorical variable.

2. Group by the categorical variable and obtain the aggregated sum over the "Target" variable.

3. Group by the categorical variable and obtain aggregated count over "Target" variable.

4. Divide step 2 / step 3 results and join it back with the training data.

```python
import pandas as pd

data = {'Temperature': ['Hot', 'Cold', 'Very Hot', 'Warm', 'Hot', 'Warm', 'Warm', 'Hot', 'Hot', 'Cold'],
        'Color': ['Red', 'Yellow', 'Blue', 'Blue', 'Red', 'Yellow', 'Red', 'Yellow', 'Yellow', 'Yellow'],
        'Target': [1, 1, 1, 0, 1, 0, 1, 0, 1, 1]}

df = pd.DataFrame(data, columns = ['Temperature', 'Color', 'Target'])

mean_encode = df.groupby('Temperature')['Target'].mean()

df.loc[:, 'Temperature_mean_enc'] = df['Temperature'].map(mean_encode)
```