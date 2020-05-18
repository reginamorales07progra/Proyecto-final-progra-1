import validators
import os
import time
import csv
import requests as req
import json


class contactBook(dict):
    def _missing_(self, key):
        value = self[key] = type(self)()
        return value


contacts = contactBook()
r = req.get('http://demo7130536.mockable.io/final-contacts-100')
data =json.loads(r.text)
for key, lcontact in data.items():
  contacts[key] = lcontact
  

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


def buscarContacto():
    name = input("buscar: ")
    values = contacts.values()
    names = []
    for letter in values:
        cts = letter.keys()
        for person in cts:
            names.append(person)

    def match(fullname):
        return name.lower() in fullname.lower()

    persons = filter(match, names)
    if len(persons):
        print("Resultados: ")
        for person in persons:
            print(f' - {person}')

    else:
        print("Ningun contacto encontrado")

    print("\n")


def eliminarContacto():
    letters = contacts.keys()
    cts = []
    count = 1
    for letter in letters:
        persons = contacts[letter]
        print(letter)
        for name, data in persons.items():
            print(f'   {count}. {name}')
            count += 1
            cts.append(name)

    select = input("Eliminar contact contacto: ").lower()
    if select.isdigit():
        key = int(select) - 1
        del cts[key]
        try:
            for letter, persons in contacts.items():
                for person in persons.keys():
                    if not person in cts:
                        del contacts[letter][person]
        except:
            pass

    else:
        key = select[:1].upper()
        if contacts[key][select]:
            del contacts[key][select]
            print("contacto eliminado")
        else:
            print("contacto no encontrado")


def callContact():
    letters = contacts.keys()
    cts = []
    count = 1
    for letter in letters:
        persons = contacts[letter]
        print(letter)
        for name, data in persons.items():
            print(f'   {count}. {name}')
            count += 1
            cts.append(data)

    select = input("contacto? ").lower()
    if select.isdigit():
        person = cts[int(select) - 1]
        time.sleep(3)
        print(f'Lamando a "{person["nombre"]}" al {person["telefono"]}')

    else:
        key = select[:1].upper()
        if contacts[key][select]:
            person = contacts[key][select]
            time.sleep(3)
            print(f'Lamando a "{person["nombre"]}" al {person["telefono"]}')
        else:
            print("contacto no encontrado\n")


def SendMessage():
    letters = contacts.keys()
    cts = []
    count = 1
    for letter in letters:
        persons = contacts[letter]
        print(letter)
        for name, data in persons.items():
            print(f'   {count}. {name}')
            count += 1
            cts.append(data)

    select = input("contacto? ").lower()
    message = input("\nMensaje: ")
    if select.isdigit():
        person = cts[int(select) - 1]
        print(
            f'Hola "{person["nombre"]}" {person["telefono"]}\n\t > {message}')


def SendMail():
    letters = contacts.keys()
    cts = []
    count = 1
    for letter in letters:
        persons = contacts[letter]
        print(letter)
        for name, data in persons.items():
            print(f'   {count}. {name}')
            count += 1
            cts.append(data)

    select = input("contacto? ").lower()
    subject = input("\nSubject: ")
    message = input("Mensaje: ")
    if select.isdigit():
        person = cts[int(select) - 1]
        print(
            f'Enviando correo a "{person["nombre"]}" {person["correo"]}\n\t > Subject: {subject} \n\t > Message: {message}')

    else:
        key = select[:1].upper()
        if contacts[key][select]:
            person = contacts[key][select]
            print(
                f'Enviando correo a "{person["nombre"]}" {person["correo"]}\n\t > Subject: {subject} \n\t > Message: {message}')
        else:
            print("contacto no encontrado\n")


def exportContacts():
    with open('contacts.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["nombre", "telefono", "correo", "empresa", "extra"])
        for letter, persons in contacts.items():
            for person in persons:
                writer.writerow(list(persons[person].values()))
  
        print("contactos exportados exitosamente")

while not exit:
    clear()
    # Agregar contactos
    # Buscar contactos
    # Listar contactos
    # Borrar contactos
    # Llamar contactos
    # Enviar mensaje a contactos
    # Enviar correo a contacto.
    # Exportar Contactos.
    options = {
        "1": {
            "text": "Crear Contacto",
            "pointer": crearContacto
        },
        "2": {
            "text": "Buscar Contacto",
            "pointer": buscarContacto
        },
        "3": {
            "text": "listar Contactos",
            "pointer": listarContactos
        },
        "4": {
            "text": "Eliminar Contacto",
            "pointer": eliminarContacto
        },
        "5": {
            "text": "Lammar a contacto",
            "pointer": callContact
        },
        "6": {
            "text": "Enviar mensaje a contacto",
            "pointer": SendMessage
        },
        "7": {
            "text": "Enviar correo a contacto",
            "pointer": SendMail
        },
        "8": {
            "text": "Exportar Contactos",
            "pointer": exportContacts
        },


    }
    for n, option in options.items():
        print(f'{n}) {option["text"]}')

    select = input("Ingrese numero de opcion: ")
    option = options.get(select)
    clear()
    option["pointer"]()
    wait()