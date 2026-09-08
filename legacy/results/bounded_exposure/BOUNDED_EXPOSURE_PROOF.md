# Bounded positive-exposure reversal: statement and proof

This supplement gives a new, purely analytic result. It uses no training or evaluation observations. The accompanying verifier enumerates synthetic rational policies, solves their finite polytopes exactly, and independently checks risk-constrained optima by linear programming.

## 1. Sharp geometric bound, including a row floor

Let the conditional exposure satisfy `0 < u <= w(X) <= v < infinity` almost surely. Put `T=E[w]`, `c(a)=E[a]`, and `d(a)=E[a w]/T` for any measurable randomized gate `0<=a(X)<=1`.

Consider two gates `a_R,a_W` satisfying

- `x=c(a_R)-c(a_W)>=0`,
- `y=d(a_W)-d(a_R)>=0`,
- `c(a_W)>=c0`, where `0<=c0<1`.

In particular, the ordering conditions hold whenever the gates respectively maximize row coverage and exposure coverage over the same nonempty feasible class. No assumption about loss estimation or a particular ratio-risk constraint is needed for the bound itself.

Define

```
D = (v-u)/(v+u),
A(x) = min((1-x)/2, 1-c0-x).
```

Then

```
y <= ((v-u) A(x) - u x)/(u+(v-u) A(x)).             (B1)
```

Consequently,

```
y <= (D-x)/(1-D x),                                (B2)
x <= min(D, (1-u/v)(1-c0)),
0 <= x,y <= D.                                     (B3)
```

For a fixed classifier with between one and `m` positive predictions per example in the evaluated population, take `u=1,v=m`. Each reversal gap is therefore at most `(m-1)/(m+1)`. The joint bound (B2) is stronger than applying these two individual bounds independently. For `m=2`, each gap is at most `1/3`, rather than the unrestricted bound `1`. If the actual exposure is in `[u,u(1+delta)]`, each gap is at most `delta/(2+delta)`; this is a quantitative statement about approximately constant positive exposure.

### Proof

Write `z=a_R-a_W` and decompose its positive and negative parts. Let

```
b=E[z_+], a=E[(-z)_+],
Q_-=E[(w-u)(-z)_+], Q_+=E[(w-u)z_+].
```

Then `b-a=x`, `a+b<=1`, and `T>=u+Q_-`. Also `z_+<=1-a_W`, so `b<=1-c(a_W)<=1-c0`. These give

```
a <= min((1-x)/2,1-c0-x)=A(x).
```

The assumed exposure ordering gives `Q_--Q_+-u x>=0`. Since `Q_+>=0` and `Q_-<=(v-u)a`, we obtain

```
y=(Q_--Q_+-u x)/T
 <=(Q_--u x)/(u+Q_-)
 <=((v-u)a-u x)/(u+(v-u)a).
```

For the first inequality, removing the nonnegative `Q_+` increases the numerator and replacing `T` by its lower bound decreases the denominator; the resulting numerator remains nonnegative. For the second, `(q-u x)/(u+q)` increases with `q>=0`, with derivative `u(1+x)/(u+q)^2>0`. Thus these substitutions do not treat correlated numerator and denominator bounds as independent.

For fixed `x>=0`, the last expression increases with `a`, with derivative `(v-u)u(1+x)/(u+(v-u)a)^2>=0`. Substituting `a<=A(x)` proves (B1). Substituting just `a<=(1-x)/2` gives (B2). The nonnegative right-hand side of (B1), together with both upper bounds on `a`, gives the two bounds on `x` in (B3). Finally (B2) is at most `D` for `x>=0` because `D<1`. This proves the result. When `u=v`, both ordered gaps must be zero.

## 2. Sharpness with a fixed multi-label classifier and independent randomized acceptance

The floor-aware bound (B1) is sharp in closure even for unique optima of ratio-risk constrained selection. This is a statement across a class of laws, not across all gates for one fixed law.

Fix any integer `m>=2`, risk cap `0<r<1`, and row floor `0<=c0<1`. Write `u=1,v=m` and

```
Xmax = min((m-1)/(m+1), (1-1/m)(1-c0)).
```

For any interior target gap `0<x<Xmax`, set

```
A=min((1-x)/2,1-c0-x),
amin=x/(m-1).
```

Then `A>amin`. Choose any `a` with `amin<a<A`, and define three positive context probabilities

```
p_K=k=1-2a-x, p_U=p=a+x, p_V=q=a.
```

Thus `k>0`, `p>q>0`, `m q>p`, and `k+q=1-a-x>=c0`. Choose a positive budget small enough that

```
0<B<min(r k, (1-r)p, (1-r)m q).
```

Define conditional exposure and false-positive count moments by

```
             K                 U                 V
w            1                 1                 m
ell          r-B/k             r+B/p             r m+B/q
```

All moments obey `0<=ell<=w`. They are realized by a fixed `m`-label classifier as follows: at `K,U` the classifier predicts just the first label positive; at `V` it predicts all `m` labels positive. Conditional on each context, make all predicted-positive labels false jointly with probability `ell/w`, and true otherwise. Nonpredicted labels can be false in both outcomes. Therefore `L` is the realized number of false positives and `W` the deterministic number of positive predictions, with the displayed conditional moments. The gate observes all context information and accepts or rejects the entire vector using a uniform random variable independent of the labels given context.

