def fibonacci(n):
    fib_series = [0, 1]
    for i in range(2, n):
        next_num = fib_series[-1] + fib_series[-2]
        fib_series.append(next_num)
    return fib_series


num_terms = int(input("Enter the number of terms in the Fibonacci series: "))
fib_series = fibonacci(num_terms)
print("Fibonacci series:", fib_series)
