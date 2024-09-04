def analyze_array(arr):
    if not arr:
        return None, None, 0
    
    minimum = min(arr)
    maximum = max(arr)
    odd_count = sum(1 for num in arr if num % 2 != 0)
    
    return minimum, maximum, odd_count

# Example usage
example_array = [3, 7, 2, 8, 1, 9, 4, 6, 5]
min_val, max_val, odd_count = analyze_array(example_array)

print(f"Array: {example_array}")
print(f"Minimum: {min_val}")
print(f"Maximum: {max_val}")
print(f"Number of odd numbers: {odd_count}")