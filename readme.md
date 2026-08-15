*Problem statement* 
Going to Gikomba to shop for items can be cumbersome and tedious exercise for a shopper in Nairobi. Congestion of both cars and people, mud when it rains, just to name a few.

*Proposed solution*
I seek to develop an e-commerce website that brings the customer closer to goods and items sold by vendors and retailors in the Gikomba market. This will make it easier for consumers who do not wish to make it physically to the market while having their goods conveniently delivered to their doorstep. It will also give retailors a platform to market their products while broadening their customer base.


*DATABASE SYNTAX*
1.CREATE TABLE users (
 id SERIAL PRIMARY KEY, 
 name VARCHAR(100)NOT NULL,
 email VARCHAR(255)UNIQUE NOT NULL,
 password VARCHAR(255)NOT NULL,
 role VARCHAR (20) NOT NULL DEFAULT 'customer',
 CONSTRAINT valid_user_role
 CHECK(role IN('customer','employee','admin','vendor'))
);


2.CREATE TABLE branches(
 id SERIAL PRIMARY KEY,
 name VARCHAR(100)NOT NULL,
 location VARCHAR(255)NOT NULL
);


3.CREATE TABLE departments(
 id SERIAL PRIMARY KEY,
 b_id INTEGER NOT NULL,

 CONSTRAINT fk_department_branch
   FOREIGN KEY (b_id)
   REFERENCEs branches(id)
);


4.CREATE TABLE employees(
 id SERIAL PRIMARY KEY,
 user_id INTEGER NOT NULL,
 dep_id INTEGER NOT NULL,

 CONSTRAINT fk_employee_department
  FOREIGN KEY(dep_id)
  REFERENCES departments(id)
);


5.CREATE TABLE customers(
 id SERIAL PRIMARY KEY,
 user_id INTEGER NOT NULL,

 CONSTRAINT fk_customer_user
 FOREIGN KEY (user_id)
 REFERENCES users(id)
);



6.CREATE TABLE vendors(
 id SERIAL PRIMARY KEY,
 user_id INTEGER NOT NULL UNIQUE,
 CONSTRAINT fk_vendor_user
  FOREIGN KEY(user_id)
  REFERENCES users(id) 
);


7.CREATE TABLE stores(
 id SERIAL PRIMARY KEY,
 b_id INTEGER NOT NULL,
 CONSTRAINT fk_store_branch
 FOREIGN KEY (b_id)
 REFERENCES branches (id)
);


8.CREATE TABLE categories(
 id SERIAL PRIMARY KEY
);


9.CREATE TABLE products(
 id SERIAL PRIMARY KEY,
 v_id INTEGER NOT NULL,
 ca_id INTEGER NOT NULL,
 CONSTRAINT fk_product_vendor
 FOREIGN KEY (ca_id)
 REFERENCES categories(id)
);


10.CREATE TABLE inventory (
 id SERIAL PRIMARY KEY,
 prod_id INTEGER NOT NULL,
 s_id INTEGER NOT NULL,
 CONSTRAINT fk_inventory_store
 FOREIGN KEY (s_id)
 REFERENCES stores(id)
);


11.CREATE TABLE pickup_station(
 id SERIAL PRIMARY KEY,
 st_id INTEGER NOT NULL,
 CONSTRAINT fk_pickup_store
 FOREIGN KEY (st_id)
 REFERENCES stores(id)
);


12.CREATE TABLE orders (
 id SERIAL PRIMARY KEY,
 c_id INTEGER NOT NULL,
 e_id INTEGER NOT NULL,

 CONSTRAINT fk_order_customer
 FOREIGN KEY(c_id)
 REFERENCES customers(id),

 CONSTRAINT fk_order_employee
 FOREIGN KEY (e_id)
 REFERENCES employees (id)
);


13.CREATE TABLE order_details(
 id SERIAL PRIMARY KEY,
 o_id INTEGER NOT NULL,
 pr_id INTEGER NOT NULL,

 CONSTRAINT fk_order_details_order
 FOREIGN KEY (o_id)
 REFERENCES orders (id),
 
 CONSTRAINT fk_order_details_product
 FOREIGN KEY (pr_id)
 REFERENCES products(id)
);


14.CREATE TABLE payments(
 id SERIAL PRIMARY KEY,
 o_id INTEGER NOT NULL,
 
 CONSTRAINT fk_payment_order
 FOREIGN KEY (o_id)
 REFERENCES orders(id)
);


15.CREATE TABLE deliveries (
 id SERIAL PRIMARY KEY,
 o_id INTEGER NOT NULL,
 p_id INTEGER NOT NULL,
 
 CONSTRAINT fk_delivery_order
 FOREIGN KEY (o_id)
 REFERENCES orders(id),

 CONSTRAINT fk_delivery_pickup
 FOREIGN KEY (p_id)
 REFERENCES pickup_station(id)
);


16.CREATE TABLE shipping (
 id SERIAL PRIMARY KEY,
 o_id INTEGER NOT NULL,

 CONSTRAINT fk_shipping_order
 FOREIGN KEY (o_id)
 REFERENCES orders(id)
);
 
 17.CREATE TABLE carts (
 id SERIAL PRIMARY KEY,
 user_id INTEGER NOT NULL UNIQUE,

 CONSTRAINT fk_cart_user
  FOREIGN KEY (user_id)
  REFERENCES users(id)
);


18.CREATE TABLE cart_items (
 id SERIAL PRIMARY KEY,
 cart_id INTEGER NOT NULL,
 product_id INTEGER NOT NULL,
 quantity INTEGER NOT NULL DEFAULT 1,

 CONSTRAINT fk_cart_item_cart
 FOREIGN KEY (cart_id)
 REFERENCES carts(id),

 CONSTRAINT fk_cart_item_product
 FOREIGN KEY (product_id)
 REFERENCES products(id),
 
 CONSTRAINT positive_quantity
 CHECK (quantity > 0),

 CONSTRAINT unique_cart_product
 UNIQUE(cart_id, product_id)
);


19.CREATE TABLE reviews (
 id SERIAL PRIMARY KEY,
 user_id INTEGER NOT NULL,
 product_id INTEGER NOT NULL,
 rating INTEGER NOT NULL,
 comment TEXT,
 created_at TIMESTAMP DEFAULT
 CURRENT_TIMESTAMP,

 CONSTRAINT fk_review_user
 FOREIGN KEY (user_id)
 REFERENCES users(id),

 CONSTRAINT fk_review_product
 FOREIGN KEY (product_id)
 REFERENCES products(id),

 CONSTRAINT valid_rating
 CHECK (rating BETWEEN 1 AND 5),

 CONSTRAINT unique_user_product_review
 UNIQUE (user_id,product_id)
);



















































































 




















































 




