def stats(numbers):
    avg = sum(numbers) / len(numbers)
    max_val = max(numbers)
    min_val = min(numbers)
    return avg, max_val, min_val

values = [10, 20, 30, 40]
average, high, low = stats(values)

print(f"Average={average}, Max={high}, Min={low}")