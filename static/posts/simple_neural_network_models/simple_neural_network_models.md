title:    "Simple Neural Network Models"
date:    2018-11-11  
time:    "11:26"  
location:    Austin, TX  
country:    United States  
author:    Yu Lu  
category:    Machine Learning  
cover:    cover.jpg  
abstract:  While deep neural networks are of very popular in the machine leanring community, it's also interesting to know the very basic and simple models which has inspired the fast development of move powerful models. Here is a brief summary of some of them.

# Simple Neural Network Models  
![cover](/static/posts/simple_neural_network_models/cover.jpg)  



## Belief(Bayesian) Network  

![SimpleBayesNetNodes](/static/posts/simple_neural_network_models/SimpleBayesNetNodes.svg)

+ Probablistic graphic model represents variables and their conditional dependencies 
+ Representation: directed acyclic graph(DAG)
+ Nodes: observable quantities or latent variables 
+ Application: inferring latent variables, parameter learning, structure learning

## Markov Ranodm Field(MRF)  

![Markov_random_field_example](/static/posts/simple_neural_network_models/Markov_random_field_example.png)

+ Random variables with having a Markov property described by undirected graph 
+ Representation: similar to Baysian Network, MRF is represented by  undirected graph G(V, E), may be cyclic.
+ Properties: pairwise, local and global Markov property
+ Application: computer vision, machine learning



## Hopfield Network(1974)  

![Hopfield-net](/static/posts/simple_neural_network_models/Hopfield-net.png)

+ A form a recurrent artificial neural network (RNN)  
+ Units: binary threshold units, e.g. 1, -1 
+ Connection: compelete undirected graph G = <V, f> with weight \\( w_{i,j} \\)
+ Energy: \\( E = -\frac{1}{2}\sum_{i,j} w_{i,j} s_i s_j  + \sum_i \theta_i s_i \\), s: state of unit, w: connection weight, \\( \theta \\): threshold
+ \\( s_i = +1 \\) if \\( \sum_j w_{i,j}s_j \geq \theta_i \\), otherwise \\( s_i = -1 \\)
+ Physics analog: Ising model 

## Boltzmann Machine  

![Boltzmannexample](/static/posts/simple_neural_network_models/Boltzmannexample.png)

+ A form a recurrent artificial neural network (RNN)  
+ A generative, stochastic counter part of Hopfield Network
+ Energy: \\( E = -(\frac{1}{2}\sum_{i,j} w_{i,j} s_i s_j  + \sum_i \theta_i s_i) \\), 
+ s: state of unit, w: connection weight, \\( \theta \\): threshold
+ Application: with unconstrained connectivity, has no proven useful application for practical problems

## Restricted Boltzmann Machine(RBM, 1986)  

![Restricted_Boltzmann_machine](/static/posts/simple_neural_network_models/Restricted_Boltzmann_machine.png)

+ Variant of Boltzmann Machine 
+ No inter connections between neurons on the same layer 
+ Energy: \\( E(v,h) = -\sum_i a_i v_i - \sum_j b_j h_j - \sum_i \sum_j v_i w_{i,j} h_j \\)
+ v: visiable units, h: hidden units, w: connection weights
+ Application: so many... 




