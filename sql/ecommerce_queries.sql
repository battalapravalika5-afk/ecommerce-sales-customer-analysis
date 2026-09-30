-- E-Commerce Sales & Customer Analysis
-- Table name: ecommerce_sales

-- 1. Total sales
SELECT ROUND(SUM(Sales), 2) AS total_sales
FROM ecommerce_sales;

-- 2. Total profit
SELECT ROUND(SUM(Profit), 2) AS total_profit
FROM ecommerce_sales;

-- 3. Number of orders
SELECT COUNT(DISTINCT Order_ID) AS total_orders
FROM ecommerce_sales;

-- 4. Average order value
SELECT ROUND(AVG(Sales), 2) AS average_order_value
FROM ecommerce_sales;

-- 5. Sales by category
SELECT
    Category,
    COUNT(DISTINCT Order_ID) AS orders,
    ROUND(SUM(Sales), 2) AS total_sales,
    ROUND(SUM(Profit), 2) AS total_profit
FROM ecommerce_sales
GROUP BY Category
ORDER BY total_sales DESC;

-- 6. Sales by region
SELECT
    Region,
    ROUND(SUM(Sales), 2) AS total_sales,
    ROUND(SUM(Profit), 2) AS total_profit
FROM ecommerce_sales
GROUP BY Region
ORDER BY total_sales DESC;

-- 7. Top 10 products by sales
SELECT
    Product,
    ROUND(SUM(Sales), 2) AS total_sales,
    ROUND(SUM(Profit), 2) AS total_profit
FROM ecommerce_sales
GROUP BY Product
ORDER BY total_sales DESC
LIMIT 10;

-- 8. Top 10 customers by revenue
SELECT
    Customer_ID,
    COUNT(DISTINCT Order_ID) AS orders,
    ROUND(SUM(Sales), 2) AS total_sales
FROM ecommerce_sales
GROUP BY Customer_ID
ORDER BY total_sales DESC
LIMIT 10;

-- 9. Monthly sales
SELECT
    strftime('%Y-%m', Order_Date) AS month,
    ROUND(SUM(Sales), 2) AS monthly_sales
FROM ecommerce_sales
GROUP BY month
ORDER BY month;

-- 10. Products with positive profit
SELECT
    Product,
    ROUND(SUM(Sales), 2) AS sales,
    ROUND(SUM(Profit), 2) AS profit
FROM ecommerce_sales
GROUP BY Product
HAVING SUM(Profit) > 0
ORDER BY profit DESC;

-- 11. Discount analysis
SELECT
    ROUND(Discount * 100, 0) AS discount_percent,
    COUNT(*) AS orders,
    ROUND(AVG(Sales), 2) AS avg_sales,
    ROUND(AVG(Profit), 2) AS avg_profit
FROM ecommerce_sales
GROUP BY discount_percent
ORDER BY discount_percent;
