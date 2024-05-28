def factorial_iteration(n):
    result = 1
    for i in range(1, n + 1):
        result = result * i
    return result


def factorial_recursive(n):
    if n == 2:
        return 2
    return n * factorial_recursive(n - 1)


if __name__ == "__main__":
    print(factorial_recursive(5))
