import math
import random
import matplotlib.pyplot as plt

def rastrigin(x, y):
    return 20 + (x * x - 10 * math.cos(2 * math.pi * x)) + (y * y - 10 * math.cos(2 * math.pi * y))

def get_neighbor(x, y, step_size):
    new_x = x + random.uniform(-step_size, step_size)
    new_y = y + random.uniform(-step_size, step_size)
    new_x = max(-5.12, min(5.12, new_x))
    new_y = max(-5.12, min(5.12, new_y))

    return new_x, new_y

def simulated_annealing(cooling_rate=0.995):
    current_x = random.uniform(-5.12, 5.12)
    current_y = random.uniform(-5.12, 5.12)
    current_value = rastrigin(current_x, current_y)

    best_x = current_x
    best_y = current_y
    best_value = current_value

    temperature = 100.0
    min_temperature = 0.001
    step_size = 0.5
    max_iterations = 5000
    best_values = []
    temperatures = []

    for _ in range(max_iterations):
        if temperature < min_temperature:
            break

        new_x, new_y = get_neighbor(current_x, current_y, step_size)
        new_value = rastrigin(new_x, new_y)

        delta = new_value - current_value

        if delta < 0:
            current_x = new_x
            current_y = new_y
            current_value = new_value
        else:
            probability = math.exp(-delta / temperature)
            if random.random() < probability:
                current_x = new_x
                current_y = new_y
                current_value = new_value

        if current_value < best_value:
            best_x = current_x
            best_y = current_y
            best_value = current_value

        best_values.append(best_value)
        temperatures.append(temperature)
        temperature = temperature * cooling_rate

    return best_x, best_y, best_value, best_values, temperatures


def run_multiple_times(num_runs=10, cooling_rate=0.995):
    all_best_values = []
    last_best_values = None
    last_temperatures = None

    print(f"\nRunning simulated annealing {num_runs} times - ")
    print(f"Cooling rate = {cooling_rate}")
    print("-" * 40)

    for i in range(num_runs):
        best_x, best_y, best_value, best_values, temperatures = simulated_annealing(cooling_rate)

        print(f"Run {i + 1}")
        print(f"x = {best_x:.4f}")
        print(f"y = {best_y:.4f}")
        print(f"f(x, y) = {best_value:.6f}")
        print("-" * 40)

        all_best_values.append(best_value)
        last_best_values = best_values
        last_temperatures = temperatures

    average_value = sum(all_best_values) / len(all_best_values)
    best_value = min(all_best_values)
    worst_value = max(all_best_values)

    print("\nFINAL SUMMARY")
    print(f"Average best value: {average_value:.6f}")
    print(f"Best value: {best_value:.6f}")
    print(f"Worst value: {worst_value:.6f}")

    return all_best_values, last_best_values, last_temperatures


def compare_cooling_rates():
    cooling_rates = [0.99, 0.995, 0.999]
    averages = []

    print("\nCOMPARING COOLING RATES")
    print("=" * 40)

    for rate in cooling_rates:
        results, _, _ = run_multiple_times(num_runs=5, cooling_rate=rate)
        avg = sum(results) / len(results)
        averages.append(avg)
        print(f"Cooling rate {rate} average best value = {avg:.6f}")
        print("=" * 40)

    plt.figure(figsize=(8, 5))
    plt.bar([str(rate) for rate in cooling_rates], averages)
    plt.title("Average Best Value for Different Cooling Rates")
    plt.xlabel("Cooling Rate")
    plt.ylabel("Average Best Value")
    plt.grid(True)
    plt.show()


def main():
    all_best_values, best_values, temperatures = run_multiple_times(num_runs=10, cooling_rate=0.995)
    plt.figure(figsize=(8, 5))
    plt.plot(range(1, len(all_best_values) + 1), all_best_values, marker="o")
    plt.title("Best Value from Each Run")
    plt.xlabel("Run Number")
    plt.ylabel("Best Value")
    plt.grid(True)
    plt.show()

    plt.figure(figsize=(8, 5))
    plt.plot(best_values)
    plt.title("Best Objective Value Over Iterations")
    plt.xlabel("Iteration")
    plt.ylabel("Best Value Found")
    plt.grid(True)
    plt.show()

    plt.figure(figsize=(8, 5))
    plt.plot(temperatures)
    plt.title("Temperature Over Iterations")
    plt.xlabel("Iteration")
    plt.ylabel("Temperature")
    plt.grid(True)
    plt.show()

    compare_cooling_rates()


if __name__ == "__main__":
    main()