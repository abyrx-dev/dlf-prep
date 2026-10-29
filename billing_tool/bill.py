import csv

total = 0

with open("sales.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        amount = int(row["qty"]) * int(row["price"])
        print(f"{row['item']}: {amount}")
        total += amount

print(f"Total: {total}")
