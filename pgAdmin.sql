-- 1-masala --
select extract(month from orders.order_date),
count(distinct orders.order_id) from orders, order_details, products
where orders.order_id = order_details.order_id and order_details.product_id = products.product_id
and products.category_id = 1 and products.unit_price > 10 and extract(year from orders.order_date) = 1996
group by extract(month from orders.order_date)
group by extract(month from orders.order_date)

-- 2-masala --
select distinct suppliers.company_name
from suppliers, products, order_details, orders where suppliers.supplier_id = products.supplier_id
and products.product_id = order_details.product_id and order_details.order_id = orders.order_id
and products.category_id = 3 and products.unit_price = (select min(unit_price)
from products where category_id = 3)
and extract(year from orders.order_date) = 1997 and extract(month from orders.order_date) = 7

-- 3-masala --
select distinct employees.first_name, employees.last_name
from employees, orders where employees.employee_id = orders.employee_id
and extract(year from orders.order_date) = 1998 and extract(month from orders.order_date) = 3

-- 4-masala --
select categories.category_name, sum(order_details.quantity)
from categories, products, order_details, orders where categories.category_id = products.category_id
and products.product_id = order_details.product_id and order_details.order_id = orders.order_id
and products.unit_price = ( select max(unit_price) from products where category_id = categories.category_id)
and extract(year from orders.order_date) = 1996 group by categories.category_name

-- 5-masala --
select distinct suppliers.company_name from suppliers, products, order_details, orders, customers
where suppliers.supplier_id = products.supplier_id
and products.product_id = order_details.product_id and order_details.order_id = orders.order_id
and orders.customer_id = customers.customer_id and suppliers.country = 'USA' and customers.country = 'USA'
and extract(year from orders.order_date) = 1997

-- 6-masala --
select distinct employees.first_name, employees.last_name from employees, orders, order_details, products
where employees.employee_id = orders.employee_id and orders.order_id = order_details.order_id
and order_details.product_id = products.product_id and products.category_id = 5
and extract(year from orders.order_date) = 1997

-- 7-masala --
select customers.city, extract(month from orders.order_date),
count(orders.order_id) from customers, orders
where customers.customer_id = orders.customer_id and customers.country = 'usa'
and extract(year from orders.order_date) = 1997
group by customers.city, extract(month from orders.order_date)
order by customers.city, extract(month from orders.order_date);

