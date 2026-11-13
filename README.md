# Spiking Reservoir Memory Capacity (`lsm-03-memory-capacity`)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.14+](https://img.shields.io/badge/python-3.14%2B-blue.svg)](https://www.python.org/)
[![Brian2](https://img.shields.io/badge/Simulator-Brian2-orange.svg)](https://brian2.readthedocs.io/)

> *Evaluating short-term memory performance and information processing capacity (Jaeger, 2002) in a spiking Leaky Integrate-and-Fire reservoir.*

---

## Overview

![Main Result](figures/main_result.png)

This project measures the temporal memory capacity of the spiking network by tasking linear readouts with reconstructing past input values $u(t-k)$ across increasing time delays $k$.

---

## Quick Execution

```bash
pip install -r requirements.txt
PYTHONPATH=. python3 scripts/run_experiment.py