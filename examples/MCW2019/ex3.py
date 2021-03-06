from sageopt import standard_poly_monomials, infer_domain, poly_solrec, poly_constrained_relaxation
import numpy as np

n = 7
x = standard_poly_monomials(n)
f = 0
for i in range(n):
    sel = np.ones(n, dtype=bool)
    sel[i] = False
    f -= 64 * np.prod(x[sel])
gts = [0.25 - x[i]**2 for i in range(n)]  # -0.5 <= x[i] <= 0.5 for all i.
X = infer_domain(f, gts, [])
dual = poly_constrained_relaxation(f, gts=[], eqs=[], form='dual', p=0, q=1, ell=0, X=X)
dual.solve(verbose=False, solver='MOSEK')
print()
solns = poly_solrec(dual)
for sol in solns:
    print(sol)
