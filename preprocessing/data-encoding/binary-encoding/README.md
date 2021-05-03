# Binary Encoding

Binary encoding __convers a category into binary digits__. Each binary digit creates one feature column. If there are __n__ unique categories, then binary encoding results in only $log_2(n)$ features.

For example, if you have 4 features, the total number of binary encoded features will be 3. Compared to One Hot Encoding, this will require fewer feature columns (for 100 categories, One Hot Encoding will have 100 features, while for Binary Encoding, we will need just 7 features).

1. Categories are first converted to numeric order starting from 1.
2. Integers converted to binary code.
3. Digits of binary number form separate columns.

```python
import pandas as pd

data = {'Temperature': ['Hot', 'Cold', 'Very Hot', 'Warm', 'Hot', 'Warm', 'Warm', 'Hot', 'Hot', 'Cold'],
        'Color': ['Red', 'Yellow', 'Blue', 'Blue', 'Red', 'Yellow', 'Red', 'Yellow', 'Yellow', 'Yellow'],
        'Target': [1, 1, 1, 0, 1, 0, 1, 0, 1, 1]}

df = pd.DataFrame(data, columns = ['Temperature', 'Color', 'Target'])

from category_encoders import BinaryEncoder

encoder = BinaryEncoder(cols=['Temperature'])

dfbin = encoder.fit_transform(df['Temperature'])

df = pd.concat([df, dfbin], axis=1)
```