import json
from faker import Faker
import random

def create_new_courier():
    fake = Faker()
    login = fake.name()
    password = fake.password()
    firstName = fake.first_name()
    payload = {
        "login": login,
        "password": password,
        "name": firstName
    }

    return payload


def  create_data_for_order(color):
    fake = Faker(locale="ru_RU")
    payload = {
        "firstName": fake.first_name(),
        "lastName": fake.last_name(),
        "address": fake.address(),
        "metroStation": fake.text(10),
        "phone": fake.phone_number(),
        "rentTime": random.randrange(1,8),
        "deliveryDate": fake.date(),
        "color": color,
        "comment": fake.text(10)
    }

    return json.dumps(payload)

