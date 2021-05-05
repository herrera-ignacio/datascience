# Regression Analysis

* Definition
* Regression Model
* History

## Definition

In _statistical modeling_, __regression analysis__ is a set of statistical processes for **estimating the relationships between a _dependent variable_** (often called the '_outcome variable_') **and one or more _independent variables_** (often called '_predictors_').

Regression analysis is primarily used for two conceptually distinct purposes.

1. __Prediction__ and __forecasting__, where its use has substantial overlap with te field of _Machine Learning_.

2. Infer __causal relationships__ between independent and dependent variables in some situations.

Importantly, regressions by themselves _only reveal relationships between a dependent variable and a collection of independent variables in a fixed dataset_. To use regressions for predition or to infer causal relationships, respectively, a researcher must carefully justify why existing relationships have predictive power for a new context or why a relationship between two variables has a causal interpretation. The latter is especially important when researchers hope to estimate causal relationships using observational data.

## Regression Model

In practice, researchers first select a model they would like to estimate and then use their chosen method (e.g., _ordinary least squares_) to estimate the parameters of that model.

Regression models involve the following components:

* __Unknown parameters__, often denoted as a _scalar_ or _vector_ $\beta$.

* __Independent variables__, which are observed in data and are often denoted as a vector $X_i$ (where $i$ denotes a row of data).

* __Dependent variable__, which are observed in data and often denoted using the scalar $Y_i$.

* __Error terms__, which are _not_ directly observed in data and ore often denoted using the scalar $e_i$.

Most regression models propose that $Y_i$ is a function of $X_i$ and $\beta$ with $e_i$ representing an _additive error term_ that may stand in for un-modeled determinants of $Y_i_ or random statistical noise:

$Y_i = f(X_i, \beta) + e_i$

> The researchers' goal is to estimate the function $f(X_i, \beta)$ that most closely fits the data.

To carry out regression analysis, the form of the function $f$ must be specified. Sometimes the form of this function is based on knowledge about the relationship between $Y_i$ and $X_i$ that does not rely on the data. If no such knowledge is available, a flexible or convenient form for $f$ is chosen.

> For example, _least squares_ (including its most common variant, _ordinary least squares_) finds the value of $\beta$ that minimizes the sum of squared errors $\sum_{i}{(Y_i - f(X_i, \beta))^2}$.

A given regression model will ultimately provide an estimate of $\beta$, usually denoted $\hat{\beta}$ to distinguish the estimate from the true (unknown) parameter value that generated the data. Using this estimate, the researchar can use the _fitted_ value $\hat{Y}_i = f(X_i, \hat{\beta})$ for prediction or to assess the accuracy of the model in explaining the data.

Whether the researcher is intrinsically interested in the estimate $\hat{\beta}$ or the predicted value $\hat{Y_i}$ will depend on context and their goals.

> It is important to note that there must be sufficient data to estimate a regression model (to not make the system _undetermined_).

## History

The earliest form of regression was the __method of least squares__, which was published by _Legendre_ in 1805, and by _Gauss_ in 1809. Legendre and Gauss both applied the method to the problem of determining, from astronomical observations, the orbits of bodies about the Sun (mostly comets, but also later the then newly discovered minor planets). Gauss published further development of the theory of least squares in 1821, including a version of the __Gauss-Markov theorem__.

The term "_regression_" was coined by _Francis Galton_ in the 19th century to describe a biological phenomenon (heights of descendants of tall ancestors tend to regress down towards a normal average, also known as __regression toward the mean__). For Galton, regression had only this biological meaning, but his work was later extended by _Udny Yule_ and _Karl Pearson_ to a more general statistical context. In the work of _Yule_ and _Pearson_, the _joint distribution_ of the response and explanatory variables is assumed to be _Gaussian_. This assumption was weakened by _R.A. Fisher_ in his works of 1922 and 1925. Fisher assumed that the _conditional distribution_ of the response variable is Gaussian, but the joint distribution need not be.

Regression methods continue to be an area of active research. In recent decades, new methods have been developed for _robust regression_, regression involving correlated responses such as _time series_ and _growth curves_, regression in which the predictor (independent variable) or response variables are curves, images, graphs, or other complex data objects, regression methods accommodating various types of missing data, nonparametric regression,Bayesian methods for regression, regression in which the predictor variables are measured with error, regression with more predictor variables that observations, and _causal inference_ with regresion.
