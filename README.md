# Industrial Benchmark light

The "Industrial Benchmark light" covers a large number of aspects that we have identified as essential for industrial applications. It was designed as a simplified variant of the "Industrial Benchmark" [1,2]. While the "Industrial Benchmark" (IB) has the same level of difficulty and complexity as real RL applications, the Industrial benchmark light (IBlight) corresponds more to the difficulty of simple industrial RL tasks.  State and action space are continuous, the state space is not as high dimensional as in the IB, but likewise only partially observable. The actions consist of two continuous components and act on two controls. 
The optimization task is multiobjective in the sense that there are two reward components that have opposite dependencies on the actions. The dynamic behavior is heteroscedastic with state-dependent observation noise and state-dependent probability distributions based on latent variables. 
Each specific choice is based on our experience with industrial challenges.

[1] Daniel Hein et al., A benchmark environment motivated by industrial control problems, 2017
[2] https://github.com/siemens/industrialbenchmark
