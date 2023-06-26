#W3 schools

# 1.SELECT o.OrderID,o.OrderDate,c.CustomerName,c.City,c.Address,c.PostalCode,s.ShipperName,p.ProductName,od.Quantity
# FROM Orders o
# JOIN Customers c ON o.CustomerID = c.CustomerID
# JOIN Shippers s ON o.ShipperID = s.ShipperID
# JOIN OrderDetails od ON o.OrderID = od.OrderID
# JOIN Products p ON od.ProductID = p.ProductID;
# 2.SELECT
#     Products.ProductName,Shippers.ShipperName
# FROM
#     Products
# JOIN
#     OrderDetails ON Products.ProductId = OrderDetails.ProductId
# JOIN
#     Orders ON OrderDetails.OrderId = Orders.OrderId
# JOIN
#     Shippers ON Orders.ShipperId = Shippers.ShipperId;
# 3.SELECT
#     Shippers.ShipperName,
#     COUNT(*) AS ShippedProductCount
# FROM
#     Shippers
# JOIN
#     Orders ON Shippers.ShipperId = Orders.ShipperId
# JOIN
#     OrderDetails ON Orders.OrderId = OrderDetails.OrderId
# GROUP BY
#     Shippers.ShipperName;
# 4.SELECT COUNT(*) AS CountNoSonCustomers
# FROM Customers
# WHERE CustomerName NOT LIKE '%son%';

# 5. SELECT SUM(Price * Quantity) AS Total_Sales 
# FROM Orders AS o 
# INNER JOIN OrderDetails AS ord ON ord.OrderID=o.OrderID
# INNER JOIN Products AS p ON p.ProductID=ord.ProductID
# WHERE OrderDate LIKE '%1997%';
# 6.SELECT
#     C.CustomerName,
#     SUM(OD.Quantity * P.Price) AS TotalAmount
# FROM
#     Customers C
# LEFT JOIN
#     Orders O ON C.CustomerId = O.CustomerId
# LEFT JOIN
#     OrderDetails OD ON O.OrderId = OD.OrderId
# LEFT JOIN
#     Products P ON OD.ProductId = P.ProductId
# GROUP BY
#     C.CustomerName
# ORDER BY
#     TotalAmount DESC;
# 7.SELECT
#     S.SupplierName,
#     COUNT(*) AS TotalProductsOrdered
# FROM
#     Suppliers S
# JOIN
#     Products P ON S.SupplierId = P.SupplierId
# JOIN
#     OrderDetails OD ON P.ProductId = OD.ProductId
# GROUP BY
#     S.SupplierName
# ORDER BY
#     TotalProductsOrdered DESC
# LIMIT 1;
# 8.SELECT
#     P.ProductName,
#     SUM(OD.Quantity * p.Price) AS TotalSales
# FROM
#     Products P
# JOIN
#     OrderDetails OD ON P.ProductId = OD.ProductId
# GROUP BY
#     P.ProductName;

# 9.SELECT SUBSTR(OrderDate, 0, 8) AS Month,SUM(od.Quantity * p.Price) AS TotalSales
# FROM Orders o
# JOIN OrderDetails od ON o.OrderId = od.OrderId
# JOIN Products p ON od.ProductId = p.ProductId
# GROUP BY Month
# ORDER BY TotalSales DESC
# LIMIT 1;
# 10.SELECT
#     OrderDate,
#     SUM(OD.Quantity * P.Price) AS TotalSales
# FROM
#     Orders O
# JOIN
#     OrderDetails OD ON O.OrderId = OD.OrderId
# JOIN
#     Products P ON OD.ProductId = P.ProductId
# GROUP BY
#     OrderDate;
# 11.SELECT
#     C.CustomerName,
#     IFNULL(SUM(OD.Quantity * P.Price), 0) AS TotalSales
# FROM
#     Customers C
# LEFT JOIN
#     Orders O ON C.CustomerId = O.CustomerId
# LEFT JOIN
#     OrderDetails OD ON O.OrderId = OD.OrderId
# LEFT JOIN
#     Products P ON OD.ProductId = P.ProductId
# GROUP BY
#     C.CustomerName;
# 12.CREATE TABLE payments (
#     PaymentID INT PRIMARY KEY,
#     OrderID INT,
#     PaymentDate DATE,
#     Amount DECIMAL(10,2),
#     FOREIGN KEY (OrderID) REFERENCES Orders(OrderID)
# );
