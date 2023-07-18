from flask import Blueprint, render_template
from models.orders import orders

orders_blueprint = Blueprint("orders", __name__)

@orders_blueprint.route("/orders")
def index():
	return render_template("index.html", title="Order List", order_list = orders)

@orders_blueprint.route("/orders/<id>")
def order(id):
	id = int(id)
	return render_template("order.html",title="Order", order=orders[id])