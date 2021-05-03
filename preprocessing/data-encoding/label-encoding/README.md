# Label Encoding

Each category is assigned a value from 1 through N (N is the number of categories for the feature). One major issue with this approach is there is no relation or order between classes, but the algorithm might consider them in some order or relationship.

## Example

```python
import pandas as pd

data = {'Temperature': ['Hot', 'Cold', 'Very Hot', 'Warm', 'Hot', 'Warm', 'Warm', 'Hot', 'Hot', 'Cold'],
        'Color': ['Red', 'Yellow', 'Blue', 'Blue', 'Red', 'Yellow', 'Red', 'Yellow', 'Yellow', 'Yellow'],
        'Target': [1, 1, 1, 0, 1, 0, 1, 0, 1, 1]}

df = pd.DataFrame(data, columns = ['Temperature', 'Color', 'Target'])

# Pandas
df.loc[:, 'Temp_factorize_encode'] = pd.factorize(df['Temperature'])[0].reshape(-1, 1)

# Scikit-learn
from sklearn.preprocessing import LabelEncoder

df['Temp_label_encoded'] = LabelEncoder().fit_transform(df.Temperature)
```
