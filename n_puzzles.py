def n_doors_puzzle(n):
    # Initialize the doors
    doors = [False] * n

    # Iterate over the range n times
    for i in range(n):
        # Toggle the doors
        for j in range(i, n, i + 1):
            doors[j] = not doors[j]
            print(f"i: {i + 1}; j:{j + 1}; step size: {i + 1}. Toggling door number {j + 1}.")

    print("Algorithm has finished.")
    print("\n")

    # Store the door numbers in two separate lists
    open_doors = [i + 1 for i, door in enumerate(doors) if door]
    closed_doors = [i + 1 for i, door in enumerate(doors) if not door]

    # Print the open doors first and then the closed ones
    for door in open_doors:
        print(f"Door number {door} remains open.")
    print("\n")
    print("\n")
    for door in closed_doors:
        print(f"Door number {door} remains closed.")


# Test the function
print("Test 1")
n_doors_puzzle(10)
print("\n")
print("\n")
print("\n")


print("Test 2")
n_doors_puzzle(20)
