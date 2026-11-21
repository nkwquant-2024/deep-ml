
import math

def bidding_mc(bid, value, low, high, n, antithetic=False):
    def van_der_corput(i):
        u = 0.0
        factor = 0.5

        while i > 0:
            u += (i % 2) * factor
            i //= 2
            factor *= 0.5

        return u

    def payoff(u):
        reserve = low + u * (high - low)
        return value - bid if bid >= reserve else 0.0

    samples = []

    for i in range(1, n + 1):
        u = van_der_corput(i)

        if antithetic:
            p = (payoff(u) + payoff(1 - u)) / 2
        else:
            p = payoff(u)

        samples.append(p)

    estimate = sum(samples) / n

    if n < 2:
        standard_error = 0.0
    else:
        variance = sum((x - estimate) ** 2 for x in samples) / (n - 1)
        standard_error = math.sqrt(variance / n)

    return estimate, standard_error