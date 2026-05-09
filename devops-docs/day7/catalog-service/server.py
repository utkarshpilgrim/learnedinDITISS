from flask import Flask
import mysql.connector

db_conf = {
    "host": "db",
    "user": "root",
    "password": "root",
    "database": "mydb"
}

app = Flask(__name__)

@app.route("/products", methods=["GET"])
def products():
    try:
        with mysql.connector.connect(**db_conf) as connection:
            with connection.cursor() as cursor:
                sql = "SELECT id, title, price FROM Product"
                print("SQL:", sql)
                cursor.execute(sql)
                products = cursor.fetchall()
                print(products)

                items = []
                for product in products:
                    items.append({
                        "id": product[0],
                        "title": product[1],
                        "price": product[2]
                    })

                print(items)
                return items
    except Exception as ex:
        print(ex)
        return ex


@app.route("/", methods=["GET"])
def root():
    return "<h1>Welcome to catalog service v1.4</h1>"

app.run(host="0.0.0.0", port=4000, debug=True)