from math import *

"""Encoding a message with Cesar process"""

def encrypt(chain):
    key = int(input("Donne une clé de codage: "))
    message = input("Donne le message que tu veux crypter: ")
    