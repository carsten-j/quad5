# Quadratic Approximation

Modern Bayesian data analysis is based on efficient Markov Chain Monte Carlo (MCMC) techniques. 

Learning Bayesian statistic can be hard for a Frequentist! The [Statistical Rethinking](https://xcelab.net/rm/) book by Richard McElreath tries to avoid cognitive overload for its readers by not requireing them to learn Bayesian statistics and MCMC at the same time. The posterior distribution is in most interesting cases analytically intractable and hence MCMC is used to numerically determine it.

As a simpler alternative to MCMC one can you Quadratic Approximation[^1]. A lot of people has ported the R code examples from Statistical Rethinking to Python using frameworks like PYMC, Pyro, NumPyro, and TensorFlow Probability. Apparently there is no Quadratic Approximation solution available for PYMC[^2]. Numpyro has [AutoLaplaceApproximation](https://num.pyro.ai/en/latest/autoguide.html#numpyro.infer.autoguide.AutoLaplaceApproximation)[^3] but it is not clear to me that this is the same as Quadratic Approximation.

quad5 leverages [PYMC](https://www.pymc.io/welcome.html) and works by adding a custom step for the sample method on PYMC models. By doing so it benefits from standard PYMC functionality that automatically adds constant, deterministic, and observed data to the 
[inferencedata](https://python.arviz.org/en/stable/getting_started/WorkingWithInferenceData.html) output from the sample method. This allows for easy usage of the [Arviz](https://www.arviz.org/en/latest/) visualization library for posterior distributions and more general the ecosystem around PYMC.

## Word of warning
This package is not production-grade code. It is primarily meant for educational purposes. Secondary for the author to learn more about the internals of the PYMC library.

I am quite sure there will be valid PYMC models where this package not is able to produce a quadratic approximation for the posterior distribution. You are more than welcome to submit either a PR or create a issue for such cases.

## Example
``` python

        import arviz as az
        import numpy as np
        import pymc as pm
        import quad5 as quad5

        y = np.array([2642, 3503, 4358], dtype=np.float64)

        with pm.Model() as m:
            logsigma = pm.Uniform("logsigma", 1, 100)
            mu = pm.Uniform("mu", 0, 10000)
            _ = pm.Normal("y", mu=mu, sigma=pm.math.exp(logsigma), observed=y)
            custom_step = quad5.QuadraticApproximation([mu, logsigma], m)
            trace = pm.sample(draws=1000, chains=4, tune=100, step=custom_step)

        az.plot_posterior(trace)    
```

![Posterior Distribution](https://github.com/carsten-j/quad5/blob/98d36e3a79434c226b70301165fc95f656a7334f/images/posterior.png)

See more examples in this [notebook](https://colab.research.google.com/github/carsten-j/Rethinking/blob/main/chapter4.ipynb) with examples from chapter 4 in Statistical Rethinking.

[^1]: [The Bernstein-Von Mises Theorem](https://en.wikipedia.org/wiki/Bernstein%E2%80%93von_Mises_theorem) states that under some regularity conditions the posterior distribution is asymptotically normal. If the distribution is unimodal with most of the probability mass located symmetric around the peak then quite often you will get a faily good approximation using Quadratic Approximation.

[^2]: This work is partly based on the Python package [pymc3-quap](https://github.com/rasmusbergpalm/pymc3-quap) but pymc3-quap is based on PYMC3 and a lot happend bewteen version 3 and 5 of PYMC. Optimizers works better when provided with a good initial guess and hence a (optional) starting point has been added to function arguments. Please see [Github](https://github.com/pymc-devs/pymc/issues/5443#issuecomment-1030609090) for a discussion about the differences between PYMC version 3 and 5 for computing the Hessian and in particular the for loop `for var in vars:` used when computing the Hessian.

[^3]:The NumPyro documentation refers to "Automatic Guide Generation" and as I understand it this is a kind
of variational inference of the posterior distribution.
