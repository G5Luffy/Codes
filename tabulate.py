from tabulate import tabulate

data = [
    ["Alice", 24, "Engineer"],
    ["Bob", 30, "Doctor"],
    ["Charlie", 22, "Artist"],
    ["David", 28, "Teacher"]
]

headers = ["Name", "Age", "Occupation"]

print(tabulate(data, headers, tablefmt="pretty"))