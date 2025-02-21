from flask import Flask, render_template
import pymysql
import os

app = Flask(__name__)

# Connect to AWS RDS MySQL Database
db = pymysql.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME"),
)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/products')
def products():
    cursor = db.cursor()
    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()
    return render_template("product.html", products=products)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
