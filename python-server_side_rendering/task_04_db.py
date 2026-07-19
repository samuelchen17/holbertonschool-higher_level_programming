from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)


# functions
def read_json():
    """
    Read from json file
    """
    with open("products.json", "r") as file:
        return json.load(file)


def read_csv():
    """
    Read from csv file
    """
    products = []

    with open("products.csv", "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            products.append(
                {
                    "id": int(row["id"]),
                    "name": row["name"],
                    "category": row["category"],
                    "price": float(row["price"]),
                }
            )

    return products


def get_sql_data():
    conn = sqlite3.connect("products.db")
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Products")
    rows = cursor.fetchall()

    conn.close()

    return [dict(row) for row in rows]


# routes
@app.route("/")
def home():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/items")
def items():
    with open("items.json", "r") as file:
        data = json.load(file)

    return render_template("items.html", items=data["items"])


@app.route("/products")
def products():

    source = request.args.get("source")
    product_id = request.args.get("id")

    # Check source
    if source == "json":
        products = read_json()

    elif source == "csv":
        products = read_csv()

    elif source == "sql":
        products = get_sql_data()

    else:
        return render_template("product_display.html", error="Wrong source")

    if product_id:

        product_id = int(product_id)

        products = [
            product for product in products if product["id"] == product_id
        ]

        if not products:
            return render_template(
                "product_display.html", error="Product not found"
            )

    return render_template("product_display.html", products=products)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
