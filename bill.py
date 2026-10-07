def calculate_tip(bill, percent):
    return bill * percent / 100


def split(total, people):
    return total / people


bill = float(input("Bill total: "))
percent = float(input("Tip %: "))
people = int(input("Number of people: "))

tip = calculate_tip(bill, percent)
total = bill + tip
each = split(total, people)

print(f"Tip: {tip:,.2f}")
print(f"Total: {total:,.2f}")
print(f"Each pays: {each:,.2f}")
