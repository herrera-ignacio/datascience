# Frequency Encoding

In the cases where the frequency is related somewhat with the target variable, it helps the model to understand and assign the weight in direct and inverse proportion, depending on the nature of the data.

1. Select a categorical variable to transform.

2. Group by categorical variable and obtain counts of each category.

3. Join it back with the training dataset.

```python
import pandas as pd

data = {'Temperature': ['Hot', 'Cold', 'Very Hot', 'Warm', 'Hot', 'Warm', 'Warm', 'Hot', 'Hot', 'Cold'],
        'Color': ['Red', 'Yellow', 'Blue', 'Blue', 'Red', 'Yellow', 'Red', 'Yellow', 'Yellow', 'Yellow'],
        'Target': [1, 1, 1, 0, 1, 0, 1, 0, 1, 1]}

df = pd.DataFrame(data, columns = ['Temperature', 'Color', 'Target'])

# Cold: 2/10, Hot: 4/10, Very Hot: 1/10, Warm: 3/10
fe = df.groupby('Temperature').size() / len(df)

df.loc[:, 'Temp_freq_encode'] = df['Temperature'].map(fe)
```
