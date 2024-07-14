import json
import random
from faker import Faker


class Helpers:
    @staticmethod
    def create_courier_data():
        fake = Faker()
        login = fake.name()
        password = fake.password()
        first_name = fake.first_name()
        payload = {
            "login": login,
            "password": password,
            "first_name": first_name
        }
        return payload

    @staticmethod
    def create_data_for_order(color):
        fake = Faker(locale="ru_RU")
        payload = {
            "firstName": fake.first_name(),
            "lastName": fake.last_name(),
            "address": fake.address(),
            "metroStation": random.randrange(10),
            "phone": fake.phone_number(),
            "rentTime": random.randrange(6),
            "deliveryDate": fake.date(),
            "color": color,
            "comment": fake.text(10)
        }
        return json.dumps(payload)
