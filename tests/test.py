import unittest

import numpy as np
import pymc as pm

from quad5.quadratic_approximation import QuadraticApproximation


class TestQuap(unittest.TestCase):
    # Example originates from Bayesian Data Analyses, 3rd Edition
    # By Andrew Gelman, John Carlin, Hal Stern, David Dunson,
    # Aki Vehtari, and Donald Rubin.
    # See section. 4.1
    def test_analytical_solution_against_quadratic_approx(
        self,
    ):
        y = np.array([2642, 3503, 4358], dtype=np.float64)
        n = y.size

        with pm.Model() as m:
            logsigma = pm.Uniform("logsigma", 1, 100)
            mu = pm.Uniform("mu", 0, 10000)
            _ = pm.Normal("y", mu=mu, sigma=pm.math.exp(logsigma), observed=y)
            custom_step = QuadraticApproximation([mu, logsigma], m)
            _ = pm.sample(draws=1000, chains=4, tune=100, step=custom_step)

        bda_map = [y.mean(), np.log(y.std())]
        bda_cov = np.array([[y.var() / n, 0], [0, 1 / (2 * n)]])

        assert np.allclose(custom_step.mode, bda_map)
        assert np.allclose(custom_step.covariance, bda_cov, atol=1e-3)


if __name__ == "__main__":
    unittest.main()
