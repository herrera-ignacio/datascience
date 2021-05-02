### Scaling data

When we have different columns whose numeric range is considerable, for example, a "Salary" column that goes from 10.000 to 100.000, and another "Age" column that goes from 40 to 60, the variations in "Age" won't have so much impact on some comparision algorithms.

Thus, it's important to "Scale" data to reflect this, and you have two options:

1. __Normalisation__: $x_{stand} = \frac{x-mean(x)}{standard\ deviation(x)}$

2. __Standardisation__: $x_{norm} = \frac{x - min(x)}{max(x) - min(x)}
