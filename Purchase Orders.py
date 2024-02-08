# Global dictionary to store purchase orders
purchase_orders = {}


def create_purchase_order(po_num):
    FY1, FY2,  = 2023, 2024
    vendor = input("Enter vendor name: ")
    item = input("Enter item name: ")
    quantity = int(input("Enter quantity: "))
    unit_price = float(input("Enter unit price: "))

    # Generate a unique purchase order number
    order_number = str(f'Company_Name/{FY1}-{FY2}/0{po_num}')

    # Calculate total cost
    cost = quantity * unit_price
    total_cost = cost * 1.18

    # Store the purchase order in the dictionary
    purchase_orders[order_number] = {
        'vendor': vendor,
        'item': item,
        'quantity': quantity,
        'unit_price': unit_price,
        'total_cost': total_cost
    }

    print(f"Purchase Order created successfully. Order Number: {order_number}")


def view_purchase_order(order_number):
    if order_number in purchase_orders:
        order_details = purchase_orders[order_number]
        print(f"Purchase Order {order_number} Details:")
        for key, value in order_details.items():
            print(f"{key}: {value}")
    else:
        print("Purchase Order not found.")


def update_purchase_order(order_number):
    if order_number in purchase_orders:
        print("Update Purchase Order:")
        item = input("Enter updated item name (press Enter to keep the existing value): ")
        quantity = int(input("Enter updated quantity (press Enter to keep the existing value): "))
        unit_price = float(input("Enter updated unit price (press Enter to keep the existing value): "))

        # Update purchase order details
        if item:
            purchase_orders[order_number]['item'] = item
        if quantity:
            purchase_orders[order_number]['quantity'] = quantity
        if unit_price:
            purchase_orders[order_number]['unit_price'] = unit_price

        # Update total cost
        purchase_orders[order_number]['total_cost'] = purchase_orders[order_number]['quantity'] * \
                                                      purchase_orders[order_number]['unit_price']

        print("Purchase Order updated successfully.")
    else:
        print("Purchase Order not found.")


def list_all_purchase_orders():
    print("List of All Purchase Orders:")
    for order_number, order_details in purchase_orders.items():
        print(
            f"Order Number: {order_number}, Vendor: {order_details['vendor']}, Total Cost: {order_details['total_cost']}")


def delete_purchase_order(order_number):
    if order_number in purchase_orders:
        del purchase_orders[order_number]
        print(f"Purchase Order {order_number} deleted successfully.")
    else:
        print("Purchase Order not found.")


run_time = True
PO_num = 1
while run_time:
    print('---------------------------------------\n'
          'To create a New Purchase Order, Enter 1 \n'
          'To view all Purchase Orders, Enter 2 \n'
          'To View a Specific Purchase Order, Enter 3 \n'
          'To Update a Purchase Order, Enter 4 \n'
          'To Delete a Purchase Order, Enter 9 \n'
          'To Exit, Enter 0\n'
          '------------------------------')
    po_command=int(input('Enter the command: '))
    if po_command == 1:
        create_purchase_order(PO_num)
        PO_num += 1
    elif po_command == 2:
        list_all_purchase_orders()
    elif po_command == 3:
        order_number_to_view = input("Enter the Order Number to view details: ")
        view_purchase_order(order_number_to_view)
    elif po_command == 4:
        order_number_to_update = input("Enter the Order Number to update details: ")
        update_purchase_order(order_number_to_update)
    elif po_command == 9:
        order_number_to_delete = input("Enter the Order Number to delete: ")
        delete_purchase_order(order_number_to_delete)
    elif po_command == 0:
        run_time = False
    else:
        raise ValueError('Invalid Command')