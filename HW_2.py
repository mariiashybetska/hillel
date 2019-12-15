from flask import Flask, request
import string
import random
import os
import sqlite3

app = Flask('app')


@app.route('/')
def title():
    return 'Home work lesson 4'


def get_number_of_symbols():
    n = request.args['symbols']
    if any([n[i].isalpha() for i in range(len(n))]):
        return 'Please, enter only numbers!'
    elif int(n) < 0:
        return 'Please, enter positive number!'
    elif int(n) > 1000:
        return 'Please, enter number from 0 to 1000!'
    else:
        return ' '.join(
            random.choice(string.ascii_uppercase) for i in range(int(n))
        )


@app.route('/get-symbols')
def get_symbols():
    return get_number_of_symbols()


def exec_query(query):
    db_pass = os.path.join(os.getcwd(), 'chinook.db')
    conn = sqlite3.connect(db_pass)
    cur = conn.cursor()
    cur.execute(query)
    record = cur.fetchall()
    return record


@app.route('/filter-customers')
def get_customers():
    query = f'SELECT * FROM customers WHERE City = \'{request.args["city"]}\' and State = \'{request.args["state"]}\';'
    result = exec_query(query)
    return str(result)


@app.route('/unique-names')
def get_unique_names():
    query = 'SELECT COUNT(distinct FirstName) FROM customers;'
    result = str(exec_query(query))[2::]
    c = result.find(',')
    result = result[:c]
    return f'There are {result} unique first names in table Customers'


@app.route('/profit')
def get_profit():
    query = 'SELECT SUM(UnitPrice * Quantity) FROM invoice_items;'
    result = str(exec_query(query))[2::]
    c = result.find(',')
    result = result[:c]
    return f'Total profit is {result}'


if __name__ == '__main__':
    app.run(port=5000, debug=True)

