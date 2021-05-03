#### Ordinal Encoding

Ordinal Encoding ensures the encoding of variables __retains the ordinal nature of the variable__. It assigns a numeric value to each label such as _Label Encoding_ but conserving the ordinal nature.

```python
import pandas as pd

data = {'Temperature': ['Hot', 'Cold', 'Very Hot', 'Warm', 'Hot', 'Warm', 'Warm', 'Hot', 'Hot', 'Cold'],
        'Color': ['Red', 'Yellow', 'Blue', 'Blue', 'Red', 'Yellow', 'Red', 'Yellow', 'Yellow', 'Yellow'],
        'Target': [1, 1, 1, 0, 1, 0, 1, 0, 1, 1]}

df = pd.DataFrame(data, columns = ['Temperature', 'Color', 'Target'])

# Pandas
temp_dict = {'Cold': 1,
             'Warm': 2,
             'Hot': 3,
             'Very Hot': 4}

df['Temp_Ordinal'] = df.Temperature.map(temp_dict)

# Scikit-learn
from sklearn.preprocessing import OrdinalEncoder

oe = OrdinalEncoder(categories=[['Cold', 'Warm', 'Hot', 'Very Hot']])

df['Temperature'] = oe.fit_transform(df[['Temperature']])
```


