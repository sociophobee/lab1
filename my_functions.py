def calculate_x(a, b):
    x = (a + b) / (a - b)
    return x


def pyramid(n):
    print("\nПіраміда:")

    for i in range(1, n + 1):
        for j in range(i):
            print(i, end=" ")
        print()