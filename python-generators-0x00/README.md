# Python Generators

This project demonstrates the use of Python generators to stream data from a MySQL database. It includes functionality to:

- Connect to a MySQL database
- Create a database and table if they do not exist
- Insert sample data from a CSV file into the table
- Stream data from the `user_data` table using a generator

## Setup

1. Ensure you have MySQL running.
2. Set up the database and table by running the `0-main.py` script.
3. The `user_data.csv` file contains sample data that will be inserted into the `user_data` table.

## Running the Script

Run the `0-main.py` script to:
1. Set up the database and table.
2. Insert data into the table.
3. Stream and print the rows from the `user_data` table.

```bash
$ python3 0-main.py
