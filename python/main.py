from golden_search import golden_search

def func(x):
    return 2*x / (4 + (0.8 *x) + (x**2) + (0.2 * (x**3)))

def main():
    min_val = 0
    max_val = 20
    function_output, x_val, iteration = golden_search(func, min_val, max_val)
    print(function_output, x_val, iteration)

if __name__ == '__main__':
    main()