def series_sum(n):
    """Sum series of nth terms."""
    counter, result = 1, 1
    if n == 0: return '0.00'
    for i in range(1, n):
        result += 1 / (counter + 3)
        counter += 3
    result = str(round(float(result), 2))
    result = result if len(result) >= 4 else result + '0'
    return result