The signed conditional excesses are `(-B/k,B/p,B/q)`. Their probability-weighted masses are exactly `(-B,B,B)`. Every optimum accepts `K`, which both increases its utility and relaxes the cap. Conditional on accepting `K`, feasibility reduces to

```
a_U+a_V<=1.
```

The unique row optimum is `a_R=(1,1,0)` because `p>q`. The unique exposure optimum is `a_W=(1,0,1)` because `m q>p`. Both satisfy the row floor and saturate the risk cap `R=r`. Their gaps are

```
x=p-q,
y=(m q-p)/(1+(m-1)q)
 = ((m-1)a-x)/(1+(m-1)a).
```

Letting `a` increase to `A` approaches (B1). If `k=1-2A-x>0`, taking `a=A` attains (B1) exactly, with the exposure optimum at the row floor and both optima still unique. If `k` tends to zero, choose `B` to tend to zero with it; this preserves the displayed moment bounds and all strict optimizer inequalities at each finite approximation.

The endpoint `x=0` is approached through positive interior `x`, and `x=Xmax` is approached from below. At these limiting endpoints an objective can tie, so uniqueness is claimed for the approximating laws rather than for the degenerate endpoints. The full floor-aware boundary is consequently sharp in closure. With a nonbinding row floor, this specializes to the simpler envelope (B2).

The same algebra gives sharpness for any positive real `u<v` when arbitrary nonnegative ratio-loss/exposure laws are allowed: use exposures `(u,u,v)`, replace the common budget condition by `B<min(r u k,(1-r)u p,(1-r)v q)`, and set moments `(r u-B/k,r u+B/p,r v+B/q)`. The classifier construction itself uses integer positive-prediction counts, hence the specialization `u=1,v=m` above.

## 3. Why the proposed “if and only if” is not valid

### A fixed loss law

Constant positive conditional exposure makes `d(a)=c(a)` for every gate and therefore prevents strict reversal. Conversely, nonconstant exposure does not ensure strict reversal for a given loss law. For example, with probabilities `(1/3,1/3,1/3)`, exposure `(1,1,2)`, and loss identically zero, the accept-all gate is the unique optimum of both utilities at any positive cap. A less degenerate sufficient condition is that accepting every case already satisfies the cap: again both utilities reach their maximum at accept-all.

Thus nonconstant positive exposure is necessary but not sufficient for strict reversal in a fixed problem. The correct existence claim is that, for every integer `m>=2`, every `0<r<1`, and every `c0<1`, there exists a fixed whole-example multi-label classification law with a strict reversal. Section 2 proves this stronger constructive statement and quantifies its sharp limits.

### Even a universal statement over losses needs a support condition

A nonconstant exposure function on a fixed feature distribution is not by itself sufficient to guarantee that some conditional loss law produces a strict reversal. In a feature space with exactly two positive-probability atoms and positive exposures, both objectives accept every atom of nonpositive signed excess. If both atoms have nonpositive excess, both accept all. If both have positive excess, no positive-exposure gate satisfies the cap. Otherwise, after accepting the one nonpositive-excess atom, there is only one remaining positive-excess atom; both utilities accept it to the same maximal extent. A common row floor cannot create an opposing optimum. The verifier checks this argument on an exact rational grid, including nonconstant weights `(1,2)`.

Our three-context construction supplies a common source of slack and two paid alternatives with different exposures. This is a sufficient support structure; the manuscript does not claim an exhaustive characterization of all fixed supports and loss laws.

### Zero exposure and binary precision require separate treatment

The positive lower bound `u>0` is essential to the scope of (B1)-(B3). Ordinary binary precision has zero-exposure predicted-negative examples. In that case `w=0` also implies `ell=0`, so such examples can be completed to acceptance at no risk or exposure cost. If positive exposure is a constant `s` on the remaining support, this completion satisfies

```
c(a_plus)=P(w=0)+P(w>0) d(a).
```

This yields the common-optimum identity used in the manuscript. It does not imply that every ratio-risk problem with a constant positive-exposure subset avoids reversal: a zero-exposure context with positive loss is not neutral and cannot be included by this completion argument. Neither the bound nor the necessity statement above silently treats such contexts as free.

## 4. Verification record

Run `python code/verify_bounded_exposure.py`. Its default output is `reproduction_outputs/bounded_exposure_validation/BOUNDED_EXPOSURE_CHECKS.json`, separate from archived evidence.

The verifier checks:

- 1,662 exact ordered-policy comparisons, including fractional acceptance and positive row floors;
- 15 exact endpoint-weight instances attaining the unrestricted geometric envelope;
- 54 three-context laws with unique risk-constrained row and exposure optima, checked by rational vertex enumeration;
- 6 laws attaining the floor-aware envelope exactly with positive common mass;
- 122 independent numerical LP optimizations;
- an exact nonconstant-exposure/zero-loss counterexample;
- 274 feasible two-atom cases with a common optimum, with 158 additional cases having no positive-exposure feasible gate.

These checks supplement the analytic proof; they do not replace its general argument. They read no empirical prediction or outcome cache.
