#!/usr/bin/env python3

def fuzzbizz(n):
    """
    FizzBuzz implementation that returns:
    - "Fizz" for multiples of 3
    - "Buzz" for multiples of 5
    - "FizzBuzz" for multiples of both 3 and 5
    - The number itself for all other cases
    """
    if n % 15 == 0:
        return "FizzBuzz"
    elif n % 3 == 0:
        return "Fizz"
    elif n % 5 == 0:
        return "Buzz"
    else:
        return str(n)


def main():
    """Run FizzBuzz for numbers 1 to 100"""
    print("FizzBuzz from 1 to 100:")
    print("-" * 30)
    
    for i in range(1, 101):
        print(f"{i:3d}: {fuzzbizz(i)}")


if __name__ == "__main__":
    main()