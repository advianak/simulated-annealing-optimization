# Simulated Annealing Optimization

A stochastic optimization project implementing the Simulated Annealing algorithm from scratch in Python to solve complex non-convex optimization problems.

---
sample

## Overview

This project explores the behavior of Simulated Annealing, a probabilistic optimization algorithm inspired by thermodynamic cooling processes in physics.

The system searches for near-optimal solutions on the highly multi-modal **Rastrigin function**, a benchmark optimization problem known for containing many local minima that commonly trap greedy algorithms.

Unlike deterministic optimization methods, Simulated Annealing allows controlled acceptance of worse solutions during early exploration stages, enabling the algorithm to escape local minima and continue searching globally for better solutions.

The project investigates:

* stochastic optimization behavior
* cooling schedule effects
* convergence vs exploration tradeoffs
* local minima avoidance
* randomized search stability
* parameter sensitivity analysis

---

# Optimization Pipeline

```text
┌─────────────────────────────┐
│ Random Initial Solution     │
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│ Generate Neighbor Solution  │
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│ Evaluate Objective Function │
│     (Rastrigin Function)    │
└──────────────┬──────────────┘
               │
      Better Solution?
         ┌─────┴─────┐
         │           │
        YES         NO
         │           │
         ▼           ▼
┌─────────────┐  ┌─────────────────────┐
│ Accept Move │  │ Probabilistic       │
│ Immediately │  │ Acceptance Check    │
└──────┬──────┘  └─────────┬───────────┘
       │                    │
       └─────────┬──────────┘
                 ▼
┌─────────────────────────────┐
│ Reduce Temperature          │
│ Using Cooling Schedule      │
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│ Converge Toward Best State  │
└─────────────────────────────┘
```

---

## Objective Function

The optimization target is the two-dimensional **Rastrigin function**, a highly non-linear benchmark function frequently used in optimization research.

### Why Rastrigin?

The function contains:

* many local minima
* highly rugged search landscapes
* strong non-convexity
* difficult optimization regions

This makes it an excellent benchmark for evaluating stochastic optimization algorithms.

---

## Simulated Annealing Strategy

The algorithm begins with:

* a random solution
* high exploration temperature
* stochastic neighbor generation

At each iteration:

1. A nearby candidate solution is generated
2. The objective value is evaluated
3. Better solutions are accepted immediately
4. Worse solutions may still be accepted probabilistically

The probability of accepting worse solutions decreases over time as the system cools.

This enables:

* early exploration
* local minima escape
* late-stage convergence

---

## Cooling Schedule Experiments

The project evaluates multiple cooling schedules:

| Cooling Rate | Behavior                               |
| ------------ | -------------------------------------- |
| 0.99         | Faster convergence, less exploration   |
| 0.995        | Balanced exploration and convergence   |
| 0.999        | Slower cooling, stronger global search |

Experimental analysis showed that slower cooling schedules consistently produced lower objective values and improved optimization performance.

---

## Experimental Results

The algorithm was evaluated across multiple randomized runs to analyze stochastic consistency.

### Observations

* Rapid objective reduction during early iterations
* Stable convergence behavior over time
* Strong sensitivity to cooling rate selection
* Successful escape from local minima
* Consistent near-optimal solutions across repeated trials

The optimization curves demonstrated:

* exploration during high temperatures
* gradual convergence during cooling
* stabilization near low objective regions

---

## Visualizations

The project generates:

* best objective value per run
* convergence curves over iterations
* temperature decay graphs
* cooling rate comparison charts

These plots help visualize:

* optimization dynamics
* stochastic variability
* convergence efficiency
* parameter tuning effects

---

## Technologies

* Python
* NumPy
* Matplotlib
* Simulated Annealing
* Stochastic Optimization
* Physics-Based Optimization

---

## Repository Structure

```text
simulated-annealing-optimization/
│
├── main.py
├── README.md
├── visualizations/
│   ├── convergence_curve.png
│   ├── cooling_rate_comparison.png
│   └── temperature_decay.png
└── report/
```

---

## Key Concepts Demonstrated

* Stochastic Search
* Simulated Annealing
* Metaheuristic Optimization
* Cooling Schedules
* Exploration vs Exploitation
* Local Minima Escape
* Non-Convex Optimization

---

## Learning Outcomes

This project strengthened understanding of:

* probabilistic optimization algorithms
* stochastic decision-making systems
* cooling schedule design
* optimization parameter tuning
* randomized search strategies
* convergence analysis
* non-convex optimization landscapes

---

## Future Improvements

Potential future extensions include:

* adaptive cooling schedules
* higher-dimensional optimization
* hybrid genetic + annealing optimization
* parallel stochastic search
* benchmark comparisons against PSO and GA
* neural optimization integration

---

## Author

Adviana Kirubalin
Arizona State University
Computer Science & Data Science
