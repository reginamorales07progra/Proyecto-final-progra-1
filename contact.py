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

    def crearContacto():

    print("Ingrese el contacto\n")
    contact = {
        "nombre": input("nombre: ").lower(),
        "telefono": input("telefono: "),
        "correo": input("correo: "),
        "empresa": input("empresa: "),
        "extra": input("extra: ")

    }
    fail = validate(contact)
    clear()
    print("\nverificando...")

    while len(fail.keys()):
        for key in fail.keys():
            data = input(f'ingresaste mal el {key}, intentalo de nuevo: ')
            contact[key] = data
        fail = validate(contact)

    char = contact["nombre"][:1].upper()
    contacts[char][contact["nombre"]] = contact

    clear()
    print("agregado exitosamente\n")


def showPerson(person):
    for name, data in person.items():
        print(f'{name}: ')
        for key, value in data.items():
            print(f'\t{key}: {value}')


def listarContactos():
    letters = contacts.keys()
    cts = []
    count = 1
    for letter in letters:
        persons = contacts[letter]
        print(letter)
        for name, data in persons.items():
            print(f'   {count}. {name}')
            count += 1
            cts.append({name: data})

    select = input("Ver contacto: ").lower()
    if len(select):
        person = cts[int(select) - 1]
        showPerson(person)