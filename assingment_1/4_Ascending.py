try:
    expected_count = int(input("Enter the number of values: "))
    numbers = [
        int(value.strip())
        for value in input("Enter comma-separated numbers: ").split(",")
    ]
except ValueError:
    print("Please enter a whole-number count and valid whole numbers.")
else:
    if expected_count < 0:
        print("The number of values cannot be negative.")
    elif len(numbers) != expected_count:
        print(f"Error: enter exactly {expected_count} numbers.")
    else:
        print("Numbers in ascending order:", sorted(numbers))
