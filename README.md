# Quadratic Approximation

Modern Bayesian data analysis is based on efficient Markov Chain Monte Carlo (MCMC) techniques. 

Learning Bayesian statistic can be hard for a Frequentist! The [Statistical Rethinking](https://xcelab.net/rm/) book by Richard McElreath tries to avoid cognitive overload for its readers by not requireing them to learn Bayesian statistics and MCMC at the same time. The posterior distribution is in most interesting cases analytically intractable and hence MCMC is used to numerically determine it.

As a simpler alternative to MCMC one can you Quadratic Approximation[^1]. A lot of people has ported the R code examples from Statistical Rethinking to Python using frameworks like PYMC, Pyro, NumPyro, and TensorFlow Probability. Apparently there is no Quadratic Approximation solution available for PYMC[^2]. Numpyro has [AutoLaplaceApproximation](https://num.pyro.ai/en/latest/autoguide.html#numpyro.infer.autoguide.AutoLaplaceApproximation)[^3] but it is not clear to me that this is the same as Quadratic Approximation.

quad5 leverages [PYMC](https://www.pymc.io/welcome.html) and works by adding a custom step for the sample method on PYMC models. By doing so it benefits from standard PYMC functionality that automatically adds constant, deterministic, and observed data to the 
[inferencedata](https://python.arviz.org/en/stable/getting_started/WorkingWithInferenceData.html) output from the sample method. This allows for easy usage of the [Arviz](https://www.arviz.org/en/latest/) visualization library for posterior distributions and more general the ecosystem around PYMC.

## Word of warning
This package is not production-grade code. It is primarily meant for educational purposes. Secondary for the author to learn more about the internals of the PYMC library.

I am quite sure there will be valid PYMC models where this package not is able to produce a quadratic approximation for the posterior distribution. You are more than welcome to submit eihter PR's or createa issue for such cases.

## Example


add photo of model

and summary

See more examples ...

[^1]: The Bernstein-Von Mises Theorem states that under some regularity conditions 
the posterior distribution is asymptotically normal. Unimodal , most of the probability mass is located symmetric around the peak

[^2]: This work is partly based on the Python package [pymc3-quap](https://github.com/rasmusbergpalm/pymc3-quap) but pymc3-quap is based on PYMC3 and a lot happend bewteen version 3 and 5 of PYMC.

[^3]:foo