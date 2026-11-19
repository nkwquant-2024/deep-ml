import numpy as np

def simulate_dice_sum(num_rolls, seed=0):
    rng = np.random.RandomState(seed)
    d1 = rng.randint(1, 7, size=num_rolls)
    d2 = rng.randint(1, 7, size=num_rolls)
    simulation = d1+d2
    counts = np.bincount(simulation, minlength=12)
    empirical = counts[2:] / num_rolls
    s = np.arange(2, 13)
    theoretical = (6 - abs(s - 7)) /36
    return (empirical, theoretical)