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


@app.route("/api/v1/teachers", methods=['GET'])
def get_teachers():
    return jsonify({'teachers': TeacherModel.get_all_instances()})


@app.route("/api/v1/teachers/new", methods=['POST'])
def new_teacher():

    json = request.get_json(force=True)

    if not validate(json, 'firstName', 'lastName', 'department'):
        abort(400)

    first_name = json['firstName']
    last_name = json['lastName']
    department = json['department']

    teacher = LabModel(first_name=first_name,
                       last_name=last_name,
                       department=department)

    teacher.push()
    return ""


@app.route("/api/v1/reservedCarts", methods=['GET'])
def get_reserved_carts():
    return jsonify({'reservedCarts': ReservedCartModel.get_all_instances()})


@app.route("/api/v1/reservedCarts/new", methods=['POST'])
def new_reserved_cart():

    json = request.get_json(force=True)

    if not validate(json,
                    'fullName',
                    'department',
                    'cartNumber',
                    'deviceType',
                    'deviceQuantity',
                    'date',
                    'block'):
        abort(400)

    full_name = json['fullName']
    department = json['department']
    cart_number = json['cartNumber']
    device_type = json['deviceType']
    device_quantity = json['deviceQuantity']
    date = json['date']
    block = json['block']

    reserved_cart = ReservedCartModel(full_name=full_name,
                                      department=department,
                                      cart_number=cart_number,
                                      device_type=device_type,
                                      device_quantity=device_quantity,
                                      date=date,
                                      block=block)

    reserved_cart.push()

    return ""


@app.route("/api/v1/reservedLabs", methods=['GET'])
def get_reserved_labs():
    return jsonify({'reservedLabs': ReservedLabModel.get_all_instances()})


@app.route("/api/v1/reservedLabs/new", methods=['POST'])
def new_reserved_lab():

    json = request.get_json(force=True)

    if not validate(json,
                    'fullName',
                    'department',
                    'labNumber',
                    'deviceQuantity',
                    'date',
                    'block'):
        abort(400)

    full_name = json['fullName']
    department = json['department']
    lab_number = json['labNumber']
    device_quantity = json['deviceQuantity']
    date = json['date']
    block = json['block']

    reserved_lab = ReservedLabModel(full_name=full_name,
                                      department=department,
                                      lab_number=lab_number,
                                      device_quantity=device_quantity,
                                      date=date,
                                      block=block)

    reserved_lab.push()

    return ""

if __name__ == '__main__':
    Database.initialize()
    app.run(debug=True)
