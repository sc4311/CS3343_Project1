def n_doors_puzzle(n):
    # Initialize the doors
    doors = [False] * n

    # Iterate over the range n times
    for i in range(n):
        # Toggle the doors
        for j in range(i, n, i + 1):
            doors[j] = not doors[j]

    # Store the door numbers in a separate list
    open_doors = [i + 1 for i, door in enumerate(doors) if door]

    # Apply the FizzBuzz logic to the open doors only
    for i in range(len(open_doors)):
        if open_doors[i] % 3 == 0 and open_doors[i] % 5 == 0:
            open_doors[i] = "FizzBuzz"
        elif open_doors[i] % 3 == 0:
            open_doors[i] = "Fizz"
        elif open_doors[i] % 5 == 0:
            open_doors[i] = "Buzz"
        else:
            open_doors[i] = open_doors[i]

    return open_doors


# Test the function
print("Test 1: When n = 20")
print("N Doors Puzzle's Fizz Buzz Implementation:",n_doors_puzzle(20))
print("Test 2: When n = 100")
print("N Doors Puzzle's Fizz Buzz Implementation:", n_doors_puzzle(100))
print("Test 3: When n = 257")
print("N Doors Puzzle's Fizz Buzz Implementation:", n_doors_puzzle(257))