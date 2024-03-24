menu = [("Samosa", 15), ("Idli", 30), ("Maggie", 50), ("Dosa", 70), ("Tea", 10), ("Coffee", 20), ("Sandwich", 35), ("ColdDrink", 25)]

for i, item in enumerate(menu):
    print(f"{i+1}. {item[0]}: Rs {item[1]}")


order = []
bill = 0

while True:
    
    item_ord = input()

    if not item_ord:
        break

    
    
    item_numb, item_quan = map(int, item_ord.split())


    item_name, item_price = menu[item_numb-1]

    order.append((item_name, item_quan, item_price))


    bill += item_price * item_quan


for item in order:
    print(f"{item[0]}, {item[1]}, Rs {item[1]*item[2]}")

print(f"TOTAL, {sum(item[1] for item in order)} items, Rs {bill}")

