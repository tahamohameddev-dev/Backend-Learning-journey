# Database Journey

## What is a Database (DB)?

|Any collection of related|Database can be stored in different ways|
|---|---|
|Phone Book|On paper|
|Shopping list|in your mind|
|Todo list|On a computer|
|Your 5 best frinds|Tis powerpoint|
|Facebooks User Base|Computer Sectoin|


# Database Management Systems (DBMS)

## A special software program that helps users create and maintain a database

- Makes it easy to manage large amount of informatoin
- Handles security
- Backups
- Importing/exporting data 
- Concurrency
- Interacts with software  applications 

## What is CRUD?
- CRUD is a simple way to describe the four basic actions we do with data:
- Create: Save new data (e.g., adding a new expense).
- Read: View existing data (e.g., checking your list of expenses).
- Update: Change data (e.g., editing an expense amount).
- Delete: Remove data (e.g., deleting an old entry).

## Relational Databases (SQL)

A highly organized way to store data using tables:

- **Structure**: Data is saved in rows and columns, just like an Excel sheet.
- **Relationships**: Tables are connected to each other using keys.
- **Consistency**: Strict rules ensure that your data is accurate and reliable (essential for financial apps).
- **The Language**: We use SQL (Structured Query Language) to interact with these databases.
- **Examples**: MySQL, PostgreSQL, SQLite.

## Non-Relational Databases (NoSQL)

A flexible way to store data as documents:

- **Structure**: Data is stored in flexible formats (like JSON) rather than fixed tables.
- **Flexibility**: You can add new types of data easily without changing the structure.
- **Use Case**: Best for fast, large-scale, or rapidly changing data.
- **Examples**: MongoDB, Redis.

# Structured Query Language (SQL)

## **SQL** is language used for interacting with Relational Database Management Systems (RDBMS)

** You can use SQL to get the RDBMS to do things for you **
- Create, retieve, update & delete data
- Create, manage databases
- Desingn & create database tables
- peform administration tasks (security, user management, import/export, etc)

## SQL Learning Journey: Practical Basics

Now that we have covered the theory, let's start applying our knowledge. Here, we will document the practical SQL commands starting from database creation.

### Creating a Database
This is the first step to initialize our database environment.
```sql
CREATE DATABASE girrafe;

###  Common Data Types
When creating tables, we define the data type for each column:

*   **INT**: Used for whole numbers (e.g., 10, 500).
*   **DECIMAL(M, N)**: Used for precise decimal numbers like money. (M = total digits, N = digits after decimal).
*   **VARCHAR(length)**: Used for text strings with a maximum character limit.
*   **BLOB**: Used for large binary data like images or files.
*   **DATE**: Used for dates in 'YYYY-MM-DD' format.
*   **TIMESTAMP**: Used for recording specific date and time 'YYYY-MM-DD HH:MM:SS'.

