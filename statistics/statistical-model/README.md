# Statistical Model

__Statistical model__ is a mathematical model that embodies a set of _statistical assumptions_ concerning the generation of _sample data_ (and similar data from a larger population). A statistical model __represents, often in considerably idealized form, the data-generating process__.

> Informally, a statistical model can be though a a _set of statistical assumptions_ with a certain property: that the assumption __allows us to calculate the probability of any event__.

A statistical model is usually specified as a mathematical relationship between one or more random variables and other non-random variables. As such, a statistical model is "a formal representation of a theory".

All _statistical hypothesis tests_ and all _statistical estimators_ are derived via statistical models. More generally, statistical models are part of the foundation of _statistical inference_.

## Formal Definition

A statistical model is usually thought of as a pair $(S,P)$ where $S$ is the set of possible observations, i.e. the _sample space_, and $P$ is a set of _probability distributions_ on $S$.

It is assumed that there is a "true" probability distribution induced by the process that generates the observed data. We choose $P$ to represent a set (of distributions) which contains a distribution that adequately approximates the true distribution.

> "A model is a simplification or approximation of reality and hence will not reflect all of reality". - Burnham & Anderson

> "All models are wrong, but some are useful".

The set $P$ is almost always parameterized:

$P = \{ P_{\theta} : \theta \in \Theta \}$

The set $\Theta$ defines the parameters of the model. A parameterization is generally required to have distinct parameter values give rise to distinct distributions, i.e. $P_{\theta_1} = P_{\theta_2} \Rightarrow \theta_1 = \theta_2$ must hold (must be _injective_). A parameterization that meets the requirement is said to be _identifiable_.
