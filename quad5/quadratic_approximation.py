import pymc as pm
import numpy as np
from pymc.step_methods.arraystep import ArrayStep
from pymc.util import get_value_vars_from_user_vars


class QuadraticApproximation(ArrayStep):
    def __init__(self, vars, model, **kwargs):
        self.model = model
        self.vars = vars
        self.varnames = [var.name for var in vars]

        # Compute mode and covariance
        self.mode, self.covariance = self._compute_mode_and_covariance()

        vars = get_value_vars_from_user_vars(vars, model)

        # Create necessary function sets for pymc
        super().__init__(vars, [self._logp_fn], **kwargs)

    def _point_to_array(self, point):
        return np.array([point[varname] for varname in self.varnames])

    def _array_to_point(self, array):
        return {varname: val for varname, val in zip(self.varnames, array)}

    def _logp_fn(self, x):
        point = self._array_to_point(x)
        return self.model.logp(point)

    def _compute_mode_and_covariance(self):
        # Find the MAP estimate (mode of the posterior)
        map = pm.find_MAP(vars=self.vars)

        m = pm.modelcontext(None)

        for var in self.vars:
            if m.rvs_to_transforms[var] is not None:
                m.rvs_to_transforms[var] = None
                # change name so that we can use `map[var]` value
                var_value = m.rvs_to_values[var]
                var_value.name = var.name

        H = pm.find_hessian(map, vars=self.vars)
        cov = np.linalg.inv(H)
        mean = np.concatenate([np.atleast_1d(map[v.name]) for v in self.vars])

        return mean, cov

    def astep(self, q0, logp):
        # Generate a sample from the multivariate Gaussian approximation
        sample = np.random.multivariate_normal(self.mode, self.covariance)
        return sample, []
