from flask import Flask, jsonify, request, abort
from models import *
from utilities import validate

app = Flask(__name__)

@app.route("/")
def home():
    return "This is root directory"

@app.route("/api/v1/carts", methods=['GET'])
def get_carts():
    return jsonify({'carts': CartModel.get_all_instances()})

@app.route("/api/v1/carts/new", methods=['POST'])
def new_cart():

    json = request.get_json(force=True)

    if not validate(json, 'cartNumber', 'type', 'deviceQuantity'):
        abort(400)

    cart_number = json['cartNumber']
    device_type = json['type']
    device_quantity = json['deviceQuantity']
    cart = CartModel(cart_number=cart_number,
                     device_type=device_type,
                     device_quantity=device_quantity)
    cart.push()
    return ""

@app.route("/api/v1/labs", methods=['GET'])
def get_labs():
    return jsonify({'labs': LabModel.get_all_instances()})

@app.route("/api/v1/labs/new", methods=['POST'])
def new_lab():

    json = request.get_json(force=True)

    if not validate(json, 'labNumber', 'deviceQuantity'):
        abort(400)

    lab_number = json['labNumber']
    device_quantity = json['deviceQuantity']

    lab = LabModel(lab_number=lab_number,
                   device_quantity=device_quantity)

    lab.push()
    return ""

if __name__ == '__main__':
    Database.initialize()
    app.run(debug=True)
