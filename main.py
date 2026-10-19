
# STEP 1A
# Import SQL Library and Pandas
import sqlite3
import pandas as pd

# STEP 1B
# Connect to the database
conn = sqlite3.connect("data.sqlite")


# STEP 2
# Select employee number and last name
df_first_five = pd.read_sql("""
    SELECT employeeNumber, lastName
    FROM employees
""", conn)


# STEP 3
# Select last name before employee number
df_five_reverse = pd.read_sql("""
    SELECT lastName, employeeNumber
    FROM employees
""", conn)


# STEP 4
# Alias employeeNumber as ID
df_alias = pd.read_sql("""
    SELECT lastName, employeeNumber AS ID
    FROM employees
""", conn)


# STEP 5
# Categorize employees by job title
df_executive = pd.read_sql("""
    SELECT *,
        CASE
            WHEN jobTitle = 'President'
              OR jobTitle = 'VP Sales'
              OR jobTitle = 'VP Marketing'
            THEN 'Executive'
            ELSE 'Not Executive'
        END AS role
    FROM employees
""", conn)


# STEP 6
# Find the length of each last name
df_name_length = pd.read_sql("""
    SELECT LENGTH(lastName) AS name_length
    FROM employees
""", conn)


# STEP 7
# Get the first two letters of each job title
df_short_title = pd.read_sql("""
    SELECT SUBSTR(jobTitle, 1, 2) AS short_title
    FROM employees
""", conn)


# STEP 8
# Calculate the sum of rounded order prices
sum_total_price = pd.read_sql("""
    SELECT SUM(ROUND(priceEach * quantityOrdered))
    FROM orderDetails
""", conn).to_numpy()[0]


# STEP 9
# Return order date and separate day, month, and year columns
df_day_month_year = pd.read_sql("""
    SELECT
        orderDate,
        SUBSTR(orderDate, 9, 2) AS day,
        SUBSTR(orderDate, 6, 2) AS month,
        SUBSTR(orderDate, 1, 4) AS year
    FROM orders
""", conn)


# Close the connection after all queries are complete
conn.close()
