#### One Hot Encoding

One Hot Encoding is a process of __converting categorical data variables__ so they can be provided to machine learning algorithms to improve predictions. _Is a crucial part of feature engineering for machine learning_.

With one-hot, we convert each categorical value into a new categorical column and assign a binary value of 1 or 0 to those columns. We __map each category to a vector that contains 1 and 0 denoting the presence or absence of the feature__.

This method produces a lot of columns that slows down the learning significantly if the number of the category is very high for the feature. Pandas has `get_dummies` function and Scikit-learn has `OneHotEncoder` for this purpose but it does not create an additional feature column