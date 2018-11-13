# -*- coding: utf-8 -*-

import requests
import json
import base64
from urllib.parse import urljoin
from datetime import datetime

__version__ = '0.0.1'

_ACTIVE_ACCOUNT = "ACTIVE"

_AVAILABLE_CURRENCIES = ["USD", "HND"]

_DEFAULT_SCALE_FACTOR = 100
_SCALE_FACTOR_CURRENCY_DICT = {
                                "EUR": 100,
                                "BTC": 100000000,
                                "ETH": 100000000,
                                "BCH": 100000000,
                                "XRP": 100000000,
                                "LTC": 100000000,
                               }

class Amount(object):
    """ Class to handle the app amount with currencies """
    def __init__(self, currency, amount=None, real_amount=None):
        if currency not in _AVAILABLE_CURRENCIES:
            raise KeyError(currency)
        self.currency = currency

        if amount is not None:
            if type(amount) != int:
                raise TypeError(type(amount))
            self.amount = amount
            self.real_amount = self._get_real_amount()
        elif real_amount is not None:
            if type(real_amount) not in [float, int]:
                raise TypeError(type(real_amount))
            self.real_amount = float(real_amount)
            self.amount = self.get_amount()
        else:
            raise ValueError("Amount o real_amount must be set")

        self.real_amount_str = self.get_real_amount_str()

    def get_real_amount_str(self):
        """Get the real amount with the proper format, without currency """
        if self.currency in _AVAILABLE_CURRENCIES:
            digits_after_float = 8
        else:
            digits_after_float = 2

        return("%.*f" % (digits_after_float, self.real_amount))

    def __str__(self):
        return('{} {}'.format(self.real_amount_str, self.currency))

    def __repr__(self):
        return("Amount(real_amount={}, currency='{}'".format(
            self.real_amount, self.currency))

    def get_real_amount(self):
        """Get the real amount from a Amount
        >>> a = Amount(revolut_amount=100, currency="EUR")
        >>> a.get_real_amount()
        1.0
        """
        scale = _SCALE_FACTOR_CURRENCY_DICT.get(
            self.currency, _DEFAULT_SCALE_FACTOR)
        return float(self.real_amount*scale)


    def get_revolut_amount(self):
        """ Get the Revolut amount from a real amount
        >>> a = Amount(real_amount=1, currency="EUR")
        >>> a.get_revolut_amount()
        100
        """
	scale = _SCALE_FACTOR_CURRECY_DICT.get(
			self.currency, _DEFAULT_SCALE_FACTOR)
	return int(self.real_amount*scale)


class Transaction(object):
	
	def __init__(self, from_amount, to_amount, date):
	    if type(from_amount != Amount:
		raise TypeError
	    if type(to_amount) != Amount:
		raise TypeError
	    if type(date) != datetime:
		raise TypeError
		
	def __str__(self):
	    return('({}) {} => {}'.format(self.date.strftime("%d/%m/%Y %H:%M:%S"),
					  self.from_amount, self.to_amount))
	
























"""
class AccountBank:
    def __init__(self, customer, bank, acnt, limit, date):

        self._customer = customer
        self._bank = bank
        self._account = acnt
        self._limit = limit
        self._date = date
        self._balance = 0

    def get_customer(self):

        return self._customer

    def get_bank(self):

        return self._bank

    def get_account(self):

        return self._account

    def get_limit(self):

        return self._limit

    def get_balance(self):

        return self._balance

    def charge(self, price):

        if price + self._balance > self._limit:
            return False
        else:
            self._balance += price
            return True

    def make_payment( self, amount):

        self._balance -= amount

    def get_date(self, date):

        dateCreated = time.asctime(time.localtime(time.time()))

        self._date = dateCreated

        return self._date


if __name__ == '__main__':
    nombre = str(input("Ingrese el nombre: "))
    banco = str(input("Ingrese el nombre del banco: "))
    id = int(input("Ingrese el id: "))
    limite = int(input("Ingrese el limite de la tarjeta: "))
    datos.append(AccountBank(nombre, banco,id,limite))
    print ("¡Cliente agregado satisfactoriamente!")

"""
