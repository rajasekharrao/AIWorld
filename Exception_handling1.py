try:
    result = 1/0
except ZeroDivisionError as ec:
    print(ec)
    print("Enter denominator greater than 0")
except Exception as Ef:
    print(Ef)
else:
    print(f"The result is {result}")
finally:
    print("Execution ")

