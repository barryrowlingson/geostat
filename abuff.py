
from rootfind import bisect

def abuff(g, A, tol, maxiter=30):
    """ 
    return buffer width w such that g.buffer(w).area == A, within tolerance
    """
    def f(x):
        return g.buffer(x).area

    return bisect(f, 0, wmax, tol, maxiter)
