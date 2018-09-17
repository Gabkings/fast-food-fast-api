from flask import Flask, request
from flask_restful import Resource
from .models import Order, orders

class DisplayAllOrders(Resource):
    '''Class to display all the orders available'''
    def get(self):
        '''method for displaying all the orders'''
        return {"orders":[order.collect_order_details() for order in orders]}