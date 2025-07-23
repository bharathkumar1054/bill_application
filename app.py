from flask import Flask, render_template, request
import mysql.connector
from config import db_config

app = Flask(__name__)

def get_db_connection():
    return mysql.connector.connect(**db_config)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    customer = request.form['customer']
    item = request.form['item']
    price = float(request.form['price'])
    quantity = int(request.form['quantity'])
    total = price * quantity

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO bills (customer, item, price, quantity, total) VALUES (%s, %s, %s, %s, %s)',
                   (customer, item, price, quantity, total))
    conn.commit()
    cursor.close()
    conn.close()

    return render_template('bil.html', customer=customer, item=item, price=price, quantity=quantity, total=total)

@app.route('/view')
def view():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM bills ORDER BY id DESC')
    bills = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('view_bills.html', bills=bills)

if __name__ == '__main__':
    app.run(debug=True)