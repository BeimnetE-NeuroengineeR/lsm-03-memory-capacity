import os
import numpy as np
import matplotlib.pyplot as plt
from brian2 import run, second, ms, TimedArray

from src.data import generate_memory_input
from src.reservoir import build_memory_reservoir
from src.capacity import compute_memory_capacity

def main():
    print("Initializing Project 3: Memory Capacity Evaluation...")
    
    duration = 15.0
    dt = 0.1
    time, signal = generate_memory_input(duration=duration, dt=dt)
    
    n_neurons = 200
    neurons, synapses_rec, spike_monitor = build_memory_reservoir(n_neurons=n_neurons, dt=dt)
    
    print(f"Running Brian2 simulation for {duration} seconds...")
    run(duration * second)
    
    # Bin spike rates
    bin_size_ms = 10.0
    time_bins = np.arange(0, duration * 1000, bin_size_ms)
    spike_times = spike_monitor.t / ms
    spike_indices = spike_monitor.i
    
    hist, _ = np.histogramdd(
        sample=(spike_times, spike_indices),
        bins=(time_bins, np.arange(n_neurons + 1))
    )
    
    # Downsample target signal to match rate bins
    from scipy.signal import resample
    signal_resampled = resample(signal, len(hist))
    
    max_delay = 25
    delays, capacities, total_mc = compute_memory_capacity(hist, signal_resampled, max_delay=max_delay)
    print(f"Total Memory Capacity (MC): {total_mc:.4f}")
    
    # Plot & Save
    os.makedirs("figures", exist_ok=True)
    plt.figure(figsize=(9, 5))
    plt.bar(delays, capacities, color='tab:blue', alpha=0.8, edgecolor='black')
    plt.xlabel("Delay ($k$ steps)")
    plt.ylabel("Capacity ($MC_k$)")
    plt.title(f"Spiking Reservoir Memory Capacity Profile (Total MC = {total_mc:.2f})")
    plt.grid(axis='y', linestyle='--', alpha=0.5)
    plt.tight_layout()
    plt.savefig("figures/main_result.png", dpi=300)
    print("Saved memory capacity profile to figures/main_result.png")

if __name__ == "__main__":
    main()