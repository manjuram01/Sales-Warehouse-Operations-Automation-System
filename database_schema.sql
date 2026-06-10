CREATE DATABASE swa_automation;
USE swa_automation;

CREATE TABLE Products (
    Product_ID VARCHAR(10) PRIMARY KEY,
    Product_Name VARCHAR(100),
    Category VARCHAR(50),
    Unit_Price INT,
    Supplier VARCHAR(100)
);

CREATE TABLE Customers (
    Customer_ID VARCHAR(10) PRIMARY KEY,
    Customer_Name VARCHAR(100),
    Customer_Type VARCHAR(50),
    City VARCHAR(50)
);

CREATE TABLE Inventory (
    Product_ID VARCHAR(10),
    Product_Name VARCHAR(100),
    Current_Stock INT,
    Reorder_Level INT,
    Warehouse VARCHAR(50),

    FOREIGN KEY (Product_ID)
    REFERENCES Products(Product_ID)
);

CREATE TABLE Orders (
    Order_ID VARCHAR(10) PRIMARY KEY,
    Customer_ID VARCHAR(10),
    Product_ID VARCHAR(10),
    Quantity INT,
    Order_Date DATE,
    Status VARCHAR(50),

    FOREIGN KEY (Customer_ID)
    REFERENCES Customers(Customer_ID),

    FOREIGN KEY (Product_ID)
    REFERENCES Products(Product_ID)
);

CREATE TABLE Shipments (
    Shipment_ID VARCHAR(10) PRIMARY KEY,
    Order_ID VARCHAR(10),
    Dispatch_Date DATE,
    Delivery_Date DATE,
    Shipment_Status VARCHAR(50),

    FOREIGN KEY (Order_ID)
    REFERENCES Orders(Order_ID)
);