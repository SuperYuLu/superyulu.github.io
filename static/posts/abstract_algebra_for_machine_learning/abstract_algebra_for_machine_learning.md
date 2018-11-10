title:    "Abstract Algebra for Machine Learning"
date:    2018-11-10  
time:    "10:55"  
location:    Austin, TX  
country:    United States  
author:    Yu Lu  
category:    Machine Learning  
cover:    cover.jpg  
abstract:  To truely understand machine learning and its algorithms one has to understand the underlying space of the problem, which is supported by the basic mathematic concepts of abstract algebra. Here is a brief summary.

# Abstract Algebra for Machine Learning
![cover](/static/posts/abstract_algebra_for_machine_learning/cover.jpg)  

## Function Approximation(abstract algebra)  
----  

### Abelian Group (comutative group)  
A set A together with an operation \dot which satisfies:  

+ Closure: a, b in A, a \dot b in A
+ Comutativity: a \dot b = b \dot a
+ Identity element: e \dot a = a \dot e = a 
+ Inverse element: exist b in A such that b \dot a = a \dot b = e 
+ Associativity: a \dot (b \dot c) = (a \dot b) \dot c

e.g. An Abelian group generalizes arithemetic of addition of integers.  

### Field  
Field is a set F together with two operations: addition and multiplication. Each operation on the set F forms an Abelian group.  
e.g. field of rational numbers, field of real numbers, field of complex numbers.  

### Vector Space  
A vector space over a field F is a set X together two operations: vector addition and scalar multiplication.  
Vector addition on set X forms an Abelian groups, thus inherient its property.  
Scalar mulitplication on field F satisfies:  

+ Compatibility: a(b V) = (ab) V
+ Identity vector: 1 V = V
+ Distributivity with addtition (vector): a(U + V) = a U + a V
+ Distributivity with addtition (field): (a + b) V = a V + b V
+ Zero: 0 V = 0 

## Norms and Normed Spaces  
----  
### Metric(distance)  
Defined on: set  
A metric is defined on a set with: d: X x X - > [0, +Inf), with:  

+ Non-negativity:  d(x,y) >= 0 
+ Identity: d(x,y) = 0 if and only if x = y 
+ Symmetry: d(x,y) = d(y, x)
+ Triangle inequlity: d(x, z) <= d(x,y) + d(y, z)

### Norm  
A norm on vector space V is a scalar function p: p: V -> [0, +Inf) with following properties:  

+ Positive definite: p(v) = 0 if and only if v = 0 
+ Triangle inequality: p(u + v) <= p(u) + p(v) 
+ Scalability: p(a v) = a p(v) 

Every normed space is a meric space.  

There is also norm defined on Matrix and Functions.  



