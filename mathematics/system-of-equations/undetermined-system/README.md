# Undetermined System

* Definitions
* Solutions
* Homogeneous case

## Definitions

In mathematics, a _system of linear equations_ or a _system of polynomial equations_, is considered __undetermined__ if there are fewer equations that unknowns.

> In constrast to an __overdetermined system__, where there are more equaitons that unknowns.

The terminology can be explained using the concept of __constraint counting__. Each _unknown_ can be seen as an available _degree of freedom_. Each equation introduced into the system can be viewed as a _constraint_ that restricts one degree of freedom.

Therefore, the critical case (between overdetermined and undetermined) occurs when the number of equations and the number of free variables are equao. For every variable giving a degree of freedom, there exists a corresponding constraint removing a degree of freedom.

> The undetermined case occurs when the system has been underconstrained, that is, when the _unknowns_ outnumber the _equations_.

## Solutions 

An undetermined linear system has either __no solution or infinitely many solutions__.

For example, the following doesn't have a solution. This is defined as _inconsistent_.

$
\begin{array}{rcr}
x+y+z = 1 \\
x+y+z = 0
\end{array}
$

And the following example has an infinitude of solutions.

There are _algorithms_ to decide whether an undetermined system has solutions, and if it has any, to express all solutions as linear functions of $k$ free parameters. The simplest one is __Gaussian elimination__.

## Homogeneous case

The homogeneous (_with all constant terms equal to zero_) undetermined linear system __always has non-tirivial solutions__ (in addition to the trivial solution where all the unknowns are zero).

There are __infinity of such solutions__, which form a _vector space_, whose dimension is the difference between the number of unknowns and the rank of the matrix of the system.
