# Dirichlet Process non-linear State-Space Mixture (DPnSSM) Algorithm

Using a novel approach DPnSSM to cluster time series data with non-linear dynamics. This work is based heavily on this [github repository ](https://github.com/ds2p/state-space-mixture) and this [paper](http://proceedings.mlr.press/v89/lin19b.html). I attempt to understand and replicate the results and use the algorithm to perform analysis (clustering) on new data not used in the project.

# Overview
1. Model multiple time series data as the output of a Dirichlet Process Mixture for non-linear state space models. The Dirichlet process models an infinite dimensional probability distribution to describe the behaviour of a dynamic system from a population which has the presence of subpopulations given by a mixture model. The Dirichlet process integrates the Chinese Restaurant Process (CRP) which allows us to separate closing clusters from choosing hidden parameter for each cluster. This allows us to perform the inference without having prior knowledge on the number of clusters, a priori<br>
2. Use a Metropolis within Gibbs algorithm to derive a full Bayesian inference that alternates between sampling cluster assignments and sampling parameter valves that form the basis of cluster <br>

