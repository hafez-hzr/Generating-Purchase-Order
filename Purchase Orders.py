# Import Pandas to Create Dataframes
import pandas as pd

# Global dictionary to store PO
purchase_orders = {}


def create_purchase_order():
    global FY1, FY2, PO_num
    vendor = input("Enter Vendor Name: ")
    no_of_items = int(input("Enter the number of Items: "))  # Getting Input the number of items in the PO
    tax = float(input("Enter the Tax Percentage: "))
    item, quantity, unit_price, cost, total_cost = [], [], [], [], []

    # For-Loop to get the details for N number of Items
    for i in range(no_of_items):
        item += [input("Enter Item Name: ")]
        quantity += [int(input("Enter Quantity: "))]
        unit_price += [float(input("Enter Unit Price: "))]
        cost += [quantity[i] * unit_price[i]]
        total_cost += [cost[i] * tax]

    # Generate a unique PO number
    order_number = str(f'Company_Name/{FY1}-{FY2}/0{PO_num}')
    PO_num += 1

    # Store the PO in the dictionary
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
        print(pd.DataFrame(order_details))


def update_purchase_order(order_number):
    if order_number in purchase_orders:
        print("Update Purchase Order:")
        tax = (float(input("Enter the Tax Percentage: ")))/100
        for i in range(len(purchase_orders[order_number]['item'])):
            # Update Item Names, Quantity, Unit Price and Total Cost
            purchase_orders[order_number]['item'][i] = input(f"Enter updated item {i + 1} "
                                                             f"name (press Enter to keep the existing value): ")
            purchase_orders[order_number]['quantity'][i] = int(input("Enter updated quantity "
                                                                     "(press Enter to keep the existing value): "))
            purchase_orders[order_number]['unit_price'][i] = int(input("Enter updated Unit Price "
                                                                       "(press Enter to keep the existing value): "))
            purchase_orders[order_number]['total_cost'][i] = purchase_orders[order_number]['quantity'][i] * \
                                                             purchase_orders[order_number]['unit_price'][i] * tax

        print("Purchase Order updated successfully.")
    else:
        print("Purchase Order not found.")


def list_all_purchase_orders():
    print("List of All Purchase Orders:")
    for order_number, order_details in purchase_orders.items():
        print(
            f"Order Number: {order_number}, Vendor: {order_details['vendor']}, "
            f"Total Cost: {order_details['total_cost']}")


def delete_purchase_order(order_number):
    if order_number in purchase_orders:
        del purchase_orders[order_number]
        print(f"Purchase Order {order_number} deleted successfully.")
    else:
        print("Purchase Order not found.")


def change_financial_year():
    global FY1, FY2, PO_num
    FY1 = int(input("Enter the Financial Year 1: "))
    FY2 = int(input("Enter the Financial Year 2: "))
    PO_num = 1
    print(f'Financial Years changed to {FY1}-{FY2}')


run_time = True
FY1, FY2, PO_num = 2023, 2024, 1
while run_time:
    print('\n---------------------------------------\n'
          'To create a New Purchase Order, Enter 1 \n'
          'To view all Purchase Orders, Enter 2 \n'
          'To View a Specific Purchase Order, Enter 3 \n'
          'To Update a Purchase Order, Enter 4 \n'
          'To Delete a Purchase Order, Enter 5 \n'
          'To Update the Financial Years, Enter 6\n'
          'To Exit, Enter 0\n'
          '------------------------------\n')
    po_command = int(input('Enter the command: '))
    if po_command == 1:
        create_purchase_order()
    elif po_command == 2:
        list_all_purchase_orders()
    elif po_command == 3:
        order_number_to_view = input("Enter the Order Number to view details: ")
        view_purchase_order(order_number_to_view)
    elif po_command == 4:
        order_number_to_update = input("Enter the Order Number to update details: ")
        update_purchase_order(order_number_to_update)
    elif po_command == 5:
        order_number_to_delete = input("Enter the Order Number to delete: ")
        delete_purchase_order(order_number_to_delete)
    elif po_command == 6:
        change_financial_year()
    elif po_command == 0:
        run_time = False
    else:
        raise ValueError('Invalid Command')
