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

    @classmethod
    def pull(cls, cart_number):
        data = Database.find_one(collection=cls.__collection_id,
                                 query={'cartNumber': cart_number})

        return cls(cart_number=data['cartNumber'],
                   device_type=data['type'],
                   device_quantity=data['deviceQuantity'])

    def jsonify(self):
        return {'cartNumber': self.cart_number,
                'type': self.device_type,
                'deviceQuantity': self.device_quantity}

    @staticmethod
    def get_all_instances():
        return Database.get_all_instances(CartModel.__collection_id)

    @staticmethod
    def delete_one(cart_number):
        Database.delete_one(CartModel.__collection_id,
                            query={'cartNumber': cart_number})


class LabModel(object):

    __collection_id = 'labs'

    def __init__(self, lab_number, device_quantity):
        self.lab_number = lab_number
        self.device_quantity = device_quantity

    def push(self):
        Database.insert(collection=self.__collection_id,
                        data=self.jsonify())

    @classmethod
    def pull(cls, lab_number):
        data = Database.find_one(collection=cls.__collection_id,
                                 query={'labNumber': lab_number})

        return cls(lab_number=data['labNumber'],
                   device_quantity=data['deviceQuantity'])

    def jsonify(self):
        return {'labNumber': self.lab_number,
                'deviceQuantity': self.device_quantity}

    @staticmethod
    def get_all_instances():
        return Database.get_all_instances(LabModel.__collection_id)

    @staticmethod
    def delete_one(lab_number):
        Database.delete_one(LabModel.__collection_id,
                            query={'labNumber': lab_number})


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

    @classmethod
    def pull(cls, last_name, department):
        data = Database.find_one(collection=cls.__collection_id,
                                 query={'lastName': last_name,
                                        'department': department})

        return cls(first_name=data['firstName'],
                   last_name=data['lastName'],
                   department=data['department'])

    def jsonify(self):
        return {'firstName': self.cart_number,
                'lastName': self.device_type,
                'department': self.department}

    @staticmethod
    def get_all_instances():
        return Database.get_all_instances(TeacherModel.__collection_id)

    @staticmethod
    def delete_one(first_name, last_name, department):
        Database.delete_one(TeacherModel.__collection_id,
                            query={'firstName': first_name,
                                   'lastName': last_name,
                                   'department': department})


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

    @classmethod
    def pull(
        cls,
        cart_number,
        date,
        block,
        ):

        data = Database.find_one(collection=cls.__collection_id,
                                 query={'cartNumber': cart_number,
                                        'date': date,
                                        'block': block})
        return cls(
            full_name=data['fullName'],
            department=data['department'],
            cart_number=data['cartNumber'],
            device_type=data['deviceType'],
            device_quantity=data['deviceQuantity'],
            date=data['date'],
            block=data['block'],
            )

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

    @staticmethod
    def get_all_instances():
        return Database.get_all_instances(ReservedCartModel.__collection_id)

    @staticmethod
    def delete_one(cart_number, date, block):
        Database.delete_one(ReservedCartModel.__collection_id,
                            query={'cartNumber': cart_number,
                                   'date': date,
                                   'block': block})


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

    @classmethod
    def pull(
        cls,
        department,
        date,
        block,
        ):
        data = Database.find_one(collection=cls.__collection_id,
                                 query={'department': department,
                                        'date': date,
                                        'block': block})
        return cls(
            full_name=data['fullName'],
            department=data['department'],
            lab_number=data['labNumber'],
            device_quantity=data['deviceQuantity'],
            date=data['date'],
            block=data['block'],
            )

    def jsonify(self):
        return {
            'fullName': self.full_name,
            'department': self.department,
            'labNumber': self.lab_number,
            'deviceQuantity': self.device_quantity,
            'date': self.date,
            'block': self.block,
            }

    @staticmethod
    def get_all_instances():
        return Database.get_all_instances(ReservedLabModel.__collection_id)

    @staticmethod
    def delete_one(lab_number, date, block):
        Database.delete_one(ReservedLabModel.__collection_id,
                            query={'labNumber': lab_number,
                                   'date': date,
                                   'block': block})
