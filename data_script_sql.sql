-- 1. La fecha con el mayor número de pedidos
CREATE INDEX IF NOT EXISTS idx_order_created_date ON order_full_information (order_created_date);

SELECT 
    order_created_date, 
    COUNT(order_id) AS total_orders
FROM 
    order_full_information
GROUP BY 
    order_created_date
ORDER BY 
    total_orders DESC
LIMIT 1;

-- 2. El producto más demandado
CREATE INDEX IF NOT EXISTS idx_product_name ON order_full_information (product_name);

SELECT 
    product_name, 
    SUM(quantity) AS total_quantity
FROM 
    order_full_information
GROUP BY 
    product_name
ORDER BY 
    total_quantity DESC
LIMIT 1;

-- 3. Las 3 categorías más demandadas
CREATE INDEX IF NOT EXISTS idx_category ON order_full_information (category);

SELECT 
    category, 
    SUM(quantity) AS total_quantity
FROM 
    order_full_information
GROUP BY 
    category
ORDER BY 
    total_quantity DESC
LIMIT 3;