import numpy as np
from sklearn.linear_model import Ridge
from scipy.ndimage import gaussian_filter1d

def compute_memory_capacity(spike_rates, target_signal, max_delay=30, alpha=1e-3):
    """Computes Jaeger's memory capacity for delays k = 1 to max_delay."""
    smoothed_rates = gaussian_filter1d(spike_rates, sigma=3, axis=0)
    X = smoothed_rates
    
    capacities = []
    delays = range(1, max_delay + 1)
    
    for k in delays:
        # Target is input delayed by k steps
        y = target_signal[max_delay : len(X)]
        X_sub = X[max_delay - k : len(X) - k]
        
        # Align lengths
        min_len = min(len(y), len(X_sub))
        y_trim = y[:min_len]
        X_trim = X_sub[:min_len]
        
        model = Ridge(alpha=alpha)
        model.fit(X_trim, y_trim)
        preds = model.predict(X_trim)
        
        # Variance of target and residual variance
        var_y = np.var(y_trim)
        if var_y == 0:
            mc = 0.0
        else:
            mse = np.mean((y_trim - preds) ** 2)
            mc = max(0.0, 1.0 - (mse / var_y))
        capacities.append(mc)
        
    total_mc = sum(capacities)
    return list(delays), capacities, total_mc