SELECT * FROM products;


SELECT name FROM categories;


SELECT * FROM products ORDER BY price DESC LIMIT 1;


SELECT * FROM products ORDER BY price ASC LIMIT 1;


SELECT * FROM products WHERE price > 50000;


SELECT * FROM sales ORDER BY sale_date ASC LIMIT 10;


SELECT * FROM sales WHERE quantity > 3;


SELECT * FROM sales WHERE total_amount > 100000;


SELECT * FROM products WHERE name LIKE '%Книга%';


SELECT * FROM sales WHERE sale_date::date = '2023-05-15';



SELECT COUNT(*) AS total_categories FROM categories;


SELECT COUNT(*) AS total_products FROM products;


SELECT AVG(price) AS average_price FROM products;


SELECT SUM(total_amount) AS total_revenue FROM sales;


SELECT MAX(total_amount) AS max_check_amount FROM sales;


SELECT MIN(total_amount) AS min_check_amount FROM sales;


SELECT SUM(quantity) AS total_quantity_sold FROM sales;


SELECT product_id, SUM(quantity) AS total_qty
FROM sales
GROUP BY product_id;


SELECT product_id, SUM(total_amount) AS total_revenue
FROM sales
GROUP BY product_id;


SELECT product_id, SUM(total_amount) AS total_revenue
FROM sales
GROUP BY product_id
HAVING SUM(total_amount) > 1000000;


SELECT sale_date::date AS sale_day, COUNT(*) AS sales_count
FROM sales
GROUP BY sale_date::date
ORDER BY sale_day;


SELECT sale_date::date AS sale_day, SUM(total_amount) AS daily_revenue
FROM sales
GROUP BY sale_date::date
ORDER BY daily_revenue DESC
LIMIT 1;



SELECT p.name AS product_name, c.name AS category_name
FROM products p
JOIN categories c ON p.category_id = c.category_id;


SELECT s.sale_id, p.name AS product_name, s.sale_date, s.quantity, s.total_amount
FROM sales s
JOIN products p ON s.product_id = p.product_id;


SELECT c.name AS category_name, SUM(s.total_amount) AS total_revenue
FROM sales s
JOIN products p ON s.product_id = p.product_id
JOIN categories c ON p.category_id = c.category_id
GROUP BY c.name;


SELECT c.name AS category_name, AVG(s.total_amount) AS avg_check
FROM sales s
JOIN products p ON s.product_id = p.product_id
JOIN categories c ON p.category_id = c.category_id
GROUP BY c.name
ORDER BY avg_check DESC
LIMIT 1;


SELECT s.sale_date, p.name AS product_name, c.name AS category_name, s.total_amount
FROM sales s
JOIN products p ON s.product_id = p.product_id
JOIN categories c ON p.category_id = c.category_id;


SELECT p.name
FROM products p
LEFT JOIN sales s ON p.product_id = s.product_id
WHERE s.sale_id IS NULL;


SELECT * FROM products
WHERE price > (SELECT AVG(price) FROM products);


SELECT p.name AS product_name, c.name AS category_name, SUM(s.total_amount) AS total_revenue
FROM sales s
JOIN products p ON s.product_id = p.product_id
JOIN categories c ON p.category_id = c.category_id
GROUP BY p.name, c.name
ORDER BY total_revenue DESC
LIMIT 3;