import sympy as sp
from inspect import signature

def lambdify(eq:sp.Eq):
    expression = eq.rhs
    return sp.lambdify(list(expression.free_symbols),expression)

def run(function, inputs={}, **kwargs):
    """Run sympy lambda method
    This one accepts redundant extra parameters (which the sympy lambda does not)
    Warning! This slows down the execution significantly!!!

    Parameters
    ----------
    function : [type]
        [description]
    inputs : dict, optional
        [description], by default {}

    Returns
    -------
    [type]
        [description]
    """
    s = signature(function)
    kwargs.update(inputs)
    parameters = list(s.parameters.keys())
    args = [kwargs[parameter] for parameter in parameters]
    return function(*args)