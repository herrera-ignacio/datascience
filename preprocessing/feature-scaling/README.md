# Feature Scaling

__Feature scaling__ is a method used to normalize the range of independent variables or features of data. It's generally performed during the data preprocessing step.

Since the range of values of raw data varies widely, in some machine learning algorithms, objective functions will not work properly without normalization.

> For example, many _classifiers_ calculate the distance between two points by the _Euclidean distance_. If one of the fatures has a broad range of values, the distance will be governed by this particular feature. Therefore, the range of all features should be normalized so that each feature contributes approximately proportionately to the final distance.

## Methods

### Rescaling (min-max Normalization)

This is the simplest method and consists in rescaling the range of features to scale the range in `[0, 1]` or `[-1, 1]`. Selecting the target range depends on the nature of the data. The general formula for a min-max of `[0, 1]` is given as:

$x' = \frac{x - min(x)}{max(x) - min(x)}$

### Mean Normalization 

$x_{norm} = \frac{x-mean(x)}{max(x) - min(x)}$

### Standardization (Z-score Normalization)

In machine learning, we can handle various types of data, e.g. audio signals and pixel values for image data, and this data can include multiple dimensions.

Feature standardization makes the values of each feature in the data have zero-mean and unit-variance.

$x_{stand} = \frac{x-mean(x)}{standard\ deviation(x)}$

$x_{stand} = \frac{x-\overline{x}}{\sigma}$

### Scaling to unit length

Scale the components of a feature vector such that th complete vector has length one. This usually means dividing each component by the _Euclidean length_ of the vector:

$x' = \frac{x}{\left \lvert x \right \rvert}$
