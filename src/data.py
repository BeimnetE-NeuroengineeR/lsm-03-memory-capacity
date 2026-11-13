import numpy as np

def generate_memory_input(duration=20.0, dt=0.1, seed=42):
    """Generates a uniformly distributed random input stream for memory capacity tests."""
    np.random.seed(seed)
    time = np.arange(0, duration, dt)
    # Uniform white noise in [-1, 1]
    signal = np.random.uniform(-1.0, 1.0, len(time))
    return time, signal