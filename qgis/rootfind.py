import numpy as np
import math

def bisect( f, a, b, ftol, maxiter ):
    """
    Usage: ( x, rate ) = bisect( f, a, b, ftol, maxiter )

    This function uses bisection to solve abs(f(x)) < ftol.

    This function requires that the function f(x) be already defined, and
    that its name be passed in as a string as the first argument.
    """
    x  = a
    fa = f( a )
    fb = f( b )
    
    # Make sure that (according to the Intermediate Value Theorem) the
    # specified interval does contain a root.

    if np.sign( fa ) == np.sign( fb ):
        raise ValueError("Interval [%f,%f] may not contain a root" % ( a, b ))

    # Initialize for the search.  Note that we try and minimize the number
    # of evaluations of f(x).  It is initially evaluated twice before the
    # iteration begins and then once during each iteration.  These extra
    # points are needed to start off the error calculation which compares
    # estimates of solutions just computed with previous estimates.

    x0 = x + x/2
    x1 = x + x

    k = 0
    
    while k <= maxiter:
        x2, x1, x0 = ( x1, x0, x )
        x = ( a + b ) / 2.0
        fx = f( x )
        max_error = abs( fx  )
        k = k + 1

        if max_error < ftol:
            break

        if np.sign( fa ) == np.sign( fx ):
            a, fa = ( x, fx )
        else:
            b = x

    if k > maxiter:
        raise ValueError("Error: exceeded %d iterations" % maxiter)

    return {'x': x, 'fx': fx, 'i': k }
