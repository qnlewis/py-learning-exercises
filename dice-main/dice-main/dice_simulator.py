import argparse
import random
import statistics
from collections import Counter

def parse_arguments():
    parser = argparse.ArgumentParser(description="Simulate dice rolls and analyze results.")
    parser.add_argument("--dice", type=int, default=1, help="Number of dice per roll")
    parser.add_argument("--faces", type=int, default=6, help="Number of faces on each die")
    parser.add_argument("--rolls", type=int, default=1000, help="Number of dice roll simulations")
    parser.add_argument("--weights", type=str, default=None, help="Comma-separated weights for each face")
    parser.add_argument("--bins", type=int, default=None, help="Number of bins for histogram grouping")
    return parser.parse_args()

def load_weights(weights_str, faces):
    if weights_str is None:
        return [1] * faces
    weights = list(map(float, weights_str.split(',')))
    if len(weights) != faces:
        raise ValueError(f"Expected {faces} weights, got {len(weights)}")
    return weights

def simulate_dice_rolls(num_dice, faces, num_rolls, weights):
    outcomes = []
    for _ in range(num_rolls):
        total = sum(random.choices(range(1, faces + 1), weights=weights, k=num_dice))
        outcomes.append(total)
    return outcomes

def print_frequency_distribution(outcomes):
    freq = Counter(outcomes)
    print("Frequency Distribution:")
    print(f"{'Outcome':<8}{'Frequency'}")
    for outcome in sorted(freq):
        print(f"{outcome:<8}{freq[outcome]}")
    print("\n")

def print_histogram(outcomes, bins=None):
    freq = Counter(outcomes)
    min_val, max_val = min(freq), max(freq)

    if bins is None or bins > (max_val - min_val + 1):
        bins = max_val - min_val + 1

    bin_ranges = []
    bin_width = (max_val - min_val + 1) / bins
    for i in range(bins):
        start = int(round(min_val + i * bin_width))
        end = int(round(min_val + (i + 1) * bin_width)) - 1
        if i == bins - 1:
            end = max_val
        bin_ranges.append((start, end))

    print("Histogram:")
    for start, end in bin_ranges:
        count = sum(freq.get(outcome, 0) for outcome in range(start, end + 1))
        bar = '*' * (count // 5) if count > 0 else ''
        print(f"{start}-{end:<4} : {bar} ({count})")
    print("\n")

def compute_summary_stats(outcomes):
    mean = round(statistics.mean(outcomes), 2)
    median = statistics.median(outcomes)
    try:
        mode = statistics.mode(outcomes)
    except statistics.StatisticsError:
        mode = "Multiple modes"
    variance = round(statistics.variance(outcomes), 2)
    std_dev = round(statistics.stdev(outcomes), 2)
    return { 'mean': mean, 'median': median, 'mode': mode, 'variance': variance, 'std_dev': std_dev}

def main():
    args = parse_arguments()
    weights = load_weights(args.weights, args.faces)

    outcomes = simulate_dice_rolls(args.dice, args.faces, args.rolls, weights)

    print_frequency_distribution(outcomes)

    print_histogram(outcomes, args.bins)

    stats = compute_summary_stats(outcomes)
    print(f"Mean: {stats['mean']}")
    print(f"Median: {stats['median']}")
    print(f"Mode: {stats['mode']}")
    print(f"Variance: {stats['variance']}")
    print(f"Standard Deviation: {stats['std_dev']}")

if __name__ == "__main__":
    main()