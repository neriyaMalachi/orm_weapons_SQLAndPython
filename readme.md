## ORM Example – SQLModel + MySQL

#### This project demonstrates how to use ORM (Object Relational Mapping) in Python using SQLModel, which is built on top of SQLAlchemy.
##### The goal is to replace raw SQL queries with Python classes and objects.

🔹 What This Example Shows
1. Database Connection (Engine)

The project uses SQLModel's create_engine to connect Python to a MySQL database.
The engine manages all communication between the code and the SQL server.
With echo=True, you can see the actual SQL commands being executed behind the scenes.

2. Automatic Table Creation

Using SQLModel.metadata.create_all(engine), the ORM reads all your models (classes)
and generates the corresponding SQL tables automatically — without writing SQL manually.

3. ORM Model (Class → Table)

The Weapon class represents the database table.
Each attribute in the class becomes a column in the table.
The id field is automatically created as a primary key and auto-incremented by the database.

4. Creating and Saving Records

A Session object opens a temporary connection to the database.
Inside a session you can:

Create new objects (new rows)

Add them to the session

Commit the changes to the database

When committing, SQLModel converts your object into a real SQL INSERT statement.

5. Querying Data (SELECT)

Using the select() function, the ORM builds SQL queries for you.
The results are returned as Python objects rather than raw SQL data.
This makes the code cleaner, safer, and easier to maintain.

🔹 Why ORM?

No need to write SQL manually

Tables and rows become Python classes and objects

Auto-generated schemas

Cleaner, safer, more modern code

Easier maintenance and debugging

🔹 Summary

This project demonstrates:

Connecting Python to MySQL using ORM

Auto-creating tables from Python classes

Adding new rows using objects

Fetching data using ORM queries

Understanding how ORM replaces raw SQL entirely

An excellent beginner-friendly example of using SQLModel for real database operations.