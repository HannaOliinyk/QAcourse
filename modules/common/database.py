import sqlite3

class Database():
    def __init__(self):
        self.connection = sqlite3.connect(r'/Users/anna/cat_folder/QAcourse' + r'/become_qa_auto.db')
        self.cursor = self.connection.cursor()

    def test_connection(self):
        sqlite_select_Query = "SELECT sqlite_version();"
        self.cursor.execute(sqlite_select_Query)
        record = self.cursor.fetchall()
        print(f"Connected successfully. SQLite Database Version is: {record}")

    def get_all_users(self):
        query = "SELECT name, address, city FROM customers"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record
    
    def get_user_address_by_name(self, name):
        query = f"SELECT address, city, postalCode, country FROM customers WHERE name = '{name}'"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record
    
    def update_product_qnt_by_id(self, product_id, qnt):
        if qnt < 0:
            raise ValueError("Кількеість не може бути від'ємною")
        query = f"UPDATE products SET quantity = {qnt} WHERE id = {product_id}"
        self.cursor.execute(query)
        self.connection.commit()

    def select_product_qnt_by_id(self, product_id):
        query = f"SELECT quantity FROM products WHERE id = {product_id}"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record
    
    def insert_product(self, product_id, name, description, qnt):
        query = f"INSERT OR REPLACE INTO products (id, name, description, quantity) \
              VALUES ({product_id}, '{name}', '{description}', {qnt})"
        self.cursor.execute(query)
        self.connection.commit()

    def delete_product_by_id(self, product_id):
        query = f"DELETE FROM products WHERE id = {product_id}"
        self.cursor.execute(query)
        self.connection.commit()

    def get_detailed_orders(self):
        query = f"SELECT orders.id, customers.name, products.name, products.description, \
            orders.order_date \
            FROM orders \
            JOIN customers ON orders.customer_id = customers.id \
            JOIN products ON orders.product_id = products.id"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record
    def insert_new_customer(self, customer_id, name, address, city, postalCode, country):
        query = f"INSERT OR REPLACE INTO customers(id, name, address, city, postalCode, country)\
            VALUES ({customer_id}, '{name}', '{address}', '{city}', {postalCode},'{country}')"
        self.cursor.execute(query)
        self.connection.commit()
    
    def update_change_of_contact_information(self, city, customer_id):
        query = f"UPDATE customers SET city = '{city}' WHERE id = {customer_id}"
        self.cursor.execute(query)
        self.connection.commit()
        return self.get_users(customer_id)
    
    def get_users(self, customer_id):
        query = f"SELECT * FROM customers WHERE id = {customer_id}"
        self.cursor.execute(query)
        records = self.cursor.fetchall()
        return records
    
    def get_products_with_negative_quantity(self):
        query = f"SELECT * FROM products WHERE quantity < 0"
        self.cursor.execute(query)
        products = self.cursor.fetchall()
        return products
    
    def add_new_order(self, id, customer_id, product_id, order_date):
        if product_id is not None:
            query = f"INSERT OR REPLACE INTO orders (id, customer_id, product_id, order_date)\
                VALUES ({id}, {customer_id}, {product_id},'{order_date}')"
            self.cursor.execute(query)
            self.connection.commit()
        else:
            raise ValueError('Invalid product_id')