import csv
import os

FILENAME = 'furniture_sales.csv'
FIELDS = ['id', 'customer_name', 'product', 'quantity', 'price']

def initialize_csv():
    if not os.path.exists(FILENAME):
        with open(FILENAME, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=FIELDS)
            writer.writeheader()

def create_sale(sale):
    with open(FILENAME, 'a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=FIELDS)
        writer.writerow(sale)

def read_sales():
    with open(FILENAME, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(row)

def update_sale(sale_id, updated_data):
    rows = []
    with open(FILENAME, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['id'] == sale_id:
                row.update(updated_data)
            rows.append(row)

    with open(FILENAME, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(rows)

def delete_sale(sale_id):
    rows = []
    with open(FILENAME, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['id'] != sale_id:
                rows.append(row)

    with open(FILENAME, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(rows)

if __name__ == '__main__':
    initialize_csv()

    # Create furniture sales records
    create_sale({'id': '1', 'customer_name': 'Tanvi Menon', 'product': 'Dining Table', 'quantity': '1', 'price': '25000'})
    create_sale({'id': '2', 'customer_name': 'Rahul Bansal', 'product': 'Sofa Set', 'quantity': '1', 'price': '40000'})
    create_sale({'id': '3', 'customer_name': 'Ishita Jain', 'product': 'Bookshelf', 'quantity': '2', 'price': '12000'})
    create_sale({'id': '4', 'customer_name': 'Ajay Shetty', 'product': 'Office Chair', 'quantity': '3', 'price': '18000'})
    create_sale({'id': '5', 'customer_name': 'Rekha Yadav', 'product': 'Wardrobe', 'quantity': '1', 'price': '35000'})

    print("\n🔹 Initial Furniture Sales:")
    read_sales()

    # Update and delete examples
    update_sale('2', {'quantity': '2', 'price': '80000'})
    delete_sale('4')

    print("\n🔹 After Update and Delete:")
    read_sales()
