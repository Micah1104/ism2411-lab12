# I used AI as an explainer for this code, I wasn't getting a proper output for exeercise 5 so I pasted my code into claude and asked if there were any bugs. After checking the code I realized it was a typo with the threshold in "if total > 1000" it was supposed to be 100.
import csv
from datetime import datetime

SALES_FILE = "data/sales.csv"
CLEANED_FILE = "data/cleaned.csv"
LOG_FILE = "data/run_log.txt"

print("--exercise 1--")

with open(SALES_FILE, "r") as f:
    print(f"opened {SALES_FILE}.")

print("--exercise 2--")

with open(SALES_FILE, "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

print("--exercise 3--")

with open(SALES_FILE, "r") as f:
    reader = csv.reader(f)
    header = next(reader)
    print(f"Header: {header}")
    for row in reader:
        print(row)

print("--exercise 4--")

total_revenue = 0
with open(SALES_FILE, "r") as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        product, price_str, qty_str = row
        price = float(price_str)
        quantity = int(qty_str)
        total = price * quantity
        total_revenue += total
        print(f"{product}: {quantity} units x ${price:.2f} = ${total:.2f}")
print("--exercise 5--")
high_value = []
rows_read = 0
total_revenue = 0
with open(SALES_FILE, "r") as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        rows_read += 1
        product, price_str, qty_str = row
        price = float(price_str)
        quantity = int(qty_str)
        total = price * quantity
        total_revenue += total
        if total > 100:
            high_value.append([product, f"{price:.2f}", quantity, f"{total:.2f}"])

with open(CLEANED_FILE, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Product", "Price", "Quantity", "Total"])
    for row in high_value:
        writer.writerow(row)
print(f"wrote {len(high_value)} of {rows_read} rows to {CLEANED_FILE}")

print("--exercise 6--")

dict_total = 0
with open(SALES_FILE, "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        price = float(row["price"])
        quantity = int(row["quantity"])
        total = price * quantity
        dict_total += total
        print(f"{row['product']}: {quantity} units x ${price:.2f} = ${total:.2f}")

print("--exercise 7--")
summary ={}
with open(SALES_FILE, "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        product = row["product"]
        total= float(row["price"]) * int(row["quantity"])
        summary[product] = summary.get(product, 0) + total
for product in sorted(summary):
    print(f"{product}: ${summary[product]:.2f}")

print("--exercise 8--")

timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
with open(LOG_FILE, "a") as f:
    f.write(f"{timestamp} total revenue: ${total_revenue:.2f}\n")

entries = 0
with open(SALES_FILE, "r") as f:
    for line in f:
        entries += 1
        print(line.strip())

    print(f"Total entries: {entries}")

#reflection questions
#1. With python you can read more lines of data than you can in excel. You can also log when the script is run and any other relevant data.
#2. A business situation where you would use appened mode is if you wanted to track customer transactions. You could use apppend mode to create a log of an individuals transactions.