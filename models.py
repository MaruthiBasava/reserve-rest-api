#!/usr/bin/python
# -*- coding: utf-8 -*-

from database import Database


class CartModel(object):

    __collection_id = 'carts'

    def __init__(
        self,
        cart_number,
        device_type,
        device_quantity,
        ):

        self.cart_number = cart_number
        self.device_type = device_type
        self.device_quantity = device_quantity

    def push(self):
        Database.insert(collection=self.__collection_id,
                        data=self.jsonify())

    def jsonify(self):
        return {'cartNumber': self.cart_number,
                'type': self.device_type,
                'deviceQuantity': self.device_quantity}


class LabModel(object):

    __collection_id = 'labs'

    def __init__(self, lab_number, device_quantity):
        self.lab_number = lab_number
        self.device_quantity = device_quantity

    def push(self):
        Database.insert(collection=self.__collection_id,
                        data=self.jsonify())

    def jsonify(self):
        return {'labNumber': self.lab_number,
                'deviceQuantity': self.device_quantity}


class TeacherModel(object):

    __collection_id = 'teachers'

    def __init__(
        self,
        first_name,
        last_name,
        department,
        ):

        self.first_name = first_name
        self.last_name = last_name
        self.department = department

    def push(self):
        Database.insert(collection=self.__collection_id,
                        data=self.jsonify())

    def jsonify(self):
        return {'firstName': self.cart_number,
                'lastName': self.device_type,
                'department': self.department}


class ReservedCartModel(object):

    __collection_id = 'reservedCarts'

    def __init__(
        self,
        full_name,
        department,
        cart_number,
        device_type,
        device_quantity,
        date,
        block,
        ):

        self.full_name = full_name
        self.department = department
        self.cart_number = cart_number
        self.device_type = device_type
        self.device_quantity = device_quantity
        self.date = date
        self.block = block

    def push(self):
        Database.insert(collection=self.__collection_id,
                        data=self.jsonify())

    def jsonify(self):
        return {
            'fullName': self.full_name,
            'department': self.department,
            'cartNumber': self.cart_number,
            'deviceType': self.device_type,
            'deviceQuantity': self.device_quantity,
            'date': self.date,
            'block': self.block,
            }


class ReservedLabModel(object):

    __collection_id = 'reservedLabs'

    def __init__(
        self,
        full_name,
        department,
        lab_number,
        device_quantity,
        date,
        block,
        ):

        self.full_name = full_name
        self.department = department
        self.lab_number = lab_number
        self.device_quantity = device_quantity
        self.date = date
        self.block = block

    def push(self):
        Database.insert(collection=self.__collection_id,
                        data=self.jsonify())

    def jsonify(self):
        return {
            'fullName': self.full_name,
            'department': self.department,
            'labNumber': self.lab_number,
            'deviceQuantity': self.device_quantity,
            'date': self.date,
            'block': self.block,
            }
