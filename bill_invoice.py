def generate_bill(customer_name, items, tax_rate=0.07):
    print("\n" + "=" * 50)
    print(f"{' ' * 15}INVOICE{' ' * 15}")
    print("=" * 50)
    print(f"Customer: {customer_name}")
    print(f"Date: {__import__('datetime').datetime.now().strftime('%Y-%m-%d')}")
    print("-" * 50)
    
    print(f"{'Item':<30}{'Qty':<10}{'Price':<10}{'Total':<10}")
    print("-" * 50)
    
    subtotal = 0
    for item_name, quantity, price in items:
        item_total = quantity * price
        subtotal += item_total
        print(f"{item_name:<30}{quantity:<10}${price:<9.2f}${item_total:<9.2f}")
    
    tax = subtotal * tax_rate
    total = subtotal + tax
    
    print("-" * 50)
    print(f"{'Subtotal:':<40}${subtotal:<9.2f}")
    print(f"{'Tax (' + str(tax_rate * 100) + '%):':<40}${tax:<9.2f}")
    print(f"{'Total:':<40}${total:<9.2f}")
    print("=" * 50)
    print("Thank you for your business!")
    print("=" * 50)


if __name__ == "__main__":
    customer = "John Doe"
    purchased_items = [
        ("Laptop", 1, 1299.99),
        ("Mouse", 2, 24.50),
        ("Keyboard", 1, 59.99),
        ("HDMI Cable", 3, 12.99)
    ]
    
    generate_bill(customer, purchased_items)