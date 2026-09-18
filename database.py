import psycopg2

#establishing db connection
conn = psycopg2.connect(host='localhost',port=5432, user='postgres',password='Emali50',dbname='ecommerce')

#creating a cursor object to perform db operations
cur = conn.cursor()


def insert_user(user_details):
    cur.execute("insert into users (full_name, email, password, role) values (%s, %s, %s, %s)", user_details)
    conn.commit()



def check_user(email):
    cur.execute("select * from users where email = %s", (email))
    user = cur.fetchone()
    return user  



def insert_branch(branch_details):
    cur.execute("insert into branches (branch_name, branch_location) values (%s, %s)", branch_details)
    conn.commit()



def check_branch(branch_name):
    cur.execute("select * from branches where branch_name = %s", (branch_name))
    branch = cur.fetchone()
    return branch



def insert_department(department_details):
    cur.execute("insert into departments (department_name, branch_id) values (%s, %s)", department_details)
    conn.commit()



def check_department(department_name):
    cur.execute("select * from departments where department_name = %s", (department_name))
    department = cur.fetchone()
    return department



def insert_employee(employee_details):
    cur.execute("insert into employees (full_name, email, password, role, department_id) values (%s, %s, %s, %s, %s)", employee_details)
    conn.commit()



def check_employee(email):
    cur.execute("select * from employees where email = %s", (email))
    employee = cur.fetchone()
    return employee



def insert_customer(customer_details):
    cur.execute("insert into customers (full_name, email, password) values (%s, %s, %s)", customer_details)
    conn.commit()



def check_customer(email):
    cur.execute("select * from customers where email = %s", (email))
    customer = cur.fetchone()
    return customer



def insert_vendor(vendor_details):
    cur.execute("insert into vendors (full_name, email, password) values (%s, %s, %s)", vendor_details)
    conn.commit()



def check_vendor(email):
    cur.execute("select * from vendors where email = %s", (email))
    vendor = cur.fetchone()
    return vendor



def insert_store(store_details):
    cur.execute("insert into stores (store_name, store_location) values (%s, %s)", store_details)
    conn.commit()



def check_store(store_name):
    cur.execute("select * from stores where store_name = %s", (store_name))
    store = cur.fetchone()
    return store



def insert_category(category_details):
    cur.execute("insert into categories (category_name) values (%s)", category_details)
    conn.commit()



def check_category(category_name):
    cur.execute("select * from categories where category_name = %s", (category_name))
    category = cur.fetchone()
    return category



def insert_product(product_details):
    cur.execute("insert into products (product_name, product_description, product_price, category_id, store_id) values (%s, %s, %s, %s, %s)", product_details)
    conn.commit()



def check_product(product_name):
    cur.execute("select * from products where product_name = %s", (product_name))
    product = cur.fetchone()
    return product



def insert_inventory(inventory_details):
    cur.execute("insert into inventory (product_id, quantity) values (%s, %s)", inventory_details)
    conn.commit()



def check_inventory(product_id):
    cur.execute("select * from inventory where product_id = %s", (product_id))
    inventory = cur.fetchone()
    return inventory



def insert_order(order_details):
    cur.execute("insert into orders (customer_id, order_date, total_amount) values (%s, %s, %s)", order_details)
    conn.commit()



def check_order(order_id):
    cur.execute("select * from orders where order_id = %s", (order_id))
    order = cur.fetchone()
    return order



def insert_order_details(order_item_details):
    cur.execute("insert into order_details (order_id, product_id, quantity, price) values (%s, %s, %s, %s)", order_item_details)
    conn.commit()



def check_order_details(order_id):
    cur.execute("select * from order_details where order_id = %s", (order_id))
    order_details = cur.fetchall()
    return order_details



def insert_pickup_station(pickup_station_details):
    cur.execute("insert into pickup_stations (station_name, station_location) values (%s, %s)", pickup_station_details)
    conn.commit()



def check_pickup_station(station_name):
    cur.execute("select * from pickup_stations where station_name = %s", (station_name))
    pickup_station = cur.fetchone()
    return pickup_station



def insert_payment(payment_details):
    cur.execute("insert into payments (order_id, payment_date, payment_amount, payment_method) values (%s, %s, %s, %s)", payment_details)
    conn.commit()



def check_payment(payment_id):
    cur.execute("select * from payments where payment_id = %s", (payment_id))
    payment = cur.fetchone()
    return payment



def insert_shipping(shipping_details):
    cur.execute("insert into shipping (order_id, shipment_date, shipment_status) values (%s, %s, %s)", shipping_details)
    conn.commit()



def check_shipping(shipping_id):
    cur.execute("select * from shipping where shipment_id = %s", (shipping_id))
    shipping = cur.fetchone()
    return shipping



def insert_delivery(delivery_details):
    cur.execute("insert into deliveries (order_id, delivery_date, delivery_status) values (%s, %s, %s)", delivery_details)
    conn.commit()



def check_delivery(delivery_id):
    cur.execute("select * from deliveries where delivery_id = %s", (delivery_id))
    delivery = cur.fetchone()
    return delivery



def insert_cart(cart_details):
    cur.execute("insert into carts (customer_id, product_id, quantity) values (%s, %s, %s)", cart_details)
    conn.commit()



def check_cart(customer_id):
    cur.execute("select * from carts where customer_id = %s", (customer_id))
    cart = cur.fetchall()
    return cart



def insert_cart_item(cart_item_details):
    cur.execute("insert into cart_items (cart_id, product_id, quantity) values (%s, %s, %s)", cart_item_details)
    conn.commit()



def check_cart_item(cart_id):
    cur.execute("select * from cart_items where cart_id = %s", (cart_id))
    cart_items = cur.fetchall()
    return cart_items



def insert_review(review_details):
    cur.execute("insert into reviews (product_id, customer_id, review_text, review_rating) values (%s, %s, %s, %s)", review_details)
    conn.commit()



def check_review(product_id):
    cur.execute("select * from reviews where product_id = %s", (product_id))
    reviews = cur.fetchall()
    return reviews



