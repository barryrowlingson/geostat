
from rootfind import bisect

def abuff(g, A, wmax, tol, maxiter=30):
    """ 
    return buffer width w such that g.buffer(w).area == A, within tolerance
    """
    def f(x):
        return float(g.buffer(x).area) - A

    result = bisect(f, 0, wmax, tol, maxiter)

    return {
        'geometry': g.buffer(result['x']),
        'A': result['fx'] + A,
        'Astar': A,
        'error': result['fx'],
        'width': result['x'],
        'iterations': result['i']
}
    

