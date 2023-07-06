# Dirichlet Process non-linear State-Space Mixture (DPnSSM) Algorithm

Using a novel approach DPnSSM to cluster time series data with non-linear dynamics. This work is based heavily on this [github repository ](https://github.com/ds2p/state-space-mixture) and this [paper](http://proceedings.mlr.press/v89/lin19b.html). I attempt to understand and replicate the results and use the algorithm to perform analysis (clustering) on new data not used in the project.

# Overview
1. Model multiple time series data as the output of a Dirichlet Process Mixture for non-linear state space models. The Dirichlet process models an infinite dimensional probability distribution to describe the behaviour of a dynamic system from a population which has the presence of subpopulations given by a mixture model. The Dirichlet process integrates the Chinese Restaurant Process (CRP) which allows us to separate closing clusters from choosing hidden parameter for each cluster. This allows us to perform the inference without having prior knowledge on the number of clusters, a priori<br>
2. Use a Metropolis within Gibbs algorithm to derive a full Bayesian inference that alternates between sampling cluster assignments and sampling parameter valves that form the basis of cluster <br>

# Custom

First I replicate the main results in the paper. Then I generate some random data, one with prior knowledge of the existence of cluster(s) and one without (just random). The algorithm is able to cluster and divide the population into sub groups. Results are shown below.

 Clusters                            | No sub populations, 1 cluster                
----------------------------------- | ----------------------------------- 
![output](https://github.com/cyrilakafia/clustering-time-series/assets/79414187/b5407eef-4315-4210-9ac5-7844d623e77a) | ![output_1](https://github.com/cyrilakafia/clustering-time-series/assets/79414187/27ff9e21-6988-40ed-964e-e8c5c470323d) 

# Noteworthy

The algorithm works for time series that are in a very specific format in terms of data shape and data type, continuous or discrete. 
