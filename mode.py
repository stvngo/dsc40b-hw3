def mode(numbers):
    counts = {}

    for num in numbers:
        counts[num] = counts.get(num, 0) + 1

    max_count = max(counts.values())
    modes = [num for num, count in counts.items() if count == max_count]
    return modes[0]