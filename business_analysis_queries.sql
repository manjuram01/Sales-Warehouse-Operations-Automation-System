-- Question 1: How many total orders have been placed?

SELECT COUNT(*) AS Total_Orders
FROM Orders;


-- Question 2: What is the total quantity of products sold?

SELECT SUM(Quantity) AS Total_Units_Sold
FROM Orders;


-- Question 3: Which products are the top-selling products based on units sold?

SELECT
    p.Product_Name,
    SUM(o.Quantity) AS Units_Sold
FROM Orders o
JOIN Products p
ON o.Product_ID = p.Product_ID
GROUP BY p.Product_Name
ORDER BY Units_Sold DESC;


-- Question 4: Which cities generate the highest revenue?

SELECT
    c.City,
    SUM(o.Quantity * p.Unit_Price) AS Revenue
FROM Orders o
JOIN Customers c
ON o.Customer_ID = c.Customer_ID
JOIN Products p
ON o.Product_ID = p.Product_ID
GROUP BY c.City
ORDER BY Revenue DESC;


-- Question 5: Which products are currently below their reorder level?

SELECT
    Product_Name,
    Current_Stock,
    Reorder_Level
FROM Inventory
WHERE Current_Stock < Reorder_Level;


-- Question 6: Which customer orders are currently delayed?

SELECT
    Order_ID,
    Status
FROM Orders
WHERE Status = 'Delayed';


-- Question 7: Which shipments are currently delayed?

SELECT
    Shipment_ID,
    Shipment_Status
FROM Shipments
WHERE Shipment_Status = 'Delayed';


-- Question 8: What is the distribution of customers by customer type?

SELECT
    Customer_Type,
    COUNT(*) AS Total_Customers
FROM Customers
GROUP BY Customer_Type;


-- Question 9: What is the daily revenue trend over time?

SELECT
    Order_Date,
    SUM(o.Quantity * p.Unit_Price) AS Daily_Revenue
FROM Orders o
JOIN Products p
ON o.Product_ID = p.Product_ID
GROUP BY Order_Date
ORDER BY Order_Date;


-- Question 10: Which customers place the highest number of orders?

SELECT
    c.Customer_Name,
    COUNT(o.Order_ID) AS Total_Orders
FROM Orders o
JOIN Customers c
ON o.Customer_ID = c.Customer_ID
GROUP BY c.Customer_Name
ORDER BY Total_Orders DESC;