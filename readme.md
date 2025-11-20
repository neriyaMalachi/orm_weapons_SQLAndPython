#  MySQL Connector – Basic SELECT Example

This project demonstrates how to connect to a MySQL database using  
`mysql.connector`, execute a SQL query, fetch results, and close the connection properly.

---

## Project Overview
This example shows:

- How to establish a connection to a MySQL database  
- How to create and use a cursor  
- How to execute SQL manually  
- Why `fetchall()` is required before closing the cursor  
- How to safely close the connection

---

## Requirements

Install the MySQL connector:

```bash
pip install mysql-connector-python