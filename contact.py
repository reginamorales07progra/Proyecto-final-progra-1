import validators
import os
import time
import csv


class contactBook(dict):
    def __missing__(self, key):
        value = self[key] = type(self)()
        return value


contacts = contactBook()
exit = False


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def wait():
    wait = input("presione [ENTER] para avanzar")


def validate(contact):
    fail = {}
    if len(contact["nombre"].split(" ")) < 2:
        fail["nombre"] = contact["nombre"]

    if not contact["telefono"].isdigit() or len(contact["telefono"]) != 8:
        fail["telefono"] = contact["telefono"]

    if not validators.email(contact["correo"]):
        fail["telefono"] = contact["telefono"]

    return fail